from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
import pyrebase
from django.contrib import auth

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

def ExaddExpensesLoad(request):
    return render(request, "ExAddExpense.html")

def ExaddExpenses(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    id = request.POST.get('id1')
    date = request.POST.get('date1')
    price = request.POST.get('price1')
    description = request.POST.get('des1')

    data = {"Date": date, "Price": price, "Description": description}
    db.child("Accounts").child("expenses").child(id).set(data)
    return render(request, "ExpensesList.html")

def ExpenseslistLoad(request):
    return render(request, "ExpensesList.html")

def Expenseslist(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    expenses = db.child("Accounts").child("expenses").shallow().get().val()
    print(expenses)
    return render(request, "ExpensesList.html")



def ExaddRevenueLoad(request):
    return render(request, "ExaddRevenue.html")
def ExaddRevenue(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    id = request.POST.get('id1')
    date = request.POST.get('date1')
    price = request.POST.get('price1')
    description = request.POST.get('des1')
    data = {"Date": date, "Price": price, "Description": description}
    db.child("Accounts").child("Revenue").child(id).set(data)
    return render(request, "ExaddRevenue.html")

def ExRevenueListLoad(request):
    return render(request, "ExRevenueList.html")
def ExRevenueList(request):
    return render(request, "ExRevenueList.html")


def ExaddCapitalLoad(request):
    return render(request, "ExaddCapital.html")
def ExaddCapital(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    id = request.POST.get('capId')
    date = request.POST.get('capDate')
    type = request.POST.get('capType')
    price = request.POST.get('capPrice')
    description = request.POST.get('capDes')

    data = {"Date": date, "Price": price, "Description": description, "Type": type}
    db.child("Accounts").child("CapitalAccount").child(id).set(data)
    return render(request, "ExViewCapital.html")

def ExViewCapitalLoad(request):
    return render(request, "ExViewCapital.html")
def ExViewCapital(request):
    return render(request, "ExViewCapital.html")



def ExupdateTransacktionLoad(request):
    return render(request, "ExupdateTransacktion.html")
def ExupdateTransacktion(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    id = request.POST.get('id1')
    date = request.POST.get('date1')
    price = request.POST.get('price1')
    description = request.POST.get('des1')

    data = {"Date": date, "Price": price, "Description": description}
    db.child("Accounts").child("expenses").child(id).update(data)
    return render(request, "ExpensesList.html")


def ExledgersLoad(request):
    return render(request, "ExLedgers.html")
def Exledgers(request):
    return render(request, "ExViewLedgers.html")


def ExViewledgersLoad(request):
    return render(request, "ExViewLedgers.html")

def ExpensesReportsLoad(request):
    return render(request, "ExpensesReports.html")
def ExpensesReports(request):
    return render(request, "ExpensesReports.html")
def ExReportsDisplayLoad(request):
    return render(request, "ExReportsDisplay.html")

def ExReportsDisplay(request):
    return render(request, "ExReportsDisplay.html")


