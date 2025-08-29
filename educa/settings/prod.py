# educa/settings/prod.py

from decouple import config
from .base import *

DEBUG = False

ADMINS = [
    ('Maryna Sam', 'marautumn@gmail.com'),
]

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # <-- Здесь хост вашего SMTP-сервера. Для Gmail это 'smtp.gmail.com'.
EMAIL_PORT = 587             # <-- Порт для TLS/STARTTLS. Для Gmail это 587.
EMAIL_USE_TLS = True         # <-- Использовать TLS (Transport Layer Security) для защищенного соединения.
# EMAIL_USE_SSL = False      # <-- Если используете SSL (порт 465), то это True, а USE_TLS = False.
                             #     Для Gmail с 587 портом используйте USE_TLS = True.

EMAIL_HOST_USER = 'marautumn@gmail.com'  # <-- ВАШ АДРЕС ОТПРАВИТЕЛЯ (например, my.educa.platform.mail@gmail.com)
EMAIL_HOST_PASSWORD = 'txho zazl jzmp ngpk' # <-- ПАРОЛЬ ОТ ВАШЕГО EMAIL-АККАУНТА ИЛИ ПАРОЛЬ ПРИЛОЖЕНИЯ
DEFAULT_FROM_EMAIL = 'Educa Platform <noreply@educaproject.com>' # <-- Адрес и имя отправителя по умолчанию
SERVER_EMAIL = 'marautumn@gmail.com' # <-- Email для ошибок сервера. Можно использовать ваш админский email.