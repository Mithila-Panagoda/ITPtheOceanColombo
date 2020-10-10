from django.urls import path
from . import views

urlpatterns = [
        path("ExaddExpensesLoad/", views.ExaddExpensesLoad),
        path("ExaddExpenses/", views.ExaddExpenses),
        path("ExpenseslistLoad/", views.ExpenseslistLoad),
        path("Expenseslist/", views.Expenseslist),
        path("ExaddRevenueLoad/", views.ExaddRevenueLoad),
        path("ExaddRevenue/", views.ExaddRevenue),
        path("ExRevenueListLoad/", views.ExRevenueListLoad),
        path("ExRevenueList/", views.ExRevenueList),
        path("ExaddCapitalLoad/", views.ExaddCapitalLoad),
        path("ExaddCapital/", views.ExaddCapital),
        path("ExViewCapitalLoad/", views.ExViewCapitalLoad),
        path("ExViewCapital/", views.ExViewCapital),
        path("ExupdateTransacktionLoad/", views.ExupdateTransacktionLoad),
        path("ExupdateTransacktion/", views.ExupdateTransacktion),
        path("ExledgersLoad/", views. ExledgersLoad),
        path("Exledgers/", views. Exledgers),
        path("ExViewledgersLoad/", views. ExViewledgersLoad),
        path("ExpensesReportsLoad/", views.ExpensesReportsLoad),
        path("ExpensesReports/", views.ExpensesReports),
        path("ExReportsDisplayLoad/", views.ExReportsDisplayLoad),
        path("ExReportsDisplay/", views.ExReportsDisplay),


]