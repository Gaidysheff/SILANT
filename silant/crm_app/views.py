from typing import Any

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView

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

    if request.user.is_staff == True:

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

    else:
        return redirect('forbidden')


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

# =========================== CRUD ===========================


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
        'title': "Выбранная машина"
        # 'title': f"Выбранная машина | зав. № = {machine.serialNumber}"
    }
    return render(request, 'crm_app/machine.html', context=context)


@login_required()
def show_maintenance(request, maintenance_id):
    maintenance = get_object_or_404(Maintenance, pk=maintenance_id)

    context = {
        'maintenance': maintenance,
        'machine_table_titles': machine_table_titles,
        # 'machine_table_subtitles': machine_table_subtitles,
        'menu': menu,
        'title': "Выбранное Техническое Обслуживание"
    }
    return render(request, 'crm_app/crud_read_maintenance.html', context=context)


@login_required()
def show_claim(request, claim_id):
    claim = get_object_or_404(Claims, pk=claim_id)

    context = {
        'claim': claim,
        'machine_table_titles': machine_table_titles,
        # 'machine_table_subtitles': machine_table_subtitles,
        'menu': menu,
        'title': "Выбранная Рекламация"
    }
    return render(request, 'crm_app/crud_read_claim.html', context=context)

# --------------------------------------------------------------


class AddMachine(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = 'crm_app.add_machine'
    form_class = AddMachineForm
    template_name = 'crm_app/crud_add_machine.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление Машины")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class AddMaintenance(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = 'crm_app.add_maintenance'
    form_class = AddMaintenanceForm
    template_name = 'crm_app/crud_add_maintenance.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление ТО")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class AddClaim(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = 'crm_app.add_claims'
    form_class = AddClaimForm
    template_name = 'crm_app/crud_add_claim.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление Рекламации")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())

# --------------------------------------------------------------


class UpdateMachine(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    permission_required = 'crm_app.change_machine'
    form_class = AddMachineForm
    model = Machine
    template_name = 'crm_app/crud_update_machine.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обновление Машины")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class UpdateMaintenance(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    permission_required = 'crm_app.change_maintenance'
    form_class = AddMaintenanceForm
    model = Maintenance
    template_name = 'crm_app/crud_update_maintenance.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обновление ТО")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class UpdateClaim(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    permission_required = 'crm_app.change_claims'
    form_class = AddClaimForm
    model = Claims
    template_name = 'crm_app/crud_update_claim.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обновление Рекламации")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())

# --------------------------------------------------------------


class DeleteMachine(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    permission_required = 'crm_app.delete_machine'
    model = Machine
    template_name = 'crm_app/crud_delete_machine.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удаление записи о машине")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class DeleteMaintenance(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    permission_required = 'crm_app.delete_maintenance'
    model = Maintenance
    template_name = 'crm_app/crud_delete_maintenance.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удаление записи о ТО машины")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class DeleteClaim(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    permission_required = 'crm_app.delete_claims'
    model = Claims
    template_name = 'crm_app/crud_delete_claim.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удаление записи о Рекламации на машину")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


# ======================== DIRECTORIES ========================


class AllDirectories(LoginRequiredMixin, DataMixin, TemplateView):
    template_name = 'crm_app/allDirectories.html'

    def get_context_data(self, **kwargs):
        context = super(AllDirectories, self).get_context_data(**kwargs)
        context['modelMachine'] = ModelMachine.objects.order_by('name')
        context['modelEngine'] = ModelEngine.objects.order_by('name')
        context['modelTransmission'] = ModelTransmission.objects.order_by(
            'name')
        context['modelDriveAxle'] = ModelDriveAxle.objects.order_by('name')
        context['modelSteeringAxle'] = ModelSteeringAxle.objects.order_by(
            'name')
        context['maintenanceType'] = MaintenanceType.objects.order_by('name')
        context['breakdown'] = Breakdown.objects.order_by('name')
        context['recoveryMethod'] = RecoveryMethod.objects.order_by('name')
        context['serviceCompany'] = ServiceCompany.objects.order_by('name')
        context['menu'] = menu
        context['title'] = "СПРАВОЧНИКИ"
        return context


# ---------------------------------------------------------------

class DirectoryModelMachine(LoginRequiredMixin, DataMixin, DetailView):
    model = ModelMachine
    template_name = 'crm_app/directories/directoryModelMachine.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модель Вашей машины"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryModelMachineList(LoginRequiredMixin, DataMixin, ListView):
    queryset = ModelMachine.objects.order_by('name')
    template_name = 'crm_app/directories/directoryModelMachineList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='"Модели техники"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryModelEngine(LoginRequiredMixin, DataMixin, DetailView):
    model = ModelEngine
    template_name = 'crm_app/directories/directoryModelEngine.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модель двигателя"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryModelEngineList(LoginRequiredMixin, DataMixin, ListView):
    queryset = ModelEngine.objects.order_by('name')
    template_name = 'crm_app/directories/directoryModelEngineList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модели двигателей"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryModelTransmission(LoginRequiredMixin, DataMixin, DetailView):
    model = ModelTransmission
    template_name = 'crm_app/directories/directoryModelTransmission.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модель трансмиссии"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryModelTransmissionList(LoginRequiredMixin, DataMixin, ListView):
    queryset = ModelTransmission.objects.order_by('name')
    template_name = 'crm_app/directories/directoryModelTransmissionList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модели трансмиссий"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryModelDriveAxle(LoginRequiredMixin, DataMixin, DetailView):
    model = ModelDriveAxle
    template_name = 'crm_app/directories/directoryModelDriveAxle.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модель ведущего моста"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryModelDriveAxleList(LoginRequiredMixin, DataMixin, ListView):
    queryset = ModelDriveAxle.objects.order_by('name')
    template_name = 'crm_app/directories/directoryModelDriveAxleList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модели ведущего моста"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryModelSteeringAxle(LoginRequiredMixin, DataMixin, DetailView):
    model = ModelSteeringAxle
    template_name = 'crm_app/directories/directoryModelSteeringAxle.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модель управляемого моста"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryModelSteeringAxleList(LoginRequiredMixin, DataMixin, ListView):
    queryset = ModelSteeringAxle.objects.order_by('name')
    template_name = 'crm_app/directories/directoryModelSteeringAxleList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Модели управляемого моста"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryMaintenanceType(LoginRequiredMixin, DataMixin, DetailView):
    model = MaintenanceType
    template_name = 'crm_app/directories/directoryMaintenanceType.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Вид Технического Обслуживания"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryMaintenanceTypeList(LoginRequiredMixin, DataMixin, ListView):
    queryset = MaintenanceType.objects.order_by('name')
    template_name = 'crm_app/directories/directoryMaintenanceTypeList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Виды Технического Обслуживания"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryBreakdown(LoginRequiredMixin, DataMixin, DetailView):
    model = Breakdown
    template_name = 'crm_app/directories/directoryBreakdown.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Узел отказа"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryBreakdownList(LoginRequiredMixin, DataMixin, ListView):
    queryset = Breakdown.objects.order_by('name')
    template_name = 'crm_app/directories/directoryBreakdownList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='"Узлы отказа"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryRecoveryMethod(LoginRequiredMixin, DataMixin, DetailView):
    model = RecoveryMethod
    template_name = 'crm_app/directories/directoryRecoveryMethod.html'
    pk_url_kwarg = 'modelMachine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Способ восстановления"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryRecoveryMethodList(LoginRequiredMixin, DataMixin, ListView):
    queryset = RecoveryMethod.objects.order_by('name')
    template_name = 'crm_app/directories/directoryRecoveryMethodList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Способы восстановления"')
        return dict(list(context.items()) + list(c_def.items()))

# ---------------------------------------------------------------


class DirectoryServiceCompany(LoginRequiredMixin, DataMixin, DetailView):
    model = ServiceCompany
    template_name = 'crm_app/directories/directoryServiceCompany.html'
    pk_url_kwarg = 'machine_pk'
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Сервисная компания"')
        return dict(list(context.items()) + list(c_def.items()))


class DirectoryServiceCompanyList(LoginRequiredMixin, DataMixin, ListView):
    queryset = ServiceCompany.objects.order_by('name')
    template_name = 'crm_app/directories/directoryServiceCompanyList.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='"Сервисные компании"')
        return dict(list(context.items()) + list(c_def.items()))


# =================== CRUD for DIRECTORIES ===================

class AddModelMachine(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = 'crm_app.add_modelmachine'
    form_class = AddModelMachineForm
    template_name = 'crm_app/directories/directory_add_modelMachine.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление модели машины")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class AddModelEngine(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = 'crm_app.add_modelengine'
    form_class = AddModelEngineForm
    template_name = 'crm_app/directories/directory_add_modelEngine.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление модели двигателя")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class AddModelTransmission(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = 'crm_app.add_modeltransmission'
    form_class = AddModelTransmissionForm
    template_name = 'crm_app/directories/directory_add_modelTransmission.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление модели трансмиссии")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class AddModelDriveAxle(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = 'crm_app.add_modeldriveaxle'
    form_class = AddModelDriveAxleForm
    template_name = 'crm_app/directories/directory_add_modelDriveAxle.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление модели ведущего моста")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class AddModelSteeringAxle(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = 'crm_app.add_modelsteeringaxle'
    form_class = AddModelSteeringAxleForm
    template_name = 'crm_app/directories/directory_add_modelSteeringAxle.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавление модели управляемого моста")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class AddMaintenanceType(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = 'crm_app.add_maintenancetype'
    form_class = AddMaintenanceTypeForm
    template_name = 'crm_app/directories/directory_add_maintenanceType.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавление вида Технического Обслуживания")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class AddBreakdown(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = 'crm_app.add_breakdown'
    form_class = AddBreakdownForm
    template_name = 'crm_app/directories/directory_add_breakdown.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавление узла отказа")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class AddRecoveryMethod(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = 'crm_app.add_recoverymethod'
    form_class = AddRecoveryMethodForm
    template_name = 'crm_app/directories/directory_add_recoveryMethod.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавление способа восстановления")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class AddServiceCompany(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = 'crm_app.add_servicecompany'
    form_class = AddServiceCompanyForm
    template_name = 'crm_app/directories/directory_add_serviceCompany.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавление сервисной компании")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


# --------------------------------------------------------------


class UpdateModelMachine(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    permission_required = 'crm_app.change_modelmachine'
    form_class = AddModelMachineForm
    model = ModelMachine
    template_name = 'crm_app/directories/directory_update_modelMachine.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обновление модели машины")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class UpdateModelEngine(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    permission_required = 'crm_app.change_modelengine'
    form_class = AddModelEngineForm
    model = ModelEngine
    template_name = 'crm_app/directories/directory_update_modelEngine.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обновление модели двигателя")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class UpdateModelTransmission(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    permission_required = 'crm_app.change_modeltransmission'
    form_class = AddModelTransmissionForm
    model = ModelTransmission
    template_name = 'crm_app/directories/directory_update_modelTransmission.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обновление модели трансмиссии")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class UpdateModelDriveAxle(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    permission_required = 'crm_app.change_modeldriveaxle'
    form_class = AddModelDriveAxleForm
    model = ModelDriveAxle
    template_name = 'crm_app/directories/directory_update_modelDriveAxle.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обновление модели ведущего моста")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class UpdateModelSteeringAxle(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    permission_required = 'crm_app.change_modelsteeringaxle'
    form_class = AddModelSteeringAxleForm
    model = ModelSteeringAxle
    template_name = 'crm_app/directories/directory_update_modelSteeringAxle.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Обновление модели управляемого моста")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class UpdateMaintenanceType(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    permission_required = 'crm_app.change_maintenancetype'
    form_class = AddMaintenanceTypeForm
    model = MaintenanceType
    template_name = 'crm_app/directories/directory_update_maintenanceType.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Обновление вида Технического Обслуживания")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class UpdateBreakdown(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    permission_required = 'crm_app.change_breakdown'
    form_class = AddBreakdownForm
    model = Breakdown
    template_name = 'crm_app/directories/directory_update_breakdown.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Обновление узла отказа")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class UpdateRecoveryMethod(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    permission_required = 'crm_app.change_recoverymethod'
    form_class = AddRecoveryMethodForm
    model = RecoveryMethod
    template_name = 'crm_app/directories/directory_update_recoveryMethod.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Обновление способа восстановления")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class UpdateServiceCompany(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    permission_required = 'crm_app.change_servicecompany'
    form_class = AddServiceCompanyForm
    model = ServiceCompany
    template_name = 'crm_app/directories/directory_update_serviceCompany.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Обновление сервисной компании")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


# --------------------------------------------------------------


class DeleteModelMachine(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    permission_required = 'crm_app.delete_modelmachine'
    model = ModelMachine
    template_name = 'crm_app/directories/directory_delete_modelMachine.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удаление записи о модели машины")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class DeleteModelEngine(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    permission_required = 'crm_app.delete_modelengine'
    model = ModelEngine
    template_name = 'crm_app/directories/directory_delete_modelEngine.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удаление записи о модели двигателя")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class DeleteModelTransmission(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    permission_required = 'crm_app.delete_modeltransmission'
    model = ModelTransmission
    template_name = 'crm_app/directories/directory_delete_modelTransmission.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удаление записи о модели трансмиссии")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class DeleteModelDriveAxle(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    permission_required = 'crm_app.delete_modeldriveaxle'
    model = ModelDriveAxle
    template_name = 'crm_app/directories/directory_delete_modelDriveAxle.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удаление записи о модели ведущего моста")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class DeleteModelSteeringAxle(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    permission_required = 'crm_app.delete_modelsteeringaxle'
    model = ModelSteeringAxle
    template_name = 'crm_app/directories/directory_delete_modelSteeringAxle.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удаление записи о модели управляемого моста")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class DeleteMaintenanceType(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    permission_required = 'crm_app.delete_maintenancetype'
    model = MaintenanceType
    template_name = 'crm_app/directories/directory_delete_maintenanceType.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удаление записи о виде Технического Обслуживания")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class DeleteBreakdown(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    permission_required = 'crm_app.delete_breakdown'
    model = Breakdown
    template_name = 'crm_app/directories/directory_delete_breakdown.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удаление записи об узле отказа")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class DeleteRecoveryMethod(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    permission_required = 'crm_app.delete_recoverymethod'
    model = RecoveryMethod
    template_name = 'crm_app/directories/directory_delete_recoveryMethod.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удаление записи о способе восстановления")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


class DeleteServiceCompany(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    permission_required = 'crm_app.delete_servicecompany'
    model = ServiceCompany
    template_name = 'crm_app/directories/directory_delete_serviceCompany.html'
    success_url = reverse_lazy('index')
    redirect_field_name = reverse_lazy('forbidden')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удаление записи о сервисной компании")
        return dict(list(context.items()) + list(c_def.items()))

    def handle_no_permission(self):
        return redirect(self.get_redirect_field_name())


# ============================================================


def under_construction(request):
    return render(request, 'crm_app/under_construction.html', {'menu': menu, 'title': 'Страница в разработке'})


def about(request):
    return render(request, 'crm_app/about.html', {'menu': menu, 'title': 'О нас'})


def contact(request):
    return render(request, 'crm_app/under_construction.html', {'menu': menu, 'title': 'Страница в разработке'})


def forbidden(request):
    return render(request, 'crm_app/forbidden.html', {'menu': menu, 'title': '403 Запрещено'})
