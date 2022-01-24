import os

from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '116.62.27.195']
APPEND_SLASH = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '172.17.0.1',
        'PORT': 5432,
    }
}

# 静态文件
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
