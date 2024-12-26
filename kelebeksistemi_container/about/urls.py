##################### ABOUT URLS #####################

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('privacy-terms', views.privacy_terms, name="privacy_terms"),
    path('team/', views.team, name="team"),
    path('contact/', views.contact, name="contact"),
]