from django.urls import path

from .views import TestView, FeedbackView, TestAsyncTaskView

app_name = 'web'
urlpatterns = [
    path('test/', TestView.as_view()),
    path('feedback/', FeedbackView.as_view()),
    path('async/', TestAsyncTaskView.as_view()),
]
