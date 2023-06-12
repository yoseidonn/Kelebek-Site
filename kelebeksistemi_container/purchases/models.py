from django.db import models
from accounts.models import CustomUser


# Create your models here.
class LicenseKey(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Anahtarın sahibi.")
    key = models.CharField(verbose_name="Lisans anahtarı.")
    end_date = models.DateField(verbose_name="Lisansın sona eriş tarihi.")
    
    def __str__(self):
        return self.key
    
    
class Purchase(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Satın alımı yapan kullanıcı.")
    key = models.ForeignKey(LicenseKey, verbose_name="Satılan lisans anahtarı.", on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(verbose_name="Satın alım tarihi.", auto_now_add=True)
    amount = models.DecimalField(verbose_name="Satın alım tutarı.", decimal_places=2, max_digits=8)
    
    def __str__(self):
        return f'"{self.user}" kullanıcısı tarafından "{self.purchase_date}" tarihinde yapılan satın alım.'
    
