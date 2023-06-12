from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    def __str__(self) -> str:
        return f"{self.username} | {self.first_name} {self.last_name}"