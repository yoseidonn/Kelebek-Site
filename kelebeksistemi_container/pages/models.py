from django.db import models


# Create your models here.
class Slide(models.Model):
    image = models.ImageField(upload_to="images/slide_thumbnails/%Y/%m/%d", verbose_name="Görsel", null=True)
    title = models.CharField(verbose_name="Başlık", max_length=32)
    content = models.CharField(verbose_name="İçerik", max_length=1024)
    date = models.DateTimeField(verbose_name="Eklenme tarihi.", auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.title} | {self.content} | {self.date.strftime('%d/%m/%Y - %H:%M:%S')}"

class Heading(models.Model):
    image = models.ImageField(upload_to="images/headings/thumbnails/%Y/%m/%d", verbose_name="Görsel", null=True)
    title = models.CharField(verbose_name="Başlık", max_length=32)
    content = models.CharField(verbose_name="İçerik", max_length=1024)
    date = models.DateTimeField(verbose_name="Eklenme tarihi.", auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.title} | {self.date.strftime('%d/%m/%Y - %H:%M:%S')}"
    
    
class Feature(models.Model):
    SIDES = (
        ("LEFT", "Sol"),
        ("RIGHT", "Sağ")
    )
    image = models.ImageField(upload_to="images/features/thumbnails/%Y/%m/%d", verbose_name="Görsel", null=True)
    title = models.CharField(verbose_name="Başlık", max_length=32)
    side_title = models.CharField(verbose_name="Yan başlık", max_length=32)
    content = models.CharField(verbose_name="İçerik", max_length=1024)
    side = models.CharField(choices=SIDES, default="LEFT", verbose_name='Metin yönü', max_length=32)
    date = models.DateTimeField(verbose_name="Eklenme tarihi.", auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.title} | {self.side} | {self.date.strftime('%d/%m/%Y - %H:%M:%S')}"
