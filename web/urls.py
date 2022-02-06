from django.urls import path
from django.views.decorators.cache import cache_page

from .views import TestView, FeedbackView, TestAsyncTaskView, TestRedisCache

app_name = 'web'
urlpatterns = [
    path('test', TestView.as_view()),
    path('feedback', FeedbackView.as_view()),
    path('async', TestAsyncTaskView.as_view()),
    # path('redis', TestRedisCache.as_view()),
    path('redis', cache_page(60)(TestRedisCache.as_view())),
]
