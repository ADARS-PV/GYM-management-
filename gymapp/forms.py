from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)
    height = forms.FloatField()
    weight = forms.FloatField()

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'height', 'weight', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
