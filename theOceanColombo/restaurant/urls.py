from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #front end page navigation
    path("loadtableselection/",views.loadTableSelection),
    path("loadrestauranttype/",views.loadRestaurantTypeSelection),
    path("bookingtableselection/",views.addBooking),
    path("bookingmealselection/",views.loadmealselection),
    path("bookingaddmealtocart/",views.addMealToCart),
    path("bookingbeverageselection/",views.loadBeverageSelection),
    path("bookingaddbeveragetocart/",views.addDrinkToCart),
    #Table paths
    path("loadalltable/",views.loadTableMngt),
    path("loadfreetable/",views.loadFreeTables),
    path("loadbookedtable/",views.loadBookedTables),
    path("loadupdatetable/",views.loadupdateTables),
    path("loadaddtable/",views.loadAddTable),
    path("updatetable/",views.UpdateTables),
    path("deletetable/",views.deleteTable),
    path("addtable/",views.addTables),
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