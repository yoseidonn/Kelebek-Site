from django.contrib import admin
from django import forms
from . models import LicenseKey, Purchase

# Purchases
class LicenseKeyInline(admin.TabularInline):
    model = LicenseKey
    extra = 0  # Set this to control the number of empty license key forms displayed

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    inlines = [LicenseKeyInline]
    

# LicenseKeys
admin.site.register(LicenseKey)