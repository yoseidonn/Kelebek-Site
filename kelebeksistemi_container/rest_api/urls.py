##################### REST API URLS #####################

from django.contrib import admin
from django.urls import path, include
from .views import ValidateView, test_view

urlpatterns = [
    path('', test_view),
    path('validate/<str:dsn>/<str:key>/', ValidateView.as_view()),
]