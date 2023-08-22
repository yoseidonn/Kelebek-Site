from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı adı", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "autofocus": True,
        "placeholder": "Kullanıcı adı",
    }))
    password = forms.CharField(label="Parola", max_length=32, required=True, widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Parola",
    }))
    
    class Meta:
        model = CustomUser
        fields = ["username", "password1"]

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Ad", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "autofocus": True,
        "placeholder": "Ad",
    }))
    last_name = forms.CharField(label="Soyad", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Soyad",
    }))
    username = forms.CharField(label="Kullanıcı adı", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Kullanıcı adı",
    }))
    email = forms.CharField(label="E-Posta", max_length=32, required=True, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "E-Posta",
    }))
    password1 = forms.CharField(label="Parola", max_length=32, required=True, widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Parola",
    }))
    password2 = forms.CharField(label="Parola onay", max_length=32, required=True, widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Parola onay",
    }))
    
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
        
    
class EditForm(UserChangeForm):
    profile_photo = forms.ImageField(label="Profil fotoğrafı", required=False, widget=forms.FileInput(attrs={
        "class": "form-control",
    }))
    first_name = forms.CharField(label="Ad", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Ad",
    }))
    last_name = forms.CharField(label="Soyad", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Soyad",
    }))
    email = forms.CharField(label="E-Posta", max_length=32, required=True, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "E-Posta",
    }))
    bio = forms.CharField(label="Biyografi", required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Biyografi",
    }))

    class Meta:
        model = CustomUser
        fields = ["profile_photo", "first_name", "last_name", "email", "bio"]