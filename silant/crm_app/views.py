from django.http import HttpResponse
from django.shortcuts import render

menu = ['О нас', 'Обратная связь', 'Войти']


def index(request):
    return render(request, 'crm_app/index.html', {'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'crm_app/about.html', {'menu': menu, 'title': 'О нас'})


def login(request):
    return HttpResponse("LOGIN")
