from django.shortcuts import render

import pyrebase

# Create your views here.
firebaseconfig = {
    'apiKey': "AIzaSyBew42hA7iZHy7zs47WMqIg-GSBnxP-ttM",
    'authDomain': "theoceancolombo-c128a.firebaseapp.com",
    'databaseURL': "https://theoceancolombo-c128a.firebaseio.com",
    'projectId': "theoceancolombo-c128a",
    'storageBucket': "theoceancolombo-c128a.appspot.com",
    'messagingSenderId': "925636680144",
    'appId': "1:925636680144:web:da1ab5d4f3b0d3231b01d5",
    'measurementId': "G-YH7TV23J8J"
}
firebase = pyrebase.initialize_app(firebaseconfig)
authe = firebase.auth()


def addAdditionalDeductions(request):
    return render(request, "addAdditionalDeductions.html")


def addEarnings(request):
    return render(request, "addAdditionalEarnings.html")


def additionsDeductions(request):
    return render(request, "AdditionsDeductions.html")


def EPFOfWhoseSalaryIsNeeded(request):
    return render(request, "EPFOfWhoseSalaryIsNeeded.html")


def EPFToCalculateSalary(request):
    return render(request, "EPFToCalculateSalary.html")


def directPayrollManagementHome(request):
    return render(request, "PayrollManagementHome.html")


def dirPaySlip(request):
    return render(request, "PaySlip.html")


def dirSalaryDetailsOfAllEmployees(request):
    return render(request, "SalaryDetailsOfAllEmployees.html")


def dirSalaryHistoryOfEmployee(request):
    return render(request, "SalaryHistoryOfEmployee.html")


def dirUpdateAdditionsOrDeductions(request):
    return render(request, "UpdateAdditionsOrDeductions.html")


def dirBackendHome(request):
    return render(request, "BackendHome.html")


def getDetailsByRoomType(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child("Staff").child("Employee").shallow().get().val()

    list_EPFNumber = []
    list_firstName = []
    list_lastName = []

    for j in data:
        list_EPFNumber.append(j)

    for j in list_EPFNumber:
        if request.POST.get('epfNo') == data:
            firstName = db.child("Staff").child("Employee").child(j).child("firstName").get().val()
            list_firstName.append(firstName)
        print(request.POST.get('epfNo'))
        print(data)

    for j in list_EPFNumber:
        if request.POST.get('epfNo') == data:
            lastName = db.child("Staff").child("Employee").child(j).child("lastName").get().val()
            list_lastName.append(lastName)

    if request.POST.get('epfNo') == data:
        data = zip(list_EPFNumber, list_firstName, list_lastName)
        return render(request, "additionsDeductions.html", {'data': data})
    else:
        return render(request, "EPFToCalculateSalary.html")
