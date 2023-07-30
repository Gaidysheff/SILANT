from rest_framework import serializers
from rest_framework_serializer_field_permissions import fields
from rest_framework_serializer_field_permissions.permissions import IsAuthenticated
from rest_framework_serializer_field_permissions.serializers import FieldPermissionSerializerMixin

from .models import *


class MachineSerializerAnyUser(FieldPermissionSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Machine
        fields = '__all__'

    deliveryContract = fields.CharField(
        permission_classes=(IsAuthenticated(), ))
    shipmentDate = fields.DateField(permission_classes=(IsAuthenticated(), ))
    consignee = fields.CharField(permission_classes=(IsAuthenticated(), ))
    deliveryAddress = fields.CharField(
        permission_classes=(IsAuthenticated(), ))
    additionalOptions = fields.CharField(
        permission_classes=(IsAuthenticated(), ))
    client = fields.CharField(permission_classes=(IsAuthenticated(), ))
    serviceCompany = fields.CharField(
        permission_classes=(IsAuthenticated(), ))


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'


class ClaimsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claims
        fields = '__all__'


# ======================== DIRECTORIES ========================

class DirectoryModelMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelMachine
        fields = '__all__'


class DirectoryModelEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelEngine
        fields = '__all__'


class DirectoryModelTransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTransmission
        fields = '__all__'


class DirectoryModelDriveAxleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelDriveAxle
        fields = '__all__'


class DirectoryModelSteeringAxleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelSteeringAxle
        fields = '__all__'


class DirectoryMaintenanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceType
        fields = '__all__'


class DirectoryBreakdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breakdown
        fields = '__all__'


class DirectoryRecoveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecoveryMethod
        fields = '__all__'


class DirectoryServiceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCompany
        fields = '__all__'
