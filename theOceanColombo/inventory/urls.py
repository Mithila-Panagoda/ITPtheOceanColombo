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
    path("deletestock/", views.deletestock),
    path("updatesupplier/", views.updatesupplier),
    path("deletesupplier/", views.deletesupplier),
    path("loadpurchaseorder/", views.getlist_idsrep),
    path("addlist/",views.addlist),
    path("loadlisttable/",views.loadlisttable),
    path("deletelist/",views.deletelist),
    path("createlists/",views.getstockids),
    path("addlisttosupplier/",views.addlisttosupplier),
    path("getlist_idforrepo/",views.getlist_idforrepo),
    path("generaterepo/",views.generaterepo),
    path("loadbackendhomepage/",views.loadbackendhomepage)


]