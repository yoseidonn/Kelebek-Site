from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı adı", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
    }))
    password = forms.CharField(label="Parola", max_length=32, required=True, widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))
    

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Ad", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "autofocus": True,
    }))
    last_name = forms.CharField(label="Soyad", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
    }))
    username = forms.CharField(label="Kullanıcı adı", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
    }))
    email = forms.CharField(label="E-Posta", max_length=32, required=True, widget=forms.EmailInput(attrs={
        "class": "form-control",
    }))
    password1 = forms.CharField(label="Parola", max_length=32, required=True, widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))
    password2 = forms.CharField(label="Parola onay", max_length=32, required=True, widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))
    
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]