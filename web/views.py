import json

from rest_framework.views import APIView
from rest_framework.response import Response

from web.models import Feedback
from my_async_tasks.async_task import test_create_file


class TestView(APIView):
    def get(self, request):
        return Response(data={'code': 200, 'data': 'Async task started,Congratulations!!!'})


class TestAsyncTaskView(APIView):
    def get(self, request):
        test_create_file.delay()
        return Response(data={'code': 200, 'data': 'success test,Congratulations!!!'})


class FeedbackView(APIView):
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
