from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

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
                # 'class': 'form-control',
            }
        )

    class Meta:
        model = Machine
        fields = '__all__'

        # fields = ['author', 'categoryType', 'postCategory',
        #           'title', 'text', 'photo', 'rating', 'status']

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-input', 'size': 58}),
        #     'slug': forms.URLInput(attrs={'size': 58}),
        #     'text': forms.Textarea(attrs={'cols': 60, 'rows': 7}),
        # }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 200:
    #         raise ValidationError(
    #             'Длина превышает 200 символов')
    #     return title
