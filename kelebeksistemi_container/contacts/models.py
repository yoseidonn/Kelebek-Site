from django.db import models

# Create your models here.
class Contact(models.Model):
    title = models.CharField(verbose_name="Mesaj başlığı")