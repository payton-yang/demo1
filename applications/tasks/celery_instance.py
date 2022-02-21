import os

import django
from celery import Celery, platforms
from django.conf import settings

from applications.tasks import celery_config

platforms.C_FORCE_ROOT = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.dev')
django.setup()

RABBIT_MQ_USER = "root"
RABBIT_MQ_PASSWORD = "root"
RABBIT_MQ_PORT = 5672
if settings.ENV_DEV:
    RABBIT_MQ_IP = "127.0.0.1"
else:
    RABBIT_MQ_IP = "rabbitmq"  # docker容器的IP地址

app = Celery(
    "celery",
    broker="amqp://{0}:{1}@{2}:{3}/broker".format(
        RABBIT_MQ_USER, RABBIT_MQ_PASSWORD, RABBIT_MQ_IP, RABBIT_MQ_PORT
    )
)

app.config_from_object(celery_config, silent=True, force=True)

# app.autodiscover_tasks(['my_task'], 'async_task')
# celery worker -A async_task.celery_instance -l info --pool=solo   error
# celery -A applications.tasks.celery_instance worker -l info --pool=solo 正确启动
# celery -A applications.tasks.celery_instance beat -l info  定时任务
