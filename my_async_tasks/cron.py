from datetime import datetime

from celery import shared_task

from web.models import Tasks, TaskType


@shared_task(name='test_cron')
def test_cron(x, y):
    print(f'test: {x} + {y} = {x + y}')


@shared_task(name='cron_add_task')
def test_add_file():
    """
    定时在数据库创建任务
    :return:
    """
    name = str(datetime.now())
    Tasks.objects.create(task_name=name, type=TaskType.TIMED.value)
