from django.urls import path
from .views import CustomerAPI

app_name = 'api_customer'

urlpatterns = [
    path('', CustomerAPI.as_view(), name='customer-list'),
]
