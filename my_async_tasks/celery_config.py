from kombu import Exchange, Queue
# default exchange
default_exchange = Exchange('default', type='direct')

# webhook exchange
email_exchange = Exchange("email", type='direct')

# create queue
CELERY_QUEUES = (
    Queue('default', default_exchange, routing_key='default', max_priority=10),
    Queue('email', email_exchange, routing_key='email', max_priority=1),
)

CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_ROUTING_KEY = 'default'
EMAIL_QUEUE = "email"

# timezone
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_CONCURRENCY = 4  # 并发worker数

CELERY_CREATE_MISSING_QUEUES = True  # 某个程序中出现的队列，在broker中不存在，则立刻创建它

CELERYD_FORCE_EXECV = True  # 非常重要,有些情况下可以防止死锁

CELERYD_PREFETCH_MULTIPLIER = 1

CELERY_DISABLE_RATE_LIMITS = True  # 任务发出后，经过一段时间还未收到acknowledge , 就将任务重新交给其他worker执行

CELERY_IMPORTS = [
    "my_async_tasks.async_task",
    "my_async_tasks.cron",
]

CELERY_ROUTES = (
    {
    },
)

# 定时任务
CELERYBEAT_SCHEDULE = {
    "test_cron": {
        "task": "test_cron",  # 建议填写task的name, 这样就不用填写路径和考虑路径带来的问题了 注意name不能重复
        # "schedule": crontab(minute="*/1"),
        # "schedule": timedelta(seconds=10),  # 10秒跑一次
        "schedule": 10,  # 这也是10秒跑一次
        "args": (12, 32)
    },
    "cron_add_task": {
        "task": "cron_add_task",
        "schedule": 5,  # 5秒跑一次
        "args": ()
    },
}
