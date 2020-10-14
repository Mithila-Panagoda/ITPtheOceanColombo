from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("customerlogin/", views.custloign),
    # path("logout/", views.logout),
    path("addCustomer/", views.custreg),
    path("customerRegistration/", views.loadcustreg),
    path("userDetail/", views.userdetails),
    path("userDet/",views.loaduserdetails),
    path("deleteCust/",views.deleteCus)
    
]