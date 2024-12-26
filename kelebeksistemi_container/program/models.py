from django.db import models
from accounts.models import CustomUser
    
    
# Create your models here.
class Purchase(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Satın alımı yapan kullanıcı.")
    purchase_date = models.DateTimeField(verbose_name="Satın alım tarihi.", auto_now_add=True)
    amount = models.DecimalField(verbose_name="Satın alım tutarı.", decimal_places=2, max_digits=8)
    
    def __str__(self):
        return f'"{self.user}" kullanıcısı tarafından "{self.purchase_date}" tarihinde yapılan satın alım.'


class LicenseKey(models.Model):
    KEY_TYPE = (
        ("STD", "Standart"),
        ("PRO", "Profesyonel")
    )
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, verbose_name="Satın alım:", null=True)
    key = models.CharField(verbose_name="Lisans anahtarı:", unique=True, max_length=128)
    key_type = models.CharField(choices=KEY_TYPE, verbose_name="Lisans tipi:", default="STD", max_length=32)
    disk_serial_number1 = models.BigIntegerField(verbose_name="DSN 1:", null=True, blank=True, help_text="Disk seri numarasi")
    disk_serial_number2 = models.BigIntegerField(verbose_name="DSN 2:", null=True, blank=True, help_text="Disk seri numarasi")
    end_date = models.DateField(verbose_name="Lisansın sona eriş tarihi:")
    
    def __str__(self):
        user = self.purchase.user
        name = f"{user.first_name} {user.last_name}"
        key_t = dict(self.KEY_TYPE).get(self.key_type)
        return f'"{name}" adlı kullanıcının "{key_t}" tipi "{self.key}" lisans anahtarı'