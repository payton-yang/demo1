import os

from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test2',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '172.17.0.1',
        'PORT': 5432,
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
