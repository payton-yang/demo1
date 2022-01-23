from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '116.62.27.195']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}
