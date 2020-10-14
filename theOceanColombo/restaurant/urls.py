from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #Beverages paths
    path("beveragehome/",views.loadBeverageMngt),
    path("loaddrink/",views.loadadddrink),
    path("addDrink/",views.adddrink),
    path("loadUpdateBeverage/",views.loadupdatebeverage),
    path("updatebeverage/",views.updatebeverage),
    path("deletebeverage/",views.deleteBeverage),
    #-------------------------------------------------------------
    #meals
    path("mealhome/",views.loadmealmngt),
    path("loadupdatemeal/",views.loadUpdatemeal),
    path("updatemeal/",views.updateMeal),
    path("loadaddmeal/",views.loadAddMeal),
    path("addmeal/", views.addMeal),
    path("deletemeal/",views.deleteMeal),
    path("addDrink/",views.adddrink),
]