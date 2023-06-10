from django.db import models
from django.contrib.auth.models import User


class Machine(models.Model):
    modelMachine = models.ForeignKey(
        'ModelMachine', on_delete=models.CASCADE, related_name='modelMachines', verbose_name='Модель техники')
    serialNumber = models.CharField(max_length=255, verbose_name='Зав. № машины')
    modelEngine = models.ForeignKey(
        'ModelEngine', on_delete=models.CASCADE, related_name='modelEngines', verbose_name='Модель двигателя')
    serialNumberEngine = models.CharField(max_length=255, verbose_name='Зав. № двигателя')
    modelTransmission = models.ForeignKey(
        'ModelTransmission', on_delete=models.CASCADE, related_name='modelTransmissions', verbose_name='Модель трансмиссии')
    serialTransmission = models.CharField(max_length=255, verbose_name='Зав. № трансмиссии')
    modelDriveAxle = models.ForeignKey(
        'ModelDriveAxle', on_delete=models.CASCADE, related_name='modelDriveAxles', verbose_name='Модель ведущего моста')
    serialDriveAxle = models.CharField(max_length=255, verbose_name='Зав. № ведущего моста')
    modelSteeringAxle = models.ForeignKey(
        'ModelSteeringAxle', on_delete=models.CASCADE, related_name='modelSteeringAxles', verbose_name='Модель управляемого моста')
    serialSteeringAxle = models.CharField(max_length=255, verbose_name='Зав. № управляемого моста')
    deliveryContract = models.CharField(max_length=255, verbose_name='Договор поставки №, дата')
    shipmentDate = models.DateField(verbose_name='Дата отгрузки с завода')
    consignee = models.CharField(max_length=255, verbose_name='Грузополучатель (конечный потребитель)')
    deliveryAddress = models.CharField(max_length=255, verbose_name='Адрес поставки (эксплуатации)')
    additionalOptions = models.TextField(
        default='Комплектация не указана', verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='clients', verbose_name='Клиент')
    serviceCompany = models.ManyToManyField(
        'ServiceCompany', verbose_name='Сервисная компания')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'МАШИНЫ'

    def __str__(self):
        return self.modelMachine


class Maintenance(models.Model):
    type = models.ForeignKey(
        'MaintenanceType', on_delete=models.CASCADE, related_name='maintenanceTypes', verbose_name='Вид ТО')
    maintenanceDate = models.DateField(verbose_name='Дата проведения ТО')
    operatingTime = models.IntegerField(verbose_name='Наработка, м/час')
    workOrder = models.CharField(max_length=255, verbose_name='№ заказ-наряда')
    workOrderDate = models.DateField(verbose_name='Дата заказ-наряда')
    executor = models.CharField(max_length=255, verbose_name='Организация, проводившая ТО')
    machine = models.ForeignKey(
        'ModelMachine', on_delete=models.CASCADE, verbose_name='Машина')
    serviceCompany = models.ManyToManyField(
        'ServiceCompany', verbose_name='Сервисная компания')
    
    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'ТЕХНИЧЕСКОЕ ОБСЛУЖИВАНИЕ'

    def __str__(self):
        return self.type


class Claims(models.Model):
    breakdownDate = models.DateField(verbose_name='Дата отказа')
    operatingTime = models.IntegerField(verbose_name='Наработка, м/час')
    breakdownNode = models.ForeignKey(
        'Breakdown', on_delete=models.CASCADE, related_name='breakdowns', verbose_name='Узел отказа')
    breakdownDescription = models.TextField(verbose_name='Описание отказа')
    recoveryMethod = models.ForeignKey(
        'RecoveryMethod', on_delete=models.CASCADE, related_name='recoveryMethods', verbose_name='Способ восстановления')
    usedSpareParts = models.TextField(verbose_name='Используемые запасные части')
    recoverDate = models.DateField(verbose_name='Дата восстановления')
    downtime = models.IntegerField(verbose_name='Время простоя техники')
    machine = models.ForeignKey(
        'ModelMachine', on_delete=models.CASCADE, verbose_name='Mашина')
    serviceCompany = models.ManyToManyField(
        'ServiceCompany', verbose_name='Cервисная компания')
    
    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'РЕКЛАМАЦИИ'

    def __str__(self):
        return self.machine

# =============================== Reference Tables =============================

class ModelMachine(models.Model):
    name = models.CharField(max_length=255, verbose_name='Модель')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = '_СПРАВОЧНИК_Модели техники'

    def __str__(self):
        return self.name


class ModelEngine(models.Model):
    name = models.CharField(max_length=255, verbose_name='Модель')
    description = models.TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = '_СПРАВОЧНИК_Модели двигателя'

    def __str__(self):
        return self.name


class ModelTransmission(models.Model):
    name = models.CharField(max_length=255, verbose_name='Модель')
    description = models.TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = '_СПРАВОЧНИК_Модели трансмиссии'

    def __str__(self):
        return self.name


class ModelDriveAxle(models.Model):
    name = models.CharField(max_length=255, verbose_name='Модель')
    description = models.TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = '_СПРАВОЧНИК_Модели ведущего моста'

    def __str__(self):
        return self.name


class ModelSteeringAxle(models.Model):
    name = models.CharField(max_length=255, verbose_name='Модель')
    description = models.TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = '_СПРАВОЧНИК_Модели управляемого моста'

    def __str__(self):
        return self.name


class MaintenanceType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Вид Технического Обслуживания'
        verbose_name_plural = '_СПРАВОЧНИК_Виды Технического Обслуживания'

    def __str__(self):
        return self.name


class Breakdown(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = '_СПРАВОЧНИК_Узлы отказа'

    def __str__(self):
        return self.name


class RecoveryMethod(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = '_СПРАВОЧНИК_Способы восстановления'

    def __str__(self):
        return self.name


class ServiceCompany(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = '_СПРАВОЧНИК_Сервисные компании'

    def __str__(self):
        return self.name