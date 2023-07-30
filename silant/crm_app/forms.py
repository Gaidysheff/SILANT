import datetime

from django import forms

from .models import *


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


# ======================== DIRECTORIES ========================


class AddModelMachineForm(forms.ModelForm):
    class Meta:
        model = ModelMachine
        fields = ['name', 'description',]


class AddModelEngineForm(forms.ModelForm):
    class Meta:
        model = ModelEngine
        fields = ['name', 'description',]


class AddModelTransmissionForm(forms.ModelForm):
    class Meta:
        model = ModelTransmission
        fields = ['name', 'description',]


class AddModelDriveAxleForm(forms.ModelForm):
    class Meta:
        model = ModelDriveAxle
        fields = ['name', 'description',]


class AddModelSteeringAxleForm(forms.ModelForm):
    class Meta:
        model = ModelSteeringAxle
        fields = ['name', 'description',]


class AddMaintenanceTypeForm(forms.ModelForm):
    class Meta:
        model = MaintenanceType
        fields = ['name', 'description',]


class AddBreakdownForm(forms.ModelForm):
    class Meta:
        model = Breakdown
        fields = ['name', 'description',]


class AddRecoveryMethodForm(forms.ModelForm):
    class Meta:
        model = RecoveryMethod
        fields = ['name', 'description',]


class AddServiceCompanyForm(forms.ModelForm):
    class Meta:
        model = ServiceCompany
        fields = ['name', 'description',]
