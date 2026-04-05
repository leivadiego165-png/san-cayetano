from django.contrib import admin
from django.urls import path
from facturacion import views

urlpatterns = [
    path('', views.dashboard),
]
