import os
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'snapp',
        'USER': 'postgres',
        'PASSWORD': 'U2RN82C46KD!',
        'HOST': 'db',
        'PORT': 5432
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'errMsg': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'errLog.log'),
            'when': 'D',  # this specifies the interval
            'interval': 1,  # defaults to 1, only necessary for other values
            'backupCount': 0,  # how many backup file to keep, 10 days
            'formatter': 'standard',
        },
    },
    'loggers': {
        'errMsg': {
            'handlers': ['errMsg', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

# redis
REDIS_SERVER = 'redis'
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://" + REDIS_SERVER + ":6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "password",
        }
    }
}