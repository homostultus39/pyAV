FROM python:3.9-slim

# Установите зависимости
RUN pip install flask
RUN pip install yara-python
# Создание рабочей директории приложения внутри образа
WORKDIR /app

# Копирование файлов в директорию приложения внутри образа
COPY hshsumm/main.hdb /app/hshsumm/main.hdb
COPY hshsumm/main.mdb /app/hshsumm/main.mdb
COPY hshsumm/sign_paths.py /app/hshsumm/sign_paths.py
COPY yararules /app/

COPY pars_yara_rules_filepath.py /app/
COPY virus_scanner.py /app/
COPY run_server.py /app/

ENV IN_DOCKER=1

# команда, которая будет запускать сервер Flask при запуске контейнера
CMD ["python", "run_server.py"]