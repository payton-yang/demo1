from .celery_instance import app

from web.models import Tasks, TaskType


@app.task(name='async_task')
def test_create_task(task_name='payton'):
    print(11111)
    Tasks.objects.create(task_name=task_name, type=TaskType.ASYNC.value)


@app.task(name='sub')
def sub(x, y):
    print(f'{x} - {y} = {x - y}')
