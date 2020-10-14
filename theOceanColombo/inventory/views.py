import uuid

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


# Supplier
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
    final_list = showsupplier()
    return render(request, "suppliers.html", {"final_list": final_list})


def getsupemailsfun():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    stock_ids = db.child('Supplier').shallow().get().val()
    list_supids = []
    for i in stock_ids:
        list_supids.append(i)
    print(list_supids)

    list_supemails = []
    for i in list_supids:
        sup_emails = db.child('Supplier').child(i).child('Email').get().val()
        list_supemails.append(sup_emails)
    print(list_supemails)

    return list_supemails


def getsupemails(request):
    final_list = getsupemailsfun()
    return render(request, "purchaseOrders.html", {"final_list": final_list})


def showsupplier():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    stock_ids = db.child('Supplier').shallow().get().val()
    list_supids = []
    for i in stock_ids:
        list_supids.append(i)
    print(list_supids)

    list_supnames = []
    for i in list_supids:
        sup_names = db.child('Supplier').child(i).child('Suppliername').get().val()
        list_supnames.append(sup_names)
    print(list_supnames)

    list_nics = []
    for i in list_supids:
        sup_nics = db.child('Supplier').child(i).child('nic').get().val()
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

    comb_suplists = zip(list_supids, list_supnames, list_nics, list_supemails, list_supaddress, list_supregno)
    return comb_suplists


def loadshowsupplier(request):
    final_suplist = showsupplier()
    return render(request, "suppliers.html", {'final_suplist': final_suplist})


def loadeditsupplier(request):
    sup_id = request.POST.get('sup_id')
    final_suplist = getsinglesupplier(sup_id)
    return render(request, "editSupplier.html", {'final_suplist': final_suplist})


def getsinglesupplier(sup_id):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    list_supids = []
    list_supids.append(sup_id)

    list_supnames = []
    list_supnames.append(db.child("Supplier").child(sup_id).child("Suppliername").get().val())

    list_nics = []
    list_nics.append(db.child("Supplier").child(sup_id).child("nic").get().val())

    list_supemails = []
    list_supemails.append(db.child("Supplier").child(sup_id).child("Email").get().val())

    list_supaddress = []
    list_supaddress.append(db.child("Supplier").child(sup_id).child("Address").get().val())

    list_supregno = []
    list_supregno.append(db.child("Supplier").child(sup_id).child("Registeredno").get().val())

    comb_lists = zip(list_supids, list_supnames, list_nics, list_supemails, list_supaddress, list_supregno)
    return comb_lists


def updatesupplier(request):
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

    final_suplist = showsupplier()
    return render(request, "suppliers.html", {'final_suplist': final_suplist})


def deletesupplier(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    supplierid = request.POST.get('sup_id')
    db.child("Supplier").child(supplierid).remove()
    final_suplist = showsupplier()
    return render(request, "suppliers.html", {'final_suplist': final_suplist})


# inventory
def loadaddstock(request):
    return render(request, "addStock.html")


def addstock(request):
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


def showstock():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    stock_ids = db.child('Stock').shallow().get().val()
    list_sids = []
    for i in stock_ids:
        list_sids.append(i)
    print(list_sids)

    list_snames = []
    for i in list_sids:
        st_names = db.child('Stock').child(i).child('StockName').get().val()
        list_snames.append(st_names)
    print(list_snames)

    list_uprices = []
    for i in list_sids:
        st_uprices = db.child('Stock').child(i).child('UnitPrice').get().val()
        list_uprices.append(st_uprices)
    print(list_uprices)

    list_quantities = []
    for i in list_sids:
        st_quantity = db.child('Stock').child(i).child('Quantity').get().val()
        list_quantities.append(st_quantity)
    print(list_quantities)

    list_res_levels = []
    for i in list_sids:
        st_res_levels = db.child('Stock').child(i).child('ReOrderLevel').get().val()
        list_res_levels.append(st_res_levels)
    print(list_res_levels)

    final_list = zip(list_sids, list_snames, list_quantities,list_uprices, list_res_levels)

    return final_list


def loadshowstock(request):
    final_list = showstock()
    return render(request, "inventorypage.html", {'final_list': final_list})


def loadeditstock(request):
    print("heloooooo")
    Stockid = request.POST.get('stockid')
    print("stock ID: ",Stockid)
    final_list = getsinglestock(Stockid)
    print(final_list)
    return render(request, "editstock.html", {"final_list": final_list})


def getsinglestock(stockid):
    print("testinggggg")
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    list_sids = [stockid]
    list_snames = [db.child("Stock").child(stockid).child("StockName").get().val()]
    print("listNames : ",list_snames)
    list_uprices = []
    list_uprices.append(db.child('Stock').child(stockid).child('UnitPrice').get().val())
    list_quantities = []
    list_quantities.append(db.child("Stock").child(stockid).child("Quantity").get().val())

    list_res_levels = []
    list_res_levels.append(db.child("Stock").child(stockid).child("ReOrderLevel").get().val())
    print(list_res_levels)
    comb_lists = zip(list_sids, list_snames,list_quantities, list_uprices, list_res_levels)
    print("COMBO LIST",comb_lists)
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
    final_list = showstock()
    return render(request, "inventorypage.html", {"final_list": final_list})


# create lists
def createlists(request):
    return render(request, "createlists.html")


def getstockids(request):
    list_sids = getstockidsfun()
    print(list_sids)
    return render(request, "createlists.html", {"list_sids": list_sids})


def getstockidsfun():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    stock_ids = db.child('Stock').shallow().get().val()
    list_sids = []
    for i in stock_ids:
        list_sids.append(i)
    print(list_sids)

    return list_sids


def addlist(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    listid = request.POST.get('listid')
    print(listid)
    stockid = request.POST.get('stockid')
    # stockname = request.POST.get('stockname')
    quantity = request.POST.get('Quantity')
    data = {"Stockid": stockid, "Quantity": quantity}
    db.child('Order Lists').child(listid).child(stockid).set(data)
    list_sids = getstockidsfun()
    # list_lists=showlists()

    return render(request, "createlists.html", {"list_sids": list_sids})


def showlists(listid):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    list_sids = db.child('Order Lists').child(listid).shallow().get().val()
    list_list_sid = []
    for i in list_sids:
        list_list_sid.append(i)
    print(list_list_sid)

    list_stockid = []
    for i in list_list_sid:
        list_sid = db.child('Order Lists').child(listid).child(i).child('Stockid').get().val()
        list_stockid.append(list_sid)
    print(list_stockid)

    list_quantities = []
    for i in list_list_sid:
        st_quantities = db.child('Order Lists').child(listid).child(i).child('Quantity').get().val()
        list_quantities.append(st_quantities)
    print(list_quantities)

    comb_lists = zip(list_list_sid, list_stockid, list_quantities)

    return comb_lists


def getsinglestock(listid):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    list_listid = []
    list_listid.append(listid)

    list_sid = [] = []
    list_sid.append(db.child("Stock").child(listid).child("StockName").get().val())

    list_quantities = []
    list_quantities.append(db.child("Stock").child(listid).child("UnitPrice").get().val())

    comb_lists = zip(list_listid, list_sid, list_quantities)
    return comb_lists


def loadlisttable(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    listid = request.POST.get('listid')
    final_list = showlists(listid)

    return render(request, "createlists.html", {"final_list": final_list})


def deletelist(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    list_list_sid = request.POST.get('list_list_sid')
    # list_list_sid = request.POST.get('list_list_sid')
    print(list_list_sid)
    db.child('Order Lists').child(list_list_sid).remove()
    final_list = showlists(list_list_sid)
    return render(request, "createlists.html", {"final_list": final_list})


# purchase orders
def loadpurchaseorder(request):
    return render(request, "purchaseOrders.html")


def getlistidsfun():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    listid = db.child('Order Lists').shallow().get().val()
    list_listid = []
    for i in listid:
        list_listid.append(i)
    print(list_listid)
    return list_listid


def getlist_idsrep(request):
    list_listid = getlistidsfun()
    return render(request, "purchaseOrders.html", {"list_listid": list_listid})


def addlisttosupplier(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    supemail = request.POST.get('supemail')
    print(supemail)
    # stockid = request.POST.get('stockid')
    # stockname = request.POST.get('stockname')
    date = request.POST.get('date')
    print(date)

    listid = request.POST.get('listsid')
    print(listid)
    uid = uuid.uuid1()
    data = {"SupplierEmail": supemail, "Date": date, "ListId": listid}
    db.child('Purchase Order').child(uid).set(data)
    list_listid = getlistidsfun()

    return render(request, "purchaseOrders.html", {"list_listid": list_listid})


def generaterepo(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    list_id = request.POST.get('listsid')
    data = db.child('Purchase Order').shallow().get().val()
    datalists=db.child('Order Lists').child(list_id).shallow().get().val()
    print(datalists)
    list_poids = []
    for i in data:
        list_poids.append(i)
    print("blaaaa",list_poids)
    print(list_id)
    list_supemails = []
    for i in list_poids:
        if list_id == db.child('Purchase Order').child(i).child('ListId').get().val():
            supemail = db.child('Purchase Order').child(i).child('SupplierEmail').get().val()
            list_supemails.append(supemail)
    print("EMAIL!!!",list_supemails)

    list_stockids=[]
    for i in datalists:
        list_stockids.append(i)
    print(list_stockids)

    list_quantities = []
    for i in list_stockids:
        stock_ids=db.child('Order Lists').child(list_id).child(i).child('Quantity').get().val()
        list_quantities.append(stock_ids)
    print(list_quantities)

    final_list=zip(list_supemails,list_stockids,list_quantities)
    return render(request, "inventoryreports.html", {"final_list": final_list})


def getlist_idforrepo(request):
    list_listid = getlistidsfun()
    return render(request, "inventoryreports.html", {"list_listid": list_listid})

def loadbackendhomepage(request):
    return render(request, "BackendHome.html")
