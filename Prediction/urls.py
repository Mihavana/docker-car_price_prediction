from django.urls import path
from .views import home, predict_price, clear_history, dashboard

urlpatterns = [
    path('', home, name='home'),
    path('predict-price/', predict_price, name='predict_price'),
    path('clear-history/', clear_history, name='clear_history'),
    path('dashboard/', dashboard, name='dashboard'),
]
