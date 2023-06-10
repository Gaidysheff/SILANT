from django.db import models
from django.contrib.auth.models import User


class Machine(models.Model):
    modelMachine = models.ForeignKey(
        'ModelMachine', on_delete=models.CASCADE, related_name='modelMachines')
    serialNumber = models.CharField(max_length=255)
    modelEngine = models.ForeignKey(
        'ModelEngine', on_delete=models.CASCADE, related_name='modelEngines')
    serialNumberEngine = models.CharField(max_length=255)
    modelTransmission = models.ForeignKey(
        'ModelTransmission', on_delete=models.CASCADE, related_name='modelTransmissions')
    serialDriveAxle = models.CharField(max_length=255)
    modelDriveAxle = models.ForeignKey(
        'ModelDriveAxle', on_delete=models.CASCADE, related_name='modelDriveAxles')
    serialSteeringAxle = models.CharField(max_length=255)
    modelSteeringAxle = models.ForeignKey(
        'ModelSteeringAxle', on_delete=models.CASCADE, related_name='modelSteeringAxles')
    deliveryContract = models.CharField(max_length=255)
    shipmentDate = models.DateField()
    consignee = models.CharField(max_length=255)
    deliveryAddress = models.CharField(max_length=255)
    additionalOptions = models.TextField(
        default='Комплектация не указана')
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='clients')
    serviceCompany = models.ManyToManyField(
        'ServiceCompany')


class Maintenance(models.Model):
    type = models.ForeignKey(
        'MaintenanceType', on_delete=models.CASCADE, related_name='maintenanceTypes')
    maintenanceDate = models.DateField()
    operatingTime = models.IntegerField()
    workOrder = models.CharField(max_length=255)
    workOrderDate = models.DateField()
    executor = models.CharField(max_length=255)
    machine = models.ForeignKey(
        'ModelMachine', on_delete=models.CASCADE)
    serviceCompany = models.ManyToManyField(
        'ServiceCompany')


class Claims(models.Model):
    operatingTime = models.IntegerField()
    breakdownDate = models.DateField()
    breakdownNode = models.ForeignKey(
        'Breakdown', on_delete=models.CASCADE, related_name='breakdowns')
    breakdownDescription = models.TextField()
    recoveryMethod = models.ForeignKey(
        'RecoveryMethod', on_delete=models.CASCADE, related_name='recoveryMethods')
    usedSpareParts = models.TextField()
    recoverDate = models.DateField()
    downtime = models.IntegerField()
    machine = models.ForeignKey(
        'ModelMachine', on_delete=models.CASCADE)
    serviceCompany = models.ManyToManyField(
        'ServiceCompany')


class ModelMachine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class ModelEngine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class ModelTransmission(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class ModelDriveAxle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class ModelSteeringAxle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class MaintenanceType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Breakdown(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class RecoveryMethod(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class ServiceCompany(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
