from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '116.62.27.195']
APPEND_SLASH = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
