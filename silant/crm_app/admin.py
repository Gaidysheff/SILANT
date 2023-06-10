from django.contrib import admin
from .models import Breakdown, Claims, Machine, Maintenance, MaintenanceType, ModelDriveAxle, ModelEngine, ModelMachine, ModelSteeringAxle, ModelTransmission, RecoveryMethod, ServiceCompany


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelMachine', 'serialNumber', 'modelEngine', 'serialNumberEngine', 'modelTransmission', 'serialTransmission', 'modelDriveAxle',
                    'serialDriveAxle', 'modelSteeringAxle', 'serialSteeringAxle', 'deliveryContract', 'shipmentDate', 'consignee', 'deliveryAddress', 'additionalOptions', 'client')
    list_display_links = ('id', 'modelMachine', 'serialNumber', 'modelEngine', 'serialNumberEngine', 'modelTransmission', 'serialTransmission', 'modelDriveAxle',
                          'serialDriveAxle', 'modelSteeringAxle', 'serialSteeringAxle', 'deliveryContract', 'shipmentDate', 'consignee', 'deliveryAddress', 'additionalOptions', 'client')
    search_fields = ('modelMachine', 'serialNumber', 'modelEngine', 'serialNumberEngine', 'modelTransmission', 'serialTransmission', 'modelDriveAxle', 'serialDriveAxle',
                     'modelSteeringAxle', 'serialSteeringAxle', 'deliveryContract', 'client')


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'maintenanceDate', 'workOrder',
                    'workOrderDate', 'executor', 'machine')
    list_display_links = ('id', 'type', 'maintenanceDate',
                          'workOrder', 'workOrderDate', 'executor', 'machine')
    search_fields = ('workOrder', 'executor', 'machine')


@admin.register(Claims)
class ClaimsAdmin(admin.ModelAdmin):
    list_display = ('id', 'breakdownDate', 'operatingTime', 'breakdownNode', 'breakdownDescription',
                    'recoveryMethod', 'usedSpareParts', 'recoverDate', 'downtime', 'machine')
    list_display_links = ('id', 'breakdownDate', 'operatingTime', 'breakdownNode', 'breakdownDescription',
                          'recoveryMethod', 'usedSpareParts', 'recoverDate', 'downtime', 'machine')
    search_fields = ('breakdownNode', 'breakdownDescription',
                     'recoveryMethod', 'usedSpareParts', 'machine', 'serviceCompany')


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
