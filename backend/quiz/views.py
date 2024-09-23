from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def get_time(request):
    # Пример данных, которые будут отправлены в ответе
    data = {
        "Name": "TEST",
        "Age": 30,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "programming": "Python"
    }
    return JsonResponse(data)
