import django_filters
# from django_filters import FilterSet
from .models import Claims, Machine, Maintenance


class MachineFilter(django_filters.FilterSet):
    modelMachine__name = django_filters.CharFilter(lookup_expr='icontains')
    modelEngine__name = django_filters.CharFilter(lookup_expr='icontains')
    modelTransmission__name = django_filters.CharFilter(
        lookup_expr='icontains')
    modelDriveAxle__name = django_filters.CharFilter(lookup_expr='icontains')
    modelSteeringAxle__name = django_filters.CharFilter(
        lookup_expr='icontains')

    class Meta:
        model = Machine
        fields = ['modelMachine', 'modelEngine',
                  'modelTransmission', 'modelDriveAxle', 'modelSteeringAxle']


class MaintenanceFilter(django_filters.FilterSet):
    type__name = django_filters.CharFilter(lookup_expr='icontains')
    machine__name = django_filters.CharFilter(lookup_expr='icontains')
    serviceCompany__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Maintenance
        fields = ['type', 'machine', 'serviceCompany']


class ClaimsFilter(django_filters.FilterSet):
    breakdownNode__name = django_filters.CharFilter(lookup_expr='icontains')
    recoveryMethod__name = django_filters.CharFilter(lookup_expr='icontains')
    serviceCompany__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Claims
        fields = ['breakdownNode', 'recoveryMethod', 'serviceCompany']
