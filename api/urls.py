from django.urls import path
from .views import StudentAPI

app_name = 'api'

urlpatterns = [
    path('', StudentAPI.as_view(), name='api-root'),
    path('', StudentAPI.as_view(), name='student-list'),
]
