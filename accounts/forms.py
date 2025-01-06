from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    email = forms.EmailField()


class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(max_length=15)
    password2 = forms.CharField(max_length=15)


class Editprofile(forms.ModelForm):
    idcode=forms.CharField(max_length=10)
    phone=forms.CharField(max_length=15)
    image=forms.ImageField()
    class Meta:
        model= User
        fields=["id_code","phone","image"]
