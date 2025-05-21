from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('api/customers/', views.CustomerAPI.as_view(), name='customer-api'),
]
