from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(verbose_name="Ad", blank=True, max_length=32)
    email = models.EmailField(verbose_name="E-Posta", blank=True)
    title = models.CharField(verbose_name="Başlık", blank=True, max_length=32)
    text = models.CharField(verbose_name="Mesaj", blank=True, max_length=256)
    date = models.DateTimeField(auto_now=True, verbose_name="Tarih")
    
    def __str__(self) -> str:
        return f"{self.name} | {self.title} | {self.date.strftime('%d/%m/%Y - %H:%M:%S')}"