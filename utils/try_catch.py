import traceback
from functools import wraps
from datetime import datetime

from rest_framework.response import Response


class MyExcept:

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                sign = '=' * 60 + '\n'
                print(f'{sign}>>>异常时间：\t{datetime.now()}\n>>>异常函数：\t{func.__name__}')
                print(f'{sign}{traceback.format_exc()}{sign}')
                return Response(data={'code': 500, 'data': 'Bad boy, screwed up the system!!!'})

        return wrapper
