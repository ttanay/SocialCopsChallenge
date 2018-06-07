from django.core.validators import MaxLengthValidator, MinLengthValidator
from django import forms
from .models import CustomUser

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.RegexField(regex=r'^\d{10}$', required=True)

    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'email', 'phone', 'password']
