from django.urls import path
from . import views
urlpatterns = [
    path("complaintFrontendLoad/",views.complaintFrontendLoad),
    path("complaintFrontend/", views.complaintFrontend),
    path("complaintReplytableLoad/", views.complaintReplytableLoad),


]