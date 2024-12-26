from django.db import models

# Create your models here.
class Announcement(models.Model):
    image = models.ImageField(upload_to="images/announcements/thumbnails/%Y/%m/%d", verbose_name="Duyuru kapak fotoğrafı.", null=True)
    title = models.CharField(verbose_name="Duyuru başlığı.", max_length=64)
    date = models.DateTimeField(verbose_name="Duyuru tarihi.", auto_now=True)
    content = models.CharField(verbose_name="Duyuru içeriği", max_length=4096)
    
    def __str__(self) -> str:
        return f"{self.title} | {self.date.strftime('%d/%m/%Y - %H:%M:%S')}"