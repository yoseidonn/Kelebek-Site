from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(label="Ad", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "label": "E-Posta",
        "placeholder": "Adınız",
        "autofocus": True,
    }))
    email = forms.EmailField(label="E-Posta", max_length=32, required=True, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "label": "E-Posta",
        "placeholder": "E-Posta adresiniz"
    }))
    title = forms.CharField(label="Başlık", max_length=32, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "label": "E-Posta",
        "placeholder": "Başlık"
    }))
    text = forms.CharField(label="Mesaj", max_length=512, required=True, widget=forms.Textarea(attrs={
        "class": "form-control",
        "label": "E-Posta",
        "placeholder": "Mesaj"
    }))
    
    class Meta:
        model = Contact
        fields = ["name", "email", "title", "text"]
