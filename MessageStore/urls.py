from django.urls import path
from .views import telegramMessage
urlpatterns = [
    path('message/', telegramMessage, name='telgramMessage')
]
