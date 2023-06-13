from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Machine

menu = [
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
    {'title': "Главная страница", 'url_name': 'index'},

]


machine_table_titles = ['Машина', 'Двигатель', 'Трансмиссия', 'Ведущий мост',
                        'Управляемый мост', 'Договор и Отгрузка', 'Грузополучатель', 'Дополнительно']
# machine_table_subtitles = ['Модель техники', 'Зав. № машины', 'Модель двигател', 'Зав. № двигателя', 'Модель трансмиссии', 'Зав. № трансмиссии', 'Модель ведущего моста', 'Зав. № ведущего моста', 'Модель управляемого моста',
#                            'Зав. № управляемого моста', 'Договор поставки №, дата', 'Грузополучатель (конечный потребитель)', 'Адрес поставки (эксплуатации)', 'Комплектация (дополнительные опции)', 'Клиент', 'Сервисная компания']


def index(request):
    machines = Machine.objects.all()
    context = {
        'machines': machines,
        'machine_table_titles': machine_table_titles,
        # 'machine_table_subtitles': machine_table_subtitles,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'crm_app/index.html', context=context)


def show_machine(request, machine_id):
    machine = get_object_or_404(Machine, pk=machine_id)

    context = {
        'machine': machine,
        'machine_table_titles': machine_table_titles,
        # 'machine_table_subtitles': machine_table_subtitles,
        'menu': menu,
        'title': f"Машина | зав. № = {machine.serialNumber}"
    }
    return render(request, 'crm_app/machine.html', context=context)


def about(request):
    return render(request, 'crm_app/about.html', {'menu': menu, 'title': 'О нас'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")
