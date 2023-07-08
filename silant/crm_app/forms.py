from django import forms

# from django.utils.translation import gettext_lazy as _

from .models import *
import datetime


class AddMachineForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modelMachine'].empty_label = 'не выбрано'
        self.fields['modelEngine'].empty_label = 'не выбрано'
        self.fields['modelTransmission'].empty_label = 'не выбрано'
        self.fields['modelDriveAxle'].empty_label = 'не выбрано'
        self.fields['modelSteeringAxle'].empty_label = 'не выбрано'
        self.fields['client'].empty_label = 'не выбрано'
        self.fields['serviceCompany'].empty_label = 'не выбрано'
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
        self.fields['type'].empty_label = 'не выбрано'
        self.fields['machine'].empty_label = 'не выбрано'
        self.fields['client'].empty_label = 'не выбрано'
        self.fields['serviceCompany'].empty_label = 'не выбрано'
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
        self.fields['breakdownNode'].empty_label = 'не выбрано'
        self.fields['recoveryMethod'].empty_label = 'не выбрано'
        self.fields['machine'].empty_label = 'не выбрано'
        self.fields['client'].empty_label = 'не выбрано'
        self.fields['serviceCompany'].empty_label = 'не выбрано'
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
