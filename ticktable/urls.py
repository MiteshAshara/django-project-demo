from django.urls import path
from . import views

app_name = 'ticktable'

urlpatterns = [
    path('live-price/', views.live_price_view, name='live_price'),
    path('price-history/', views.price_history_view, name='price_history'),
    path('api/update-price/', views.update_price, name='update_price'),
    path('api/get-latest-price/', views.get_latest_price, name='get_latest_price'),
    path('api/price-history/', views.get_price_history, name='price_history_api'),
]
