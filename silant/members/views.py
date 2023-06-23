from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

menu = [
    {'title': "Главная страница", 'url_name': 'index'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Обратная связь", 'url_name': 'contact'},
]


def login_user(request):
    context = {
        'menu': menu,
        'title': 'Вход в систему'
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('page_after_authorization')
        else:
            messages.success(
                request, ('Проблема с логином или паролем, попробуйте ещё раз ...'))
            return redirect('login')
    else:
        return render(request, "authentication/login.html", context=context)


def logout_user(request):
    logout(request)
    messages.success(
        request, ('Вы вышли из своего личного кабинета'))
    return redirect('index')
