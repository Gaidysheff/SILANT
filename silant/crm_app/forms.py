from django import forms

from django.utils.translation import gettext_lazy as _

from .models import *
import datetime


class AddMachineForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modelMachine'].empty_label = 'модель не выбрана'
        self.fields['modelEngine'].empty_label = 'модель не выбрана'
        self.fields['modelTransmission'].empty_label = 'модель не выбрана'
        self.fields['modelDriveAxle'].empty_label = 'модель не выбрана'
        self.fields['modelSteeringAxle'].empty_label = 'модель не выбрана'
        self.fields['client'].empty_label = 'клиент не выбран'
        self.fields['serviceCompany'].empty_label = 'компания не выбрана'
        self.shipmentDate = forms.DateField(initial=datetime.date.today)
        self.fields['shipmentDate'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'yyyy-mm-dd (DOB)',
            }
        )

    class Meta:
        model = Machine
        fields = '__all__'


class AddMaintenanceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = 'вид ТО не выбран'
        self.fields['machine'].empty_label = 'модель не выбрана'
        self.fields['client'].empty_label = 'клиент не выбран'
        self.fields['serviceCompany'].empty_label = 'компания не выбрана'
        self.maintenanceDate = forms.DateField(initial=datetime.date.today)
        self.fields['maintenanceDate'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'yyyy-mm-dd (DOB)',
            }
        )
        self.workOrderDate = forms.DateField(initial=datetime.date.today)
        self.fields['workOrderDate'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'yyyy-mm-dd (DOB)',
            }
        )
        self.fields['operatingTime'].initial = 0
        self.operatingTime = forms.FloatField(min_value=0,
                                              error_messages={'min_value': 'Наработка не может быть меньше нуля!'})

    class Meta:
        model = Maintenance
        fields = '__all__'


class AddClaimForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['breakdownNode'].empty_label = 'узел не выбран'
        self.fields['recoveryMethod'].empty_label = 'способ не выбран'
        self.fields['machine'].empty_label = 'модель не выбрана'
        self.fields['client'].empty_label = 'клиент не выбран'
        self.fields['serviceCompany'].empty_label = 'компания не выбрана'
        self.breakdownDate = forms.DateField(initial=datetime.date.today)
        self.fields['breakdownDate'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'yyyy-mm-dd (DOB)',
            }
        )
        self.recoverDate = forms.DateField(initial=datetime.date.today)
        self.fields['recoverDate'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'yyyy-mm-dd (DOB)',
            }
        )
        self.fields['operatingTime'].initial = 0
        self.operatingTime = forms.FloatField(min_value=0,
                                              error_messages={'min_value': 'Наработка не может быть меньше нуля!'})

    class Meta:
        model = Claims
        fields = '__all__'
