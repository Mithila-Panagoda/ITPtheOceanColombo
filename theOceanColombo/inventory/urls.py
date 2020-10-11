from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("loadaddsupplier/",views.loadaddsupplier),
    path("loadshowsupplier/", views.loadshowsupplier),
    path("addsupplierdb/",views.addsupplier),
    path("loadaddstock/",views.loadaddstock),
    path(r'addstockdb/',views.addstock),
    path("loadshowstock/",views.loadshowstock),
    path("loadeditsupplier/",views.loadeditsupplier),
    path("loadeditstock/", views.loadeditstock),
    path("updatestock/", views.updatestock),
    path("deletestock/", views.deletestock)

]