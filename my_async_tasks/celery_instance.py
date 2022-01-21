import os

from celery import Celery, platforms

from my_task import celery_config

platforms.C_FORCE_ROOT = True
DEV = 0
PROD = 1
if PROD:
    RABBIT_MQ_USER = "payton"
    RABBIT_MQ_PASSWORD = "payton"
    RABBIT_MQ_PORT = 5673
if DEV:
    RABBIT_MQ_USER = "root"
    RABBIT_MQ_PASSWORD = "root"
    RABBIT_MQ_PORT = 5672
RABBIT_MQ_IP = "127.0.0.1"
# 必须填写 否则会报错: cannot load settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_fjisu_task.settings')

app = Celery(
    "celery",
    broker="amqp://{0}:{1}@{2}:{3}/broker".format(
        RABBIT_MQ_USER, RABBIT_MQ_PASSWORD, RABBIT_MQ_IP, RABBIT_MQ_PORT
    )
)

app.config_from_object(celery_config, silent=True, force=True)

# app.autodiscover_tasks(['my_task'], 'async_task')
# celery worker -A async_task.celery_instance -l info --pool=solo   error
# celery -A my_task.celery_instance worker -l info --pool=solo 正确启动
# celery -A my_task.celery_instance beat -l info  定时任务
