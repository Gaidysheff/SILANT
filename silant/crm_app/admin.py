from django.contrib import admin
from .models import Breakdown, Claims, Machine, Maintenance, MaintenanceType, ModelDriveAxle, ModelEngine, ModelMachine, ModelSteeringAxle, ModelTransmission, RecoveryMethod, ServiceCompany


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelMachine', 'serialNumber', 'modelEngine', 'serialNumberEngine', 'modelTransmission', 'serialTransmission', 'modelDriveAxle',
                    'serialDriveAxle', 'modelSteeringAxle', 'serialSteeringAxle', 'deliveryContract', 'shipmentDate', 'consignee', 'deliveryAddress', 'additionalOptions', 'client', 'serviceCompany',)
    list_display_links = ('id', 'modelMachine', 'serialNumber', 'modelEngine', 'serialNumberEngine', 'modelTransmission', 'serialTransmission', 'modelDriveAxle',
                          'serialDriveAxle', 'modelSteeringAxle', 'serialSteeringAxle', 'deliveryContract', 'shipmentDate', 'consignee', 'deliveryAddress', 'additionalOptions', 'client', 'serviceCompany',)
    search_fields = ('modelMachine', 'serialNumber', 'modelEngine', 'serialNumberEngine', 'modelTransmission', 'serialTransmission', 'modelDriveAxle', 'serialDriveAxle',
                     'modelSteeringAxle', 'serialSteeringAxle', 'deliveryContract', 'client', 'serviceCompany',)
    list_filter = ('modelMachine', 'modelEngine', 'modelTransmission',
                   'modelDriveAxle', 'modelSteeringAxle', 'consignee', 'serviceCompany',)
    
    fieldsets = (
        ('Машина', 
          {'classes': ('wide', 'extrapretty'), 'fields': ('modelMachine', 'serialNumber')}),
        ('Двигатель', 
          {'classes': ('wide', 'extrapretty'), 'fields': ('modelEngine', 'serialNumberEngine')}),
        ('Трансмиссия', 
          {'classes': ('wide', 'extrapretty'), 'fields': ('modelTransmission', 'serialTransmission')}),
        ('Ведущий мост', 
          {'classes': ('wide', 'extrapretty'), 'fields': ('modelDriveAxle', 'serialDriveAxle')}),
        ('Управляемый мост', 
          {'classes': ('wide', 'extrapretty'), 'fields': ('modelSteeringAxle', 'serialSteeringAxle')}),
        ('Договор и Отгрузка', 
          {'classes': ('wide', 'extrapretty'), 'fields': ('deliveryContract', 'shipmentDate')}),
        ('Грузополучатель', 
          {'classes': ('wide', 'extrapretty'), 'fields': ('consignee', 'deliveryAddress')}),
        ('Дополнительно', {'classes': ('wide', 'extrapretty'), 'fields': ('additionalOptions', 'client', 'serviceCompany')}),
        )



@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'maintenanceDate', 'operatingTime', 'workOrder',
                    'workOrderDate', 'executor', 'machine', 'serviceCompany',)
    list_display_links = ('id', 'type', 'maintenanceDate', 'operatingTime',
                          'workOrder', 'workOrderDate', 'executor', 'machine', 'serviceCompany',)
    search_fields = ('workOrder', 'executor', 'machine')
    list_filter = ('executor', 'machine', 'serviceCompany',)
    
    fieldsets = (
         ('ИНФОРМАЦИЯ О ТЕХНИЧЕСКОМ ОБСЛУЖИВАНИИ:', 
          {'classes': ('wide', 'extrapretty'), 'fields': ('type', 'maintenanceDate', 'operatingTime', 'workOrder',
                    'workOrderDate', 'executor')}),
         ('МАШИНА И СЕРВИСНАЯ КОМПАНИЯ:', 
          {'classes': ('wide', 'extrapretty'), 'fields': ('machine', 'serviceCompany')}),
        )
    



@admin.register(Claims)
class ClaimsAdmin(admin.ModelAdmin):
    list_display = ('id', 'breakdownDate', 'operatingTime', 'breakdownNode', 'breakdownDescription',
                    'recoveryMethod', 'usedSpareParts', 'recoverDate', 'downtime', 'machine', 'serviceCompany',)
    list_display_links = ('id', 'breakdownDate', 'operatingTime', 'breakdownNode', 'breakdownDescription',
                          'recoveryMethod', 'usedSpareParts', 'recoverDate', 'downtime', 'machine', 'serviceCompany',)
    search_fields = ('breakdownNode', 'breakdownDescription',
                     'recoveryMethod', 'usedSpareParts', 'machine', 'serviceCompany')
    list_filter = ('machine', 'serviceCompany',)

    fieldsets = (
         ('ОТКАЗ / НЕИСПРАВНОСТЬ:', 
          {'classes': ('wide', 'extrapretty'), 'fields': ('breakdownDate', 'operatingTime', 'breakdownNode', 'breakdownDescription')}),
         ('ВОССТАНОВЛЕНИЕ:', 
          {'classes': ('wide', 'extrapretty'), 'fields': ('recoveryMethod', 'usedSpareParts', 'recoverDate', 'downtime')}),
         ('МАШИНА И СЕРВИСНАЯ КОМПАНИЯ:', 
          {'classes': ('wide', 'extrapretty'), 'fields': ('machine', 'serviceCompany')}),
        )


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
