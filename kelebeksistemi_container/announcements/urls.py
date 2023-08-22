##################### ANNOUNCEMENTS URLS #####################

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.announcements, name="announcements"),
    path('<int:announcement_id>/', views.announcement, name="announcement"),
]