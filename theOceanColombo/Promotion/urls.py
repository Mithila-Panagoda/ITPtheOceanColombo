from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("promoManagement/", views.Promomanagement),
    path("updatePromo/", views.Updatepromo),  
    path("updateEmp/", views.loadUpdatepromo)
]