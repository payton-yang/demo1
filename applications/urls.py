from django.urls import path, include

app_name = 'v1'
urlpatterns = [
    path('test/', include('applications.test_web.urls'))
]
