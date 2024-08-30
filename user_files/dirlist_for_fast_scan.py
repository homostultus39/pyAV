import os
import time
from itertools import chain

# Директории для проверки
system_directories = [
    os.path.join(os.environ['SystemRoot'], 'System32'),  # System32
    os.path.join(os.environ['SystemRoot'], 'SysWOW64')  # Для 64-битных систем
]

startup_directories = [
    os.path.join(os.environ['SystemDrive'], 'ProgramData', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup'),
    os.path.join(os.environ['AppData'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
]

temp_directories = [
    os.environ['TEMP'],  # Переменная среды TEMP
    os.environ['TMP']  # Переменная среды TMP
]

# Функция для фильтрации файлов по типу и дате модификации
def filter_files(directory, extensions, max_days_old=30):
    current_time = time.time()
    max_age = max_days_old * 86400  # Максимальный возраст файла в секундах

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                file_path = os.path.join(root, file)
                file_stat = os.stat(file_path)
                file_age = current_time - file_stat.st_mtime

                if file_age <= max_age:
                    yield file_path

# Типы файлов, которые будем проверять
file_extensions_to_check = ('.exe', '.dll', '.sys', '.bat')

# Собираем файлы из всех каталогов для проверки с фильтрацией по возрасту
file_paths = list(chain.from_iterable(
    filter_files(directory, file_extensions_to_check) for directory in
    system_directories + startup_directories + temp_directories
))

# Выводим количество найденных файлов для проверки
print(f"Количество файлов для проверки: {len(file_paths)}")
