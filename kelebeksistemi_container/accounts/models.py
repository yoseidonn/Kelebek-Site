from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    ROLES = (
        ('Admin', 'Yönetici'),
        ('Developer', 'Geliştirici'),
        ('User', 'Kullanıcı')
    )
    VERIFICATION_STATUSES = (
        ('Nonverified', 'Onaylanmamış'),
        ('Verified', 'Onaylanmış')
    )
    
    profile_photo = models.ImageField(upload_to="images/accounts/profile_photos/%Y/%m/%d", verbose_name="Profil fotoğrafı", null=True, blank=True, default='images/accounts/profile_photos/logo.png')
    bio = models.CharField(verbose_name="Biyografi", blank=True)
    role = models.CharField(choices=ROLES, default='User', blank=True)
    is_email_verified = models.CharField(choices=VERIFICATION_STATUSES, default='Nonverified')

    def __str__(self) -> str:
        return f"{self.username} | {self.first_name} {self.last_name}"
