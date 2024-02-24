from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password")
