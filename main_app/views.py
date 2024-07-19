from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context: dict = {
        'title': 'Home',
        'content': 'Главная страница магазина Аптека V'
    }
    return render(request, 'main_app/index.html', context)

def about(request):
    return HttpResponse('About us')
