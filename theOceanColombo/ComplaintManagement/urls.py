from django.urls import path
from . import views
urlpatterns = [
    path("complaintFrontendLoad/",views.complaintFrontendLoad),
    path("complaintFrontend/", views.complaintFrontend),
    path("complaintReplytableLoad/", views.complaintReplytableLoad),
    path("complaintReplytable/", views.getcomplaintsdetails),
    path("complaintTypereplyLoad/", views.complaintTypereplyLoad),
    path("complaintTypereply/", views.complaintTypereply),
    path("complaintCheckReplyLoad/", views.complaintCheckReplyLoad),
    path("complaintCheckReply/", views.complaintCheckReply),
    path("complaintUpdateLoad/", views.complaintUpdateLoad),
    path("complaintUpdate/", views.complaintUpdate),
    path("complaintViewLoad/", views.complaintViewLoad),


]