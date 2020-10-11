from django.shortcuts import render
from django.http import request
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
#Supplier
def loadaddsupplier(request):
    return render(request, "addSupplier.html")

def addsupplier(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    supplierid = request.POST.get('SupplierId')
    suppliername = request.POST.get('SupplierName')
    nic = request.POST.get('nic')
    registeredno = request.POST.get('registeredno')
    email = request.POST.get('email')
    address = request.POST.get('address')

    data = {"Suppliername": suppliername, "nic": nic, "Registeredno": registeredno, "Email": email, "Address": address}
    db.child("Supplier").child(supplierid).set(data)
    return render(request, "suppliers.html")

def showsupplier():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    stock_ids=db.child('Supplier').shallow().get().val()
    list_supids=[]
    for i in stock_ids:
        list_supids.append(i)
    print(list_supids)

    list_supnames=[]
    for i in list_supids:
        sup_names=db.child('Supplier').child(i).child('Suppliername').get().val()
        list_supnames.append(sup_names)
    print(list_supnames)

    list_nics=[]
    for i in list_supids:
        sup_nics=db.child('Supplier').child(i).child('nic').get().val()
        list_nics.append(sup_nics)
    print(list_nics)

    list_supemails = []
    for i in list_supids:
        sup_emails = db.child('Supplier').child(i).child('Email').get().val()
        list_supemails.append(sup_emails)
    print(list_supemails)

    list_supaddress = []
    for i in list_supids:
        sup_address = db.child('Supplier').child(i).child('Address').get().val()
        list_supaddress.append(sup_address)
    print(list_supaddress)

    list_supregno = []
    for i in list_supids:
        sup_regno = db.child('Supplier').child(i).child('Registeredno').get().val()
        list_supregno.append(sup_regno)
    print(list_supregno)

    comb_suplists= zip(list_supids,list_supnames,list_nics,list_supemails,list_supaddress,list_supregno)
    return comb_suplists

def loadshowsupplier(request):
    final_suplist=showsupplier()
    return render(request,"suppliers.html",{'final_suplist':final_suplist})

def loadeditsupplier(request):
    return render(request, "editSupplier.html")

def getsinglesupplier(sup_id):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    list_supids=[]
    list_supids.append(sup_id)

    list_snames=[]
    list_snames.append(db.child("Stock").child(sup_id).child("StockName").get().val())

    list_uprices=[]
    list_uprices.append(db.child("Stock").child(sup_id).child("UnitPrice").get().val())

    list_res_levels = []
    list_res_levels.append(db.child("Stock").child(sup_id).child("ReOrderLevel").get().val())
    comb_lists= zip(list_supids,list_snames,list_uprices,list_res_levels)
    return comb_lists

#inventory
def loadaddstock(request):
    return render(request, "addStock.html")
def addstock(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    stockid = request.POST.get('stockid')
    stockname = request.POST.get('stockname')
    unitprice = request.POST.get('unitprice')
    quantity = request.POST.get('quantity')
    reorderlevel =request.POST.get('reorderlevel')

    data = { "StockName": stockname, "UnitPrice": unitprice, "Quantity": quantity, "ReOrderLevel": reorderlevel}
    db.child("Stock").child(stockid).set(data)
    final_list = showstock()
    return render(request, "inventorypage.html", {'final_list': final_list})




def showstock():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    stock_ids=db.child('Stock').shallow().get().val()
    list_sids=[]
    for i in stock_ids:
        list_sids.append(i)
    print(list_sids)

    list_snames=[]
    for i in list_sids:
        st_names=db.child('Stock').child(i).child('StockName').get().val()
        list_snames.append(st_names)
    print(list_snames)

    list_uprices=[]
    for i in list_sids:
        st_uprices=db.child('Stock').child(i).child('UnitPrice').get().val()
        list_uprices.append(st_uprices)
    print(list_uprices)

    list_res_levels = []
    for i in list_sids:
        st_res_levels = db.child('Stock').child(i).child('ReOrderLevel').get().val()
        list_res_levels.append(st_res_levels)
    print(list_res_levels)

    comb_lists= zip(list_sids,list_snames,list_uprices,list_res_levels)

    return comb_lists

def loadshowstock(request):
    final_list=showstock()
    return render(request,"inventorypage.html",{'final_list':final_list})



def loadeditstock(request):
    stockid =request.POST.get('stockid')
    final_list=getsinglestock(stockid)
    return render(request, "editstock.html",{"final_list":final_list})

def getsinglestock(stockid):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    list_sids=[]
    list_sids.append(stockid)

    list_snames=[]
    list_snames.append(db.child("Stock").child(stockid).child("StockName").get().val())

    list_uprices=[]
    list_uprices.append(db.child("Stock").child(stockid).child("UnitPrice").get().val())

    list_res_levels = []
    list_res_levels.append(db.child("Stock").child(stockid).child("ReOrderLevel").get().val())
    comb_lists= zip(list_sids,list_snames,list_uprices,list_res_levels)
    return comb_lists

def updatestock(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    stockid = request.POST.get('stockid')
    stockname = request.POST.get('stockname')
    unitprice = request.POST.get('unitprice')
    quantity = request.POST.get('quantity')
    reorderlevel = request.POST.get('reorderlevel')

    data = {"StockName": stockname, "UnitPrice": unitprice, "Quantity": quantity, "ReOrderLevel": reorderlevel}
    db.child("Stock").child(stockid).set(data)

    final_list = showstock()
    return render(request, "inventorypage.html", {'final_list': final_list})


def deletestock(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    stockid = request.POST.get('stockid')
    db.child("Stock").child(stockid).remove()
    final_list = getsinglestock(stockid)
    return render(request, "inventorypage.html", {"final_list": final_list})



