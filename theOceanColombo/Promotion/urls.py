from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url("promoManagement/", views.Promomanagement),
    url("updatePromo/", views.Updatepromo),  
    url("updateEmp/", views.loadUpdatepromo)
]