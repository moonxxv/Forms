from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from . import models
from better_profanity import profanity


class CustomUserForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ['first_name', 'last_name', 'username']




class SmartphoneForm(forms.ModelForm):
    class Meta:
        model = models.Smartphone
        fields = '__all__'
        widgets = {
            'brand': forms.TextInput(attrs={
                'style': 'max-width: 300px;',
                'placeholder': 'Brand'
            }),
            'model': forms.TextInput(attrs={
                'style': 'max-width: 300px;',
                'placeholder': 'Model'
            }),
            'ram': forms.NumberInput(attrs={
                'style': 'max-width: 300px;',
                'placeholder': 'RAM (GB)'
            }),
            'capacity': forms.NumberInput(attrs={
                'style': 'max-width: 300px;',
                'placeholder': 'Capacity (GB)'
            })
        }        

    def clean_ram(self):
        ram = self.cleaned_data['ram']
        if ram <= 2:
            raise ValidationError('ОЗУ не может быть менее 2гб')
        return ram

    def clean_model(self):
        model = self.cleaned_data['model']
        if profanity.contains_profanity(model):
            raise forms.ValidationError("Your text contains profanity.")
        return model

    def clean_brand(self):
        brand = self.cleaned_data['brand']
        if profanity.contains_profanity(brand):
            raise forms.ValidationError("Your text contains profanity.")
        return brand