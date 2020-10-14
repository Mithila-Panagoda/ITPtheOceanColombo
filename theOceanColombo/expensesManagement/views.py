from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
import pyrebase
from datetime import datetime
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
    from datetime import date


    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    id = request.POST.get('id1')
    type = request.POST.get('type1')
    date = request.POST.get('date1')
    price = request.POST.get('price1')
    description = request.POST.get('des1')

    data = {'Type': type, "Date": date, "Price": price, "Description": description}
    db.child("Accounts").child("Expenses").child(id).set(data)
    db.child("Accounts").child("Expenses").child(type).set(data)


    return render(request, "ExaddExpense.html")


def ExpenseslistLoad(request):
    list_all = getExpenseslist()
    return render(request, "ExpensesList.html", {'list_all': list_all})


def getExpenseslist():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()



    expenses = db.child("Accounts").child("Expenses").child().shallow().get().val()
    list_expensesid = []
    for i in expenses:
        list_expensesid.append(i)

    list_type = []
    for i in list_expensesid:

        expensesType = db.child("Accounts").child("Expenses").child(i).child("Type").get().val()
        list_type.append(expensesType)

    list_date = []
    for i in list_expensesid:

        email = db.child("Accounts").child("Expenses").child(i).child("Date").get().val()
        list_date.append(email)


    list_amount = []
    for i in list_expensesid:

        amount = "Rs." + db.child("Accounts").child("Expenses").child(i).child("Price").get().val()
        list_amount.append(amount)


    list_discription = []
    for i in list_expensesid:

        description = db.child("Accounts").child("Expenses").child(i).child("Description").get().val()
        list_discription.append(description)

    list_all = zip(list_expensesid, list_type, list_amount, list_date, list_discription,)

    return list_all



#--------------------------------daily expenses-----------------------------------------------

def ExpensesReportsLoad(request):
    return render(request, "ExpensesReports.html")

def BackendHome(request):
    return render(request, "BackendHome.html")


def getbyDateTotalExpenses(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    dailyTotal=float
    dailyTotal =0
    expenses = db.child("Accounts").child("Expenses").shallow().get().val()
    list_expensesid = []
    for i in expenses:
        list_expensesid.append(i)


    for i in list_expensesid:
            list_type = []
            for i in list_expensesid:
                if request.POST.get('date') == db.child("Accounts").child("Expenses").child(i).child("Date").get().val():
                    expensesType = db.child("Accounts").child("Expenses").child(i).child("Type").get().val()
                    list_type.append(expensesType)
            print(list_type)

            list_date = []
            for i in list_expensesid:
                if request.POST.get('date') == db.child("Accounts").child("Expenses").child(i).child("Date").get().val() :
                    date = db.child("Accounts").child("Expenses").child(i).child("Date").get().val()
                    list_date.append(date)
            print(list_date)

            list_amount = []
            for i in list_expensesid:
                if request.POST.get('date') == db.child("Accounts").child("Expenses").child(i).child("Date").get().val():

                    amount = db.child("Accounts").child("Expenses").child(i).child("Price").get().val()
                    list_amount.append(amount)

            print(list_amount)
            list_discription = []
            for i in list_expensesid:
                if request.POST.get('date') == db.child("Accounts").child("Expenses").child(i).child("Date").get().val():
                    description = db.child("Accounts").child("Expenses").child(i).child("Description").get().val()
                    list_discription.append(description)
            print(list_discription)
            list_all = zip( list_type,list_date,list_amount,list_discription,)

            return render(request,"ExpensesReports.html",{"list_all": list_all})


# ------------------------------------Revenue------------------------------------------------------------------
def ExaddRevenueLoad(request):
    return render(request, "ExaddRevenue.html")


def ExaddRevenue(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    id = request.POST.get('id1')
    type = request.POST.get('type1')
    date = request.POST.get('date1')
    price = request.POST.get('price1')
    description = request.POST.get('des1')

    data = {"Type": type, "Date": date, "Price": price, "Description": description}
    db.child("Accounts").child("Revenue").child(id).set(data)
    return render(request, "ExaddRevenue.html")


def ExRevenueListLoad(request):
    return render(request, "ExRevenueList.html")
    list_all = getRevenuelist()
    return render(request, "ExRevenueList.html", {'list_all': list_all})


def getRevenueList(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    expenses = db.child("Accounts").child("Revenue").shallow().get().val()
    list_expensesid = []
    for i in expenses:
        list_expensesid.append(i)

    list_type = []
    for i in list_expensesid:
        expensesType = db.child("Accounts").child("Revenue").child(i).child("Type").get().val()
        list_type.append(expensesType)

    list_date = []
    for i in list_expensesid:
        email = db.child("Accounts").child("Revenue").child(i).child("Date").get().val()
        list_date.append(email)

    list_amount = []
    for i in list_expensesid:
        amount = "Rs." + db.child("Accounts").child("Revenue").child(i).child("Price").get().val()
        list_amount.append(amount)

    list_discription = []
    for i in list_expensesid:
        description = db.child("Accounts").child("Revenue").child(i).child("Description").get().val()
        list_discription.append(description)

    list_all = zip(list_expensesid, list_type, list_amount, list_date, list_discription)
    return list_all


# ----------------------------------------------------------------------------------------------



#----------------------------------------------------- upadate details---------------------------------
def ExupdateTransacktionLoad(request):
    expensesid = request.POST.get('expensesid')
    loadData = loadingDataToUpdatePage(expensesid)
    return render(request, "ExupdateTransacktion.html", {'list_all': loadData})


def loadingDataToUpdatePage(expensesid):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    list_expensesid = []
    list_expensesid.append(expensesid)

    list_type = []
    expensesType = db.child("Accounts").child("Expenses").child(expensesid).child("Type").get().val()
    list_type.append(expensesType)

    list_amount = []
    amount = db.child("Accounts").child("Expenses").child(expensesid).child("Price").get().val()
    list_amount.append(amount)

    list_date = []
    date = db.child("Accounts").child("Expenses").child(expensesid).child("Date").get().val()
    list_date.append(date)

    list_discription = []
    description = db.child("Accounts").child("Expenses").child(expensesid).child("Description").get().val()
    list_discription.append(description)

    list_all = zip(list_expensesid, list_type, list_amount, list_date, list_discription)
    return list_all


def ExupdateTransacktion(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    id = request.POST.get('expensesid')
    type = request.POST.get('type')
    price = request.POST.get('price')
    date = request.POST.get('date')
    description = request.POST.get('description')

    data = {"Type": type, "Price": price, "Date": date, "Description": description}
    db.child("Accounts").child("Expenses").child(id).update(data)
    list_all = getExpenseslist()
    return render(request, "ExpensesList.html", {"list_all": list_all})


# --------Delete expenses,revenue___________________________
def deleteExpensesRevenue(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    id = request.POST.get('expensesid')
    db.child("Accounts").child("Expenses").child(id).remove()
    data = getExpenseslist()
    return render(request, "ExpensesList.html", {"list_all": data})


# -----------------------------------------------------------------------------------------

#------------------------reports---------------------------------------------------------------------

def ExpensestotalLoad(request):
    list_all = getExpensestotal()
    return render(request, "ExReportsDisplay.html", {'list_all': list_all})

def getExpensestotal():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    sumE =0
    sumW =0
    sumF= 0

    expenses = db.child("Accounts").child("Expenses").shallow().get().val()
    list_id = []
    list_waterbillamount = []
    list_electricityamount = []
    list_foodBeveragesamount = []

    for i in expenses:
        list_id.append(i)
    for i in list_id:
        if db.child("Accounts").child("Expenses").child(i).child("Type").get().val() == "water bill":
            water = db.child("Accounts").child("Expenses").child(i).child("Price").get().val()
            list_waterbillamount.append(water)
        sum(water)
        print(sumW)



    for i in list_id:
        if db.child("Accounts").child("Expenses").child(i).child("Type").get().val() == "Electricity bill":
            ele = db.child("Accounts").child("Expenses").child(i).child("Price").get().val()
            list_electricityamount.append(ele)
            sumE = sumE + float(water)



    for i in list_id:
        if db.child("Accounts").child("Expenses").child(i).child("Type").get().val() == "Electricity bill":
            food = db.child("Accounts").child("Expenses").child(i).child("Price").get().val()
            list_foodBeveragesamount.append(food)
            sumE = sumE + float(food)

    total_all =zip(sumE,sumF,sumW)
    return total_all

def ExledgersLoad(request):
    return render(request, "ExLedgers.html")


def Exledgers(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    expenses = db.child("Accounts").child("Expenses").shallow().get().val()
    list_expensesid = []
    for i in expenses:
        list_expensesid.append(i)

    for i in list_expensesid:
        list_type = []
        for i in list_expensesid:
            if request.POST.get('date') == db.child("Accounts").child("Expenses").child(i).child("Date").get().val() and request.POST.get('type') == db.child("Accounts").child("Expenses").child(i).child("Type").get().val():
                expensesType = db.child("Accounts").child("Expenses").child(i).child("Type").get().val()
                list_type.append(expensesType)
        print(list_type)

        list_date = []
        for i in list_expensesid:
            if request.POST.get('date') == db.child("Accounts").child("Expenses").child(i).child("Date").get().val()  and request.POST.get('date') == db.child("Accounts").child("Expenses").child(i).child("Date").get().val():
                date = db.child("Accounts").child("Expenses").child(i).child("Date").get().val()
                list_date.append(date)
        print(list_date)

        list_amount = []
        for i in list_expensesid:
            if request.POST.get('date') == db.child("Accounts").child("Expenses").child(i).child("Date").get().val() and request.POST.get('date') == db.child("Accounts").child("Expenses").child(i).child("Date").get().val():
                amount = db.child("Accounts").child("Expenses").child(i).child("Price").get().val()
                list_amount.append(amount)


        list_discription = []
        for i in list_expensesid:
            if request.POST.get('date') == db.child("Accounts").child("Expenses").child(i).child("Date").get().val() and request.POST.get('date') == db.child("Accounts").child("Expenses").child(i).child("Date").get().val():
                description = db.child("Accounts").child("Expenses").child(i).child("Description").get().val()
                list_discription.append(description)
        print(list_discription)
        list_all = zip(list_type, list_date, list_amount, list_discription, )

        return render(request, "ExViewLedgers.html", {"list_all": list_all})




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
