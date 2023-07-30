import django_filters

from .models import Claims, Machine, Maintenance


class MachineFilter(django_filters.FilterSet):
    serialNumber = django_filters.CharFilter(
        lookup_expr='icontains')
    serialNumberEngine = django_filters.CharFilter(lookup_expr='icontains')
    serialTransmission = django_filters.CharFilter(
        lookup_expr='icontains')
    serialDriveAxle = django_filters.CharFilter(lookup_expr='icontains')
    serialSteeringAxle = django_filters.CharFilter(
        lookup_expr='icontains')

    class Meta:
        model = Machine
        fields = ['modelMachine', 'modelEngine',
                  'modelTransmission', 'modelDriveAxle', 'modelSteeringAxle']


class MaintenanceFilter(django_filters.FilterSet):
    executor = django_filters.CharFilter(lookup_expr='icontains')
    workOrder = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Maintenance
        fields = ['type', 'machine', 'serviceCompany']


class ClaimsFilter(django_filters.FilterSet):
    breakdownDescription = django_filters.CharFilter(lookup_expr='icontains')
    usedSpareParts = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Claims
        fields = ['breakdownNode', 'recoveryMethod', 'serviceCompany']
