from django import forms
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.Form):
    name = forms.CharField(label="Kullanıcı adı", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
    }))
    email = forms.EmailField(label="Parola", max_length=32, required=True, widget=forms.EmailInput(attrs={
        "class": "form-control",
    }))
    message = forms.CharField(label="Mesajınız", max_length=512, required=True, widget=forms.Textarea(attrs={
        "class": "form-control",
    }))
