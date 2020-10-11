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
    list_all = getExpenseslist()
    return render(request, "ExpensesList.html", {'list_all': list_all})


def getExpenseslist():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    expenses = db.child("Accounts").child("expenses").shallow().get().val()
    list_expensesid = []
    for i in expenses:
        list_expensesid.append(i)

    list_date = []
    for i in list_expensesid:
        email = db.child("Accounts").child("expenses").child(i).child("Date").get().val()
        list_date.append(email)

    list_amount = []
    for i in list_expensesid:
        amount = "Rs." +db.child("Accounts").child("expenses").child(i).child("Price").get().val()
        list_amount.append(amount)

    list_discription = []
    for i in list_expensesid:
        description = db.child("Accounts").child("expenses").child(i).child("Description").get().val()
        list_discription.append(description)

    list_all = zip(list_expensesid, list_amount,list_date,list_discription)
    return list_all





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


#upadate details
def ExupdateTransacktionLoad(request):
    expensesid= request.POST.get('expensesid')
    loadData=loadingDataToUpdatePage(expensesid)
    return render(request, "ExupdateTransacktion.html",{'list_all': loadData})

def loadingDataToUpdatePage(expensesid):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()


    list_expensesid = []
    list_expensesid.append(expensesid)


    list_amount = []
    amount = db.child("Accounts").child("expenses").child(expensesid).child("Price").get().val()
    list_amount.append(amount)

    list_date = []
    date = db.child("Accounts").child("expenses").child(expensesid).child("Date").get().val()
    list_date.append(date)

    list_discription = []
    description = db.child("Accounts").child("expenses").child(expensesid).child("Description").get().val()
    list_discription.append(description)

    list_all = zip(list_expensesid,list_amount ,list_date, list_discription)
    return list_all


def ExupdateTransacktion(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    id = request.POST.get('expensesid')
    date = request.POST.get('date')
    price = request.POST.get('price')
    description = request.POST.get('description')

    data = { "Date": date, "Price": price, "Description": description}
    db.child("Accounts").child("expenses").child(id).update(data)
    list_all = getExpenseslist()
    return render(request, "ExpensesList.html", {"list_all": list_all})

#--------Delete expenses,revenue___________________________
def deleteExpensesRevenue(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    id =request.POST.get('expensesid')
    db.child("Accounts").child("expenses").child(id).remove()
    data =getExpenseslist()
    return render(request, "ExpensesList.html", {"list_all": data})




#-----------------------------------------------------------------------------------------
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


