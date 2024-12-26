##################### PROGRAM URLS #####################
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('introduction/', views.introduction, name="introduction"),
    path('download/', views.download, name="download"),
    path('downloads/', views.downloads, name="downloads"),
    path('downloads/<str:platform_name>', views.downloads_details, name="downloads_details"),
    path('fees/', views.fees, name="fees"),
    path('purchase-std/', views.purchase_std, name="purchase_std"),
    path('purchase-pro/', views.purchase_pro, name="purchase_pro"),
]
