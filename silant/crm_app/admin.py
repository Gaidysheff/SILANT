from django.contrib import admin
from .models import Breakdown, Claims, Machine, Maintenance, MaintenanceType, ModelDriveAxle, ModelEngine, ModelMachine, ModelSteeringAxle, ModelTransmission, RecoveryMethod, ServiceCompany


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    pass


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Claims)
class ClaimsAdmin(admin.ModelAdmin):
    pass


@admin.register(ModelMachine)
class ModelMachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')
    search_fields = ('name', 'description')


@admin.register(ModelEngine)
class ModelEngineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')
    search_fields = ('name', 'description')


@admin.register(ModelTransmission)
class ModelTransmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')
    search_fields = ('name', 'description')


@admin.register(ModelDriveAxle)
class ModelDriveAxleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')
    search_fields = ('name', 'description')


@admin.register(ModelSteeringAxle)
class ModelSteeringAxleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')
    search_fields = ('name', 'description')


@admin.register(MaintenanceType)
class MaintenanceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')
    search_fields = ('name', 'description')


@admin.register(Breakdown)
class BreakdownAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')
    search_fields = ('name', 'description')


@admin.register(RecoveryMethod)
class RecoveryMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')
    search_fields = ('name', 'description')


@admin.register(ServiceCompany)
class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')
    search_fields = ('name', 'description')
