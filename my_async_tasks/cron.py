import os
import pathlib
from datetime import datetime

from celery import shared_task


@shared_task(name='test_cron')
def test_cron(x, y):
    print(f'test: {x} + {y} = {x + y}')


@shared_task(name='cron_add_file')
def test_add_file():
    """
    定时任务创建txt文件
    :return:
    """

    path = pathlib.Path('/www/test_cron')
    if not os.path.exists(path):
        os.makedirs(path)
    now = datetime.now()
    dest_file = path / f'{now}.txt'
    with open(dest_file, 'w+', encoding='utf-8') as f:
        f.write(str(now))
