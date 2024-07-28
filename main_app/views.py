from django.shortcuts import render
from django.http import HttpResponse

from products_app.models import Categories

def index(request):

    context: dict = {
        'title': 'Home - Главная страница магазина Аптека (V)',
        'content': 'Магазин Аптека (V)',

    }
    return render(request, 'main_app/index1.html', context)

def about(request):
    context: dict = {
        'title': 'Home - О нас',
        'content': 'Адрес Телефон',
        'text_page': 'Наши преимущества',
    }
    return render(request, 'main_app/about.html', context)

