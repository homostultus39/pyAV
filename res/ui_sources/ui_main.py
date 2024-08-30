# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'virwiz.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QWidget)
import res.ui_sources.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1063, 618)
        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(45, 12, 109, 0.8), stop:0.427447 rgba(95, 12, 109, 0.8), stop:1 rgba(45, 12, 109, 0.8));\n"
"font-family: Montserrat-Bold;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.selective_scan_button = QPushButton(self.centralwidget)
        self.selective_scan_button.setObjectName(u"selective_scan_button")
        self.selective_scan_button.setGeometry(QRect(800, 267, 231, 51))
        font = QFont()
        font.setFamilies([u"Montserrat-Bold"])
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.selective_scan_button.setFont(font)
        self.selective_scan_button.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70)\n"
"}")
        self.selective_scan_button.setAutoDefault(False)
        self.selective_scan_button.setFlat(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 61))
        font1 = QFont()
        font1.setFamilies([u"Motserrat-Bold"])
        font1.setPointSize(32)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid rgba(255, 255, 255, 0);\n"
"font-family: Motserrat-Bold;\n"
"color: white;")
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setMargin(0)
        self.label.setIndent(-1)
        self.fast_scan_button = QPushButton(self.centralwidget)
        self.fast_scan_button.setObjectName(u"fast_scan_button")
        self.fast_scan_button.setGeometry(QRect(800, 327, 231, 51))
        self.fast_scan_button.setFont(font)
        self.fast_scan_button.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70)\n"
"}")
        self.fast_scan_button.setAutoDefault(False)
        self.fast_scan_button.setFlat(False)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 80, 311, 16))
        font2 = QFont()
        font2.setFamilies([u"Montserrat-Bold"])
        font2.setBold(True)
        font2.setItalic(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: white;")
        self.virus_table = QTableView(self.centralwidget)
        self.virus_table.setObjectName(u"virus_table")
        self.virus_table.setGeometry(QRect(50, 148, 701, 381))
        self.virus_table.setStyleSheet(u"QTableView:section {\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border: 1px solid rgba(255, 255, 255, 30);\n"
"height: 50px;\n"
"font-size:14pt\n"
"}\n"
"QTableView:item {\n"
"border: 1px solid rgba(255, 255, 255, 30); \n"
"color: white;\n"
"}")
        self.virus_table.setLineWidth(10)
        self.scanning_label = QLabel(self.centralwidget)
        self.scanning_label.setObjectName(u"scanning_label")
        self.scanning_label.setGeometry(QRect(52, 564, 980, 20))
        font3 = QFont()
        font3.setFamilies([u"Montserrat-Bold"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setItalic(False)
        self.scanning_label.setFont(font3)
        self.scanning_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: white;")
        self.del_clear_button = QPushButton(self.centralwidget)
        self.del_clear_button.setObjectName(u"del_clear_button")
        self.del_clear_button.setGeometry(QRect(750, 475, 71, 61))
        self.del_clear_button.setFont(font)
        self.del_clear_button.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius:7px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.del_clear_button.setIcon(icon1)
        self.del_clear_button.setIconSize(QSize(60, 60))
        self.del_clear_button.setAutoDefault(False)
        self.del_clear_button.setFlat(False)
        self.feedback_button = QPushButton(self.centralwidget)
        self.feedback_button.setObjectName(u"feedback_button")
        self.feedback_button.setGeometry(QRect(950, 18, 91, 81))
        self.feedback_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/Telegram_logo.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.feedback_button.setIcon(icon2)
        self.feedback_button.setIconSize(QSize(60, 60))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 10, 20, 20))
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.label_4.setPixmap(QPixmap(u":/logo/mainwindow_logo.png"))
        self.label_4.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.selective_scan_button.setDefault(False)
        self.fast_scan_button.setDefault(False)
        self.del_clear_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"virwizz", None))
        self.selective_scan_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440\u043e\u0447\u043d\u0430\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Virus Wizzard", None))
        self.fast_scan_button.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u0430\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421 \u0437\u0430\u0431\u043e\u0442\u043e\u0439 \u043e \u0432\u0430\u0448\u0435\u0439 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438", None))
        self.scanning_label.setText("")
        self.del_clear_button.setText("")
        self.feedback_button.setText("")
        self.label_4.setText("")
    # retranslateUi

