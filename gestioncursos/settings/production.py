
# SECURITY WARNING: don't run with debug turned on in production!
from .base import *
from decouple import config


DEBUG = False

ALLOWED_HOSTS = ['gestioncursos.es']

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
        'OPTIONS': {
          'autocommit': True,
       
        },
    }
}