from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect


from .utilities import *
# from django.db.models import Q

from .models import Machine, Maintenance, Claims, ServiceCompany, ModelMachine


class MachinesHomePage(DataMixin, ListView):
    model = Machine
    template_name = 'crm_app/index.html'
    context_object_name = 'machines'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

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
    user_client = request.user
    user_service = request.user.last_name

    if request.user.is_staff == True:
        return redirect('index')

    machines = Machine.objects.filter(
        client=user_client).order_by('modelMachine')
    if not machines:
        service = ServiceCompany.objects.get(name=user_service)
        machines = Machine.objects.filter(
            serviceCompany=service).order_by('modelMachine')

    maintenance = Maintenance.objects.filter(
        client=user_client).order_by('type')
    if not maintenance:
        service = ServiceCompany.objects.get(name=user_service)
        maintenance = Maintenance.objects.filter(
            serviceCompany=service).order_by('type')

    claims = Claims.objects.filter(client=user_client).order_by('machine')
    if not claims:
        service = ServiceCompany.objects.get(name=user_service)
        claims = Claims.objects.filter(
            serviceCompany=service).order_by('machine')

    context = {
        'machines': machines,
        'maintenance': maintenance,
        'claims': claims,
        # 'machine_table_titles': machine_table_titles,
        # 'machine_table_subtitles': machine_table_subtitles,
        'menu': menu,
        'title': "Ваша база данных"
    }

    return render(request, 'crm_app/page_after_authorization.html', context=context)


# ======================== Directories ========================


class DirectoryModelMachine(DataMixin, DetailView):
    model = ModelMachine
    template_name = 'crm_app/directoryModelMachine.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модель Вашей машины"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryModelMachineList(DataMixin, ListView):
    queryset = ModelMachine.objects.order_by('name')
    template_name = 'crm_app/directoryModelMachineList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='"Модели техники"')
        return dict(list(context.items()) + list(c_def.items()))

# =============================================================
 

def about(request):
    return render(request, 'crm_app/about.html', {'menu': menu, 'title': 'О нас'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


# def login(request):
#     return HttpResponse("Авторизация")
