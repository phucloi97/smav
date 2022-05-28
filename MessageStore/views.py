from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.


def telegramMessage(request):
    r = requests.get(
        'https://api.telegram.org/bot1998485541:AAHhj2MOxxzvhPvluPmOfqYokmCTde1jKvA/sendMessage?chat_id=@wellcomtest&text=test')
    return HttpResponse('ok')
