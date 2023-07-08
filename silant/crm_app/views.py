from typing import Any

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from .filter import ClaimsFilter, MachineFilter, MaintenanceFilter
from .models import (Breakdown, Claims, Machine, Maintenance, MaintenanceType,
                     ModelDriveAxle, ModelEngine, ModelMachine,
                     ModelSteeringAxle, ModelTransmission, RecoveryMethod,
                     ServiceCompany)
from .utilities import *
from .forms import *


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


@login_required()
def full_db_list(request):

    filter_machines = MachineFilter(
        request.GET, queryset=Machine.objects.all().order_by('-shipmentDate'))
    filter_maintenance = MaintenanceFilter(
        request.GET, queryset=Maintenance.objects.all().order_by('-maintenanceDate'))
    filter_claims = ClaimsFilter(
        request.GET, queryset=Claims.objects.all().order_by('-breakdownDate'))

    context = {
        'filter_machines': filter_machines,
        'filter_maintenance': filter_maintenance,
        'filter_claims': filter_claims,
        'menu': menu,
        'title': "Ваша база данных"
    }

    return render(request, 'crm_app/full_db_list.html', context=context)


@login_required()
def page_after_authorization(request):
    user_client = request.user
    user_service = request.user.last_name

    if request.user.is_staff == True:
        return redirect('full_db_list')

    filter_machines = MachineFilter(request.GET, queryset=Machine.objects.filter(
        client=user_client).order_by('-shipmentDate'))
    if not filter_machines:
        service = ServiceCompany.objects.get(name=user_service)
        filter_machines = MachineFilter(request.GET, queryset=Machine.objects.filter(
            serviceCompany=service).order_by('-shipmentDate'))

    filter_maintenance = MaintenanceFilter(request.GET, queryset=Maintenance.objects.filter(
        client=user_client).order_by('-maintenanceDate'))
    if not filter_maintenance:
        service = ServiceCompany.objects.get(name=user_service)
        filter_maintenance = MaintenanceFilter(request.GET, queryset=Maintenance.objects.filter(
            serviceCompany=service).order_by('-maintenanceDate'))

    filter_claims = ClaimsFilter(request.GET, queryset=Claims.objects.filter(
        client=user_client).order_by('-breakdownDate'))
    if not filter_claims:
        service = ServiceCompany.objects.get(name=user_service)
        filter_claims = ClaimsFilter(request.GET, queryset=Claims.objects.filter(
            serviceCompany=service).order_by('-breakdownDate'))

    context = {
        'filter_machines': filter_machines,
        'filter_maintenance': filter_maintenance,
        'filter_claims': filter_claims,
        'menu': menu,
        'title': "Ваша база данных"
    }

    return render(request, 'crm_app/page_after_authorization.html', context=context)


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


@login_required()
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

# =========================== CRUD ===========================


class AddMachine(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddMachineForm
    template_name = 'crm_app/crud_add_machine.html'
    success_url = reverse_lazy('index')
    # login_url = reverse_lazy('login_user')
    raise_exception = True
    # вывести '403 Forbidden' для неавторизованного пользователя
    # (закоментить строку - тогда перенаправление на 'home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление Машины")
        return dict(list(context.items()) + list(c_def.items()))


class AddMaintenance(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddMaintenanceForm
    template_name = 'crm_app/crud_add_maintenance.html'
    success_url = reverse_lazy('index')
    # login_url = reverse_lazy('login_user')
    raise_exception = True
    # вывести '403 Forbidden' для неавторизованного пользователя
    # (закоментить строку - тогда перенаправление на 'home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление ТО")
        return dict(list(context.items()) + list(c_def.items()))


# ======================== DIRECTORIES ========================


class DirectoryModelMachine(LoginRequiredMixin, DataMixin, DetailView):
    model = ModelMachine
    template_name = 'crm_app/directoryModelMachine.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модель Вашей машины"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryModelMachineList(LoginRequiredMixin, DataMixin, ListView):
    queryset = ModelMachine.objects.order_by('name')
    template_name = 'crm_app/directoryModelMachineList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='"Модели техники"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryModelEngine(LoginRequiredMixin, DataMixin, DetailView):
    model = ModelEngine
    template_name = 'crm_app/directoryModelEngine.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модель двигателя"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryModelEngineList(LoginRequiredMixin, DataMixin, ListView):
    queryset = ModelEngine.objects.order_by('name')
    template_name = 'crm_app/directoryModelEngineList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модели двигателей"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryModelTransmission(LoginRequiredMixin, DataMixin, DetailView):
    model = ModelTransmission
    template_name = 'crm_app/directoryModelTransmission.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модель трансмиссии"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryModelTransmissionList(LoginRequiredMixin, DataMixin, ListView):
    queryset = ModelTransmission.objects.order_by('name')
    template_name = 'crm_app/directoryModelTransmissionList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модели трансмиссий"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryModelDriveAxle(LoginRequiredMixin, DataMixin, DetailView):
    model = ModelDriveAxle
    template_name = 'crm_app/directoryModelDriveAxle.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модель ведущего моста"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryModelDriveAxleList(LoginRequiredMixin, DataMixin, ListView):
    queryset = ModelDriveAxle.objects.order_by('name')
    template_name = 'crm_app/directoryModelDriveAxleList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модели ведущего моста"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryModelSteeringAxle(LoginRequiredMixin, DataMixin, DetailView):
    model = ModelSteeringAxle
    template_name = 'crm_app/directoryModelSteeringAxle.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модель управляемого моста"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryModelSteeringAxleList(LoginRequiredMixin, DataMixin, ListView):
    queryset = ModelSteeringAxle.objects.order_by('name')
    template_name = 'crm_app/directoryModelSteeringAxleList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модели управляемого моста"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryMaintenanceType(LoginRequiredMixin, DataMixin, DetailView):
    model = MaintenanceType
    template_name = 'crm_app/directoryMaintenanceType.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Вид Технического Обслуживания"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryMaintenanceTypeList(LoginRequiredMixin, DataMixin, ListView):
    queryset = MaintenanceType.objects.order_by('name')
    template_name = 'crm_app/directoryMaintenanceTypeList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Виды Технического Обслуживания"')
        return dict(list(context.items()) + list(c_def.items()))
    # ---------------------------------------------------------------


class DirectoryBreakdown(LoginRequiredMixin, DataMixin, DetailView):
    model = Breakdown
    template_name = 'crm_app/directoryBreakdown.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Узел отказа"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryBreakdownList(LoginRequiredMixin, DataMixin, ListView):
    queryset = Breakdown.objects.order_by('name')
    template_name = 'crm_app/directoryBreakdownList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='"Узлы отказа"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryRecoveryMethod(LoginRequiredMixin, DataMixin, DetailView):
    model = RecoveryMethod
    template_name = 'crm_app/directoryRecoveryMethod.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Способ восстановления"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryRecoveryMethodList(LoginRequiredMixin, DataMixin, ListView):
    queryset = RecoveryMethod.objects.order_by('name')
    template_name = 'crm_app/directoryRecoveryMethodList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Способы восстановления"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryServiceCompany(LoginRequiredMixin, DataMixin, DetailView):
    model = ServiceCompany
    template_name = 'crm_app/directoryServiceCompany.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Сервисная компания"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryServiceCompanyList(LoginRequiredMixin, DataMixin, ListView):
    queryset = ServiceCompany.objects.order_by('name')
    template_name = 'crm_app/directoryServiceCompanyList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Сервисные компании"')
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
