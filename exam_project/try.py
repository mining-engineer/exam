
from pathlib import Path
from dotenv import load_dotenv
import os
import pymysql
pymysql.install_as_MySQLdb()


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Используем MySQL/MariaDB
        'NAME': os.getenv('BDNAME'),                      # Имя вашей базы данных
        'USER': os.getenv('BDUSER'),            # Имя пользователя базы данных
        'PASSWORD': os.getenv('PASSWORD'),              # Пароль пользователя
        'HOST': os.getenv('HOST'),                   # Хост базы данных (обычно 'localhost')
        'PORT': '3306',                        # Порт базы данных (по умолчанию 3306 для MySQL/MariaDB)
        'OPTIONS': {
            'charset': 'NAME',              # Кодировка (опционально)
        },
    }
}

print(os.getenv('BDNAME'),os.getenv('BDUSER'),os.getenv('PASSWORD'),os.getenv('HOST'))