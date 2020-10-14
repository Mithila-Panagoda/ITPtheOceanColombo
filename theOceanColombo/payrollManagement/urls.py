from django.urls import path
from . import views

urlpatterns = [
    path("addDeductions/", views.addAdditionalDeductions),
    path("addEarnings/", views.addEarnings),
    path("additionsDeductions/", views.getDetailsByRoomType),
    path("EPFOfWhoseSalaryIsNeeded/", views.EPFOfWhoseSalaryIsNeeded),
    path("EPFToCalculateSalary/", views.EPFToCalculateSalary),
    path("PayrollManagementHome/", views.directPayrollManagementHome),
    path("PaySlip/", views.dirPaySlip),
    path("SalaryDetailsOfAllEmployees/", views.dirSalaryDetailsOfAllEmployees),
    path("SalaryHistoryOfEmployee/", views.dirSalaryHistoryOfEmployee),
    path("UpdateAdditionsOrDeductions/", views.dirUpdateAdditionsOrDeductions),
    path("backendHome/", views.dirBackendHome),

]

