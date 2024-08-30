import json
import os
import sys
import aiohttp
import asyncio
import time
import webbrowser as wb

from PySide6.QtCore import Qt, QThreadPool, QRunnable, QObject, Signal, Slot
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QHeaderView, QMessageBox

from res.ui_sources.ui_main import Ui_MainWindow
from dirlist_for_fast_scan import file_paths
from user_files.check_file_weight import check_signature_file_weight
from user_files.check_signature_integrity import check_signature_integrity_hash

class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    no_virus_found = Signal()
    update_status = Signal(str)

class ScannerWorker(QRunnable):
    def __init__(self, file_path, is_fast_scan):
        super().__init__()
        self.file_path = file_path
        self.is_fast_scan = is_fast_scan
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.async_run())
        except Exception as e:
            self.signals.error.emit((type(e), e.args))
        finally:
            self.signals.finished.emit()

    async def async_run(self):
        try:
            self.signals.update_status.emit(f"Проверяется: {self.file_path}")

            weight_check = check_signature_file_weight(self.file_path)

            if weight_check:
                url = 'http://localhost:5000/scan'
                async with aiohttp.ClientSession() as session:
                    with open(self.file_path, "rb") as f:
                        start_time = time.time()
                        data = aiohttp.FormData()
                        data.add_field('file', f, filename=self.file_path)
                        data.add_field('matches', json.dumps(weight_check))
                        async with session.post(url, data=data) as response:
                            response_text = await response.text()
                            elapsed_time = time.time() - start_time
                            print(f"Проверка файла {self.file_path} заняла {elapsed_time:.2f} секунд")
                            response_text = response_text.strip()
                            if response_text:
                                item_file_path = QStandardItem(self.file_path)
                                item_scan_result = QStandardItem(response_text)
                                item_scan_result.setTextAlignment(Qt.AlignCenter)
                                self.signals.result.emit((item_file_path, item_scan_result))

                    time.sleep(1)

                if not response_text:
                    self.signals.no_virus_found.emit()
            else:
                self.signals.no_virus_found.emit()
        except Exception as e:
            self.signals.error.emit((type(e), e.args))


class VirusWizzard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.virus_table_model = QStandardItemModel()
        self.virus_table_model.setHorizontalHeaderLabels(["File Path", "Scan Result"])
        self.ui.virus_table.setModel(self.virus_table_model)

        header = self.ui.virus_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        self.ui.selective_scan_button.clicked.connect(self.selective_scan)
        self.ui.fast_scan_button.clicked.connect(self.fast_scan)
        self.ui.feedback_button.clicked.connect(self.feedback)
        self.ui.del_clear_button.clicked.connect(self.delete_virus_files)

        self.threadpool = QThreadPool.globalInstance()
        self.threadpool.setMaxThreadCount(5)

        self.total_files_to_scan = 0
        self.scanned_files_count = 0
        self.viruses_found = False
        self.is_fast_scan = False

        if not check_signature_integrity_hash():
            QMessageBox.warning(self, "Ошибка", "Целостность сигнатур нарушена.")

    def handle_worker_error(self, error):
        print("Error:", error)

    def handle_worker_result(self, result):
        self.scanned_files_count += 1
        item_file_path, item_scan_result = result
        row_position = self.virus_table_model.rowCount()
        self.virus_table_model.setItem(row_position, 0, item_file_path)
        self.virus_table_model.setItem(row_position, 1, item_scan_result)
        self.viruses_found = True
        if not self.is_fast_scan:
            self.ui.scanning_label.setText("Сканирование завершено")

    def handle_no_virus_found(self):
        self.scanned_files_count += 1
        if not self.is_fast_scan:
            self.ui.scanning_label.setText("Вирусов не обнаружено")

    def update_scanning_label(self, text):
        self.ui.scanning_label.setText(text)

    def selective_scan(self):
        self.is_fast_scan = False
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Select File', '', 'All Files (*)')
        if file_path:
            self.ui.scanning_label.setText(f"Проверяется: {file_path}")
            self.scan_file_in_thread(file_path)

    def fast_scan(self):
        self.is_fast_scan = True
        self.ui.scanning_label.setText("Сканирование...")
        self.total_files_to_scan = len(file_paths)
        self.scanned_files_count = 0
        self.viruses_found = False
        for file in file_paths:
            self.scan_file_in_thread(file)

    def scan_file_in_thread(self, file_path):
        worker = ScannerWorker(file_path, self.is_fast_scan)
        worker.signals.result.connect(self.handle_worker_result)
        worker.signals.error.connect(self.handle_worker_error)
        worker.signals.no_virus_found.connect(self.handle_no_virus_found)
        worker.signals.update_status.connect(self.update_scanning_label)
        worker.signals.finished.connect(self.check_fast_scan_completion)
        self.threadpool.start(worker)

    def check_fast_scan_completion(self):
        if self.is_fast_scan and self.scanned_files_count == self.total_files_to_scan:
            if self.viruses_found:
                self.ui.scanning_label.setText("Сканирование завершено")
            else:
                self.ui.scanning_label.setText("Вирусов не обнаружено")

    def feedback(self):
        try:
            wb.open_new_tab('https://t.me/@eperniytea3')
        except Exception as e:
            pass

    def delete_virus_files(self):
        if self.virus_table_model.rowCount() == 0:
            QMessageBox.information(self, "Информация", "Нет файлов для удаления.")
            return

        # Запрашиваем подтверждение удаления
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Подтверждение удаления")
        message_box.setText("Вы уверены, что хотите удалить все файлы из списка?")
        message_box.setIcon(QMessageBox.Question)

        # Используем CSS для сделания текста белым
        message_box.setStyleSheet("QLabel { color : white; }")

        # Устанавливаем тип кнопок
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        reply = message_box.exec()
        if reply == QMessageBox.Yes:
            for row in range(self.virus_table_model.rowCount()):
                file_item = self.virus_table_model.item(row, 0)
                file_path = file_item.text()
                try:
                    os.remove(file_path)
                    self.virus_table_model.removeRow(row)
                except Exception as e:
                    print("Ошибка при удалении файла:", e)

def main():
    app = QApplication(sys.argv)
    window = VirusWizzard()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
