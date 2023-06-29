from django_filters import FilterSet
from .models import Claims, Machine, Maintenance


class MachineFilter(FilterSet):
    class Meta:
        model = Machine
        fields = {
            'modelMachine': ['icontains'],
            'modelEngine': ['icontains'],
            'modelTransmission': ['icontains'],
            'modelDriveAxle': ['icontains'],
            'modelSteeringAxle': ['icontains'],
        }


class MaintenanceFilter(FilterSet):
    class Meta:
        model = Maintenance
        fields = {
            'type': ['icontains'],
            'machine': ['icontains'],
            'serviceCompany': ['icontains'],
        }


class ClaimsFilter(FilterSet):
    class Meta:
        model = Claims
        fields = {
            'breakdownNode': ['icontains'],
            'recoveryMethod': ['icontains'],
            'serviceCompany': ['icontains'],
        }
