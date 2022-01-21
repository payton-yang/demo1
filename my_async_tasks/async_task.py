import os
import pathlib
from datetime import datetime

from celery import shared_task


@shared_task(name='aysnc_add_file')
def test_create_file(file_name='payton'):
    """
    创建文件
    :param file_name:
    :return:
    """
    path = pathlib.Path('/www/test_async')
    if not os.path.exists(path):
        os.makedirs(path)
    now = datetime.now()
    dest_file = path / f'{file_name}-{now}.txt'
    with open(dest_file, 'w+', encoding='utf-8') as f:
        f.write(f'{file_name}-{now}--async task success')


@shared_task(name='sub')
def sub(x, y):
    print(f'{x} - {y} = {x - y}')
