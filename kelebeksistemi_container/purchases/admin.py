from django.contrib import admin
from . models import LicenseKey, Purchase


# Register your models here.
admin.site.register(Purchase)
admin.site.register(LicenseKey)