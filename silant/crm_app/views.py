from django.http import HttpResponse
from django.shortcuts import render

from .models import Machine

menu = ['О нас', 'Обратная связь', 'Войти']


def index(request):
    machines = Machine.objects.all()
    return render(request, 'crm_app/index.html', {'machines': machines, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'crm_app/about.html', {'menu': menu, 'title': 'О нас'})


def login(request):
    return HttpResponse("LOGIN")
