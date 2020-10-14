from django.urls import path
from . import views

urlpatterns = [
        path("ExaddExpensesLoad/", views.ExaddExpensesLoad),
        path("ExaddExpenses/", views.ExaddExpenses),

        path("ExpenseslistLoad/", views.ExpenseslistLoad),
        path("Expenseslist/", views.getExpenseslist),

        path("ExaddRevenueLoad/", views.ExaddRevenueLoad),
        path("ExaddRevenue/", views.ExaddRevenue),

        path("ExRevenueListLoad/", views.ExRevenueListLoad),
        path("ExRevenueList/", views.getRevenueList),




        path("ExupdateTransacktionLoad/", views.ExupdateTransacktionLoad),
        path("loadingDataToUpdatePage/", views.loadingDataToUpdatePage),
        path("deleteExpensesRevenue/", views.deleteExpensesRevenue),
        path("ExupdateTransacktion/", views.ExupdateTransacktion),

        path("ExledgersLoad/", views.ExledgersLoad),
        path("Exledgers/", views. Exledgers),

        path("ExViewledgersLoad/", views. ExViewledgersLoad),
        path("ExpensesReportsLoad/", views.ExpensesReportsLoad),
        path("ExpensesReports/", views.ExpensesReports),
       # path("ExReportsDisplayLoad/", views.ExpensestotalLoad),
        path("ExReportsDisplay/", views.ExReportsDisplay),
        path("Backend/",views.BackendHome),


        path("getbyDateExpensestotal/", views.getbyDateTotalExpenses),



]