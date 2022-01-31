import time
from enum import Enum
from django.db import models


class BaseModel(models.Model):
    created_at = models.IntegerField(
        verbose_name='创建时间', null=False, blank=False, default=int(time.time()))
    updated_at = models.IntegerField(
        verbose_name='修改时间', null=False, blank=False, default=int(time.time()))
    format_created_at = models.DateTimeField(
        verbose_name="格式化时间", auto_now=True)
    format_updated_at = models.DateTimeField(
        verbose_name="格式化修改时间", auto_now_add=True)

    class Meta:
        abstract = True


class TaskType(Enum):
    ASYNC = 'async task'
    TIMED = 'timed task'
    UNKNOWN = 'unknown task'


class Tasks(BaseModel):
    TYPE = [
        (0, 'async task'),
        (1, 'timed task'),
        (-1, 'unknown task'),
    ]
    task_name = models.CharField(verbose_name='名称', max_length=200, null=False, blank=False)
    type = models.CharField(verbose_name='状态', max_length=20, null=False, blank=False, choices=TYPE,
                            default=TaskType.UNKNOWN.value)

    class Meta:
        db_table = 'tasks'


class Feedback(BaseModel):
    name = models.CharField(verbose_name='名称', max_length=50, null=False, blank=False)
    email = models.CharField(verbose_name='邮箱', max_length=200, null=False, blank=False)
    message = models.TextField(verbose_name='留言', null=False, blank=False)
    blog_url = models.CharField(verbose_name='博客地址', max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'feedback'
