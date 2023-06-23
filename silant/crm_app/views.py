from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# from django.db.models import Q

from .models import Machine, Maintenance, Claims, ServiceCompany


menu = [
    {'title': "Главная страница", 'url_name': 'index'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    # {'title': "Войти", 'url_name': 'login'},
]


machine_table_titles = ['Машина', 'Двигатель', 'Трансмиссия', 'Ведущий мост',
                        'Управляемый мост', 'Договор и Отгрузка', 'Грузополучатель', 'Дополнительно']
# machine_table_subtitles = ['Модель техники', 'Зав. № машины', 'Модель двигател', 'Зав. № двигателя', 'Модель трансмиссии', 'Зав. № трансмиссии', 'Модель ведущего моста', 'Зав. № ведущего моста', 'Модель управляемого моста',
#                            'Зав. № управляемого моста', 'Договор поставки №, дата', 'Грузополучатель (конечный потребитель)', 'Адрес поставки (эксплуатации)', 'Комплектация (дополнительные опции)', 'Клиент', 'Сервисная компания']


class MachinesHomePage(ListView):
    model = Machine
    template_name = 'crm_app/index.html'
    context_object_name = 'machines'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['machine_table_titles'] = machine_table_titles
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Machine.objects.all()


# def index(request):
#     machines = Machine.objects.all()
#     context = {
#         'machines': machines,
#         'machine_table_titles': machine_table_titles,
#         'menu': menu,
#         'title': 'Главная страница'
#     }
#     return render(request, 'crm_app/index.html', context=context)

def search_machine(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    if request.method == 'POST':
        searched = request.POST.get('searched', 'my_default_value')
        machine = Machine.objects.filter(serialNumber__icontains=searched)
        if machine:
            context['searched'] = searched
            context['machine'] = machine
            return render(request, 'crm_app/index.html', context=context)
        else:
            context['searched'] = 'Данных о машине с таким заводским номером в системе нет !!!'
            return render(request, 'crm_app/index.html', context=context)
        # return render(request, 'crm_app/search_machine.html', context=context)


def show_machine(request, machine_id):
    machine = get_object_or_404(Machine, pk=machine_id)
    claims = Claims.objects.filter(machine_id=machine_id)
    maintenance = Maintenance.objects.filter(machine_id=machine_id)

    context = {
        'machine': machine,
        'maintenance': maintenance,
        'claims': claims,
        'machine_table_titles': machine_table_titles,
        # 'machine_table_subtitles': machine_table_subtitles,
        'menu': menu,
        'title': f"Машина | зав. № = {machine.serialNumber}"
    }
    return render(request, 'crm_app/machine.html', context=context)


def page_after_authorization(request):
    user = request.user
    machines = Machine.objects.filter(client=user)
    if not machines:
        user = request.user.last_name
        service = ServiceCompany.objects.get(name=user)
        machines = Machine.objects.filter(serviceCompany=service)

    # machines = Machine.objects.filter(Q(client=user) | Q(serviceCompany=user))
    # claims = Claims.objects.filter(machine_id=machine_id)
    # maintenance = Maintenance.objects.filter(machine_id=machine_id)
    context = {
        'machines': machines,
        # 'maintenance': maintenance,
        # 'claims': claims,
        # 'machine_table_titles': machine_table_titles,
        # 'machine_table_subtitles': machine_table_subtitles,
        'menu': menu,
        'title': "Ваша база данных"
    }

    return render(request, 'crm_app/page_after_authorization.html', context=context)


def about(request):
    return render(request, 'crm_app/about.html', {'menu': menu, 'title': 'О нас'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")
