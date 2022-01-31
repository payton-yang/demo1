import json

from rest_framework.views import APIView
from rest_framework.response import Response

from web.models import Feedback
from utils.try_catch import MyExcept
from my_tasks.async_task import test_create_task


class TestView(APIView):
    def get(self, request):
        return Response(data={'code': 200, 'data': 'Test,Congratulations!!!'})


class TestAsyncTaskView(APIView):
    def get(self, request):
        name = request.GET.get('name', '')
        if not name:
            test_create_task.delay()
        else:
            test_create_task.delay(name)

        return Response(data={'code': 200, 'data': 'Async task start, Congratulations!!!'})


class FeedbackView(APIView):
    @MyExcept()
    def post(self, request):
        json_data = json.loads(request.body)
        if not json_data:
            return Response(data={'code': 200, 'data': 'Bang Bang gives you two punches....'})
        name = json_data.get('name', '')
        email = json_data.get('email', '')
        message = json_data.get('message', '')
        blog_url = json_data.get('blog_url', '')
        try:
            Feedback.objects.create(name=name, email=email, message=message, blog_url=blog_url)
        except Exception:
            return Response(data={'code': 200, 'data': 'WTF....Bang Bang gives you two punches....'})

        return Response(data={'code': 200, 'data': 'A smart kid!!!'})
