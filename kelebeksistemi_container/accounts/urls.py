##################### ACCOUNTS URLS #####################

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('register/', views.user_register),
    path('dashboard/', views.user_dashboard),
    path('logout/', views.user_logout),   
]