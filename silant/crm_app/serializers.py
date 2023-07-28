from rest_framework import serializers

from .models import Machine, Maintenance, Claims


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
