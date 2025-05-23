from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('customers/', views.CustomerAPI.as_view(), name='customer-api'),
    path('customers/<int:pk>/', views.CustomerAPI.as_view(), name='customer-detail'),
]
