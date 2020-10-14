from typing import final
from django.shortcuts import render
from django.http import request
import pyrebase
from requests.sessions import Request
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
storage = firebase.storage()

#Front end Restaurant
def restaurantLoadBeverageData():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child("resturant").child('beverages').shallow().get().val()
    list_drinkname=[]
    for i in data:
        list_drinkname.append(i)
    list_drinkDesc=[]
    list_drinkSize=[]
    list_drinkType=[]
    list_drinkPrice=[]

    for i in list_drinkname:
        if db.child("resturant").child('beverages').child(i).child("available").get().val() == "Yes":
            query= db.child("resturant").child('beverages').child(i).child("desc").get().val()
            list_drinkDesc.append(query)
        if db.child("resturant").child('beverages').child(i).child("available").get().val() == "Yes":
            query= db.child("resturant").child('beverages').child(i).child("price").get().val()
            list_drinkPrice.append(query)
        if db.child("resturant").child('beverages').child(i).child("available").get().val() == "Yes":
            query= db.child("resturant").child('beverages').child(i).child("size").get().val()
            list_drinkSize.append(query)
        if db.child("resturant").child('beverages').child(i).child("available").get().val() == "Yes":
            query= db.child("resturant").child('beverages').child(i).child("type").get().val()
            list_drinkType.append(query)
    final_data=zip(list_drinkname,list_drinkDesc,list_drinkSize,list_drinkType,list_drinkPrice)
    return final_data

def restaurantLoadMealData():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child("resturant").child('meals').shallow().get().val()
    list_mealname=[]
    for i in data:
        list_mealname.append(i)
    list_mealDesc=[]
    list_mealPrice=[]
    list_spicelvl=[]
    list_veg=[]
    print("MealName: ",list_mealname)
    for i in list_mealname:
        if db.child("resturant").child('meals').child(i).child("available").get().val() == "Yes":
            query= db.child("resturant").child('meals').child(i).child("desc").get().val()
            list_mealDesc.append(query)
    for i in list_mealname:
        if db.child("resturant").child('meals').child(i).child("available").get().val() == "Yes":
            query= db.child("resturant").child('meals').child(i).child("price").get().val()
            list_mealPrice.append(query)
    for i in list_mealname:
        if db.child("resturant").child('meals').child(i).child("available").get().val() == "Yes":
            query= db.child("resturant").child('meals').child(i).child("spicelvl").get().val()
            list_spicelvl.append(query)
    for i in list_mealname:
        if db.child("resturant").child('meals').child(i).child("available").get().val() == "Yes":
            query= db.child("resturant").child('meals').child(i).child("veg").get().val()
            list_veg.append(query)
            print(list_veg)
    print("price : ",list_mealPrice)
    final_data = zip(list_mealname,list_mealDesc,list_spicelvl,list_veg,list_mealPrice)
    return final_data
#Tables DB Code
def getSingleTableData(tblname):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    list_tblname=[]
    list_tblname.append(tblname)
    list_noseats=[]
    list_rlocation=[]
    list_location=[]
    list_rstatus=[]
    list_astatus=[]

    list_noseats.append(db.child("resturant").child('tables').child(tblname).child("No Seats").get().val())
    list_rlocation.append(db.child("resturant").child('tables').child(tblname).child("Restaurant Location").get().val())
    list_location.append(db.child("resturant").child('tables').child(tblname).child("Location").get().val())
    list_rstatus.append(db.child("resturant").child('tables').child(tblname).child("Resereved").get().val())
    list_astatus.append(db.child("resturant").child('tables').child(tblname).child("Available").get().val())

    final_data = zip(list_tblname,list_noseats,list_rlocation,list_location,list_rstatus,list_astatus)
    return final_data

def getBookedTableData():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child("resturant").child('tables').shallow().get().val()
    list_tableID=[]
    for i in data:
        list_tableID.append(i)
    list_tableID.sort(reverse=True)

    list_tblname=[]
    list_noseats=[]
    list_rlocation=[]
    list_location=[]
    list_rstatus=[]
    list_astatus=[]

    for i in list_tableID:
        if db.child("resturant").child('tables').child(i).child("Resereved").get().val() == "Reserved":
            query = db.child("resturant").child('tables').child(i).child("tableID").get().val()
            list_tblname.append(query)
        if db.child("resturant").child('tables').child(i).child("Resereved").get().val() == "Reserved":
            query = db.child("resturant").child('tables').child(i).child("No Seats").get().val()
            list_noseats.append(query)
        if db.child("resturant").child('tables').child(i).child("Resereved").get().val() == "Reserved":
            query = db.child("resturant").child('tables').child(i).child("Restaurant Location").get().val()
            list_rlocation.append(query)
        if db.child("resturant").child('tables').child(i).child("Resereved").get().val() == "Reserved":
            query = db.child("resturant").child('tables').child(i).child("Location").get().val()
            list_location.append(query)
        if db.child("resturant").child('tables').child(i).child("Resereved").get().val() == "Reserved":
            query = db.child("resturant").child('tables').child(i).child("Resereved").get().val()
            list_rstatus.append(query)
        if db.child("resturant").child('tables').child(i).child("Resereved").get().val() == "Reserved":
            query = db.child("resturant").child('tables').child(i).child("Available").get().val()
            list_astatus.append(query)
    final_data = zip(list_tblname,list_noseats,list_rlocation,list_location,list_rstatus,list_astatus)
    return final_data

def getFreeTableData():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child("resturant").child('tables').shallow().get().val()
    list_tableID=[]
    for i in data:
        list_tableID.append(i)
    list_tableID.sort(reverse=True)

    list_tblname=[]
    list_noseats=[]
    list_rlocation=[]
    list_location=[]
    list_rstatus=[]
    list_astatus=[]
    print("tbaleID ",list_tableID)
    for i in list_tableID:
        if db.child("resturant").child('tables').child(i).child("Resereved").get().val() == "Free":
            query = db.child("resturant").child('tables').child(i).child("tableID").get().val()
            list_tblname.append(query)
        if db.child("resturant").child('tables').child(i).child("Resereved").get().val() == "Free":
            query = db.child("resturant").child('tables').child(i).child("No Seats").get().val()
            list_noseats.append(query)
        if db.child("resturant").child('tables').child(i).child("Resereved").get().val() == "Free":
            query = db.child("resturant").child('tables').child(i).child("Restaurant Location").get().val()
            list_rlocation.append(query)
        if db.child("resturant").child('tables').child(i).child("Resereved").get().val() == "Free":
            query = db.child("resturant").child('tables').child(i).child("Location").get().val()
            list_location.append(query)
        if db.child("resturant").child('tables').child(i).child("Resereved").get().val() == "Free":
            query = db.child("resturant").child('tables').child(i).child("Resereved").get().val()
            list_rstatus.append(query)
        if db.child("resturant").child('tables').child(i).child("Resereved").get().val() == "Free":
            query = db.child("resturant").child('tables').child(i).child("Available").get().val()
            list_astatus.append(query)
    print("rlocation : ",list_rlocation)
    final_data = zip(list_tblname,list_noseats,list_rlocation,list_location,list_rstatus,list_astatus)
    return final_data

def getallTableData():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child("resturant").child('tables').shallow().get().val()
    list_tableID=[]
    for i in data:
        list_tableID.append(i)
    list_tableID.sort(reverse=True)
    print(list_tableID)

    list_noseats=[]
    list_rlocation=[]
    list_location=[]
    list_rstatus=[]
    list_astatus=[]

    for i in list_tableID:
        query = db.child("resturant").child('tables').child(i).child("No Seats").get().val()
        list_noseats.append(query)
        print("NO Seats :",list_noseats)
    for i in list_tableID:
        query = db.child("resturant").child('tables').child(i).child("Restaurant Location").get().val()
        list_rlocation.append(query)
    for i in list_tableID:
        query = db.child("resturant").child('tables').child(i).child("Location").get().val()
        list_location.append(query)
    for i in list_tableID:
        query = db.child("resturant").child('tables').child(i).child("Resereved").get().val()
        list_rstatus.append(query)
    for i in list_tableID:
        query = db.child("resturant").child('tables').child(i).child("Available").get().val()
        list_astatus.append(query)

    final_data = zip(list_tableID,list_noseats,list_rlocation,list_location,list_rstatus,list_astatus)
    print("finalData: ",final_data)
    return final_data
        

#Beverage DB Code
def getBeverageData():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child("resturant").child('beverages').shallow().get().val()
    list_beveragenames=[]
    for i in data:
        list_beveragenames.append(i)
    list_beveragenames.sort(reverse=True)

    list_drinkDesc=[]
    list_drinkPrice=[]
    list_drinkSize=[]
    list_drinktype=[]
    list_drinkstatus=[]

    for i in list_beveragenames:
        query = db.child("resturant").child('beverages').child(i).child("desc").get().val()
        list_drinkDesc.append(query)
    for i in list_beveragenames:
        query = db.child("resturant").child('beverages').child(i).child("price").get().val()
        list_drinkPrice.append(query)
    for i in list_beveragenames:
        query = db.child("resturant").child('beverages').child(i).child("size").get().val()
        list_drinkSize.append(query)
    for i in list_beveragenames:
        query = db.child("resturant").child('beverages').child(i).child("type").get().val()
        list_drinktype.append(query)
    for i in list_beveragenames:
        query = db.child("resturant").child('beverages').child(i).child("available").get().val()
        list_drinkstatus.append(query)

    final_data=zip(list_beveragenames,list_drinkDesc,list_drinkPrice,list_drinkSize,list_drinktype,list_drinkstatus)
    return final_data

def singleDrinkData(drinkname):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    list_beveragenames=[]
    list_drinkDesc=[]
    list_drinkPrice=[]
    list_drinkSize=[]
    list_drinktype=[]
    list_drinkstatus=[]

    list_beveragenames.append(drinkname)
    list_drinkDesc.append(db.child("resturant").child('beverages').child(drinkname).child("desc").get().val())
    list_drinkPrice.append(db.child("resturant").child('beverages').child(drinkname).child("price").get().val())
    list_drinkSize.append(db.child("resturant").child('beverages').child(drinkname).child("size").get().val())
    list_drinktype.append(db.child("resturant").child('beverages').child(drinkname).child("type").get().val())
    list_drinkstatus.append(db.child("resturant").child('beverages').child(drinkname).child("available").get().val())

    final_data = zip(list_beveragenames,list_drinkDesc,list_drinkPrice,list_drinkSize,list_drinktype,list_drinkstatus)
    return final_data
    
#Meal DB code
def getmealdata():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child("resturant").child('meals').shallow().get().val()
    #if not bool(data):
      #  return -1
    list_mealname=[]
    for i in data:
        list_mealname.append(i)
    list_mealname.sort(reverse=True)
    list_mealDesc=[]
    list_mealPrice=[]
    list_spicelvl=[]
    list_status=[]
    list_veg=[]
    for i in list_mealname:
        query = db.child("resturant").child('meals').child(i).child("desc").get().val()
        list_mealDesc.append(query)
    for i in list_mealname:
        query = db.child("resturant").child('meals').child(i).child("price").get().val()
        list_mealPrice.append(query)
    for i in list_mealname:
        query = db.child("resturant").child('meals').child(i).child("spicelvl").get().val()
        list_spicelvl.append(query)
    for i in list_mealname:
        query = db.child("resturant").child('meals').child(i).child("available").get().val()
        list_status.append(query)
    for i in list_mealname:
        query = db.child("resturant").child('meals').child(i).child("veg").get().val()
        list_veg.append(query)
        

    final_data=zip(list_mealname,list_mealDesc,list_mealPrice,list_spicelvl,list_status,list_veg)
    return final_data

def getSingleMealdata(MealName):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()  
    list_mealName=[]
    list_mealDesc=[]
    list_mealPrice=[]
    list_spicelvl=[]
    list_status=[]
    list_veg=[]
    list_mealName.append(MealName)
    list_mealDesc.append(db.child("resturant").child('meals').child(MealName).child("desc").get().val())
    list_mealPrice.append(db.child("resturant").child('meals').child(MealName).child("price").get().val())  
    list_spicelvl.append(db.child("resturant").child('meals').child(MealName).child("spicelvl").get().val())
    list_status.append(db.child("resturant").child('meals').child(MealName).child("available").get().val())
    list_veg.append(db.child("resturant").child('meals').child(MealName).child("veg").get().val())

    final_data=zip(list_mealName,list_mealDesc,list_mealPrice,list_spicelvl,list_status,list_veg)
    return final_data
#Beverage templates
def loadBeverageMngt(request):
    final_data=getBeverageData()
    return render(request,"resturantbeveragemngt.html",{'final_data':final_data})


def loadadddrink(request):
    return render(request, "addbeverage.html")


def adddrink(request):  # code not implemented
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    storage = firebase.storage()
    #imgName = request.POST.get('beveragePic')
    name = request.POST.get('name')
    #path_on_cloud = "Restuarant/Beverages/"+name+"/"+imgName
    #storage.child(path_on_cloud).put(imgName)
    #imgurl = storage.child(path_on_cloud).get_url()
    price = request.POST.get('price')
    size = request.POST.get('size')
    desc = request.POST.get('desc')
    status = request.POST.get('status')
    type = request.POST.get('drink')
    data={"price":price,"size":size,"desc":desc,"type":type,"available": status}
    db.child("resturant").child("beverages").child(name).set(data)
    final_data=getBeverageData()
    return render(request,"resturantbeveragemngt.html",{'final_data':final_data})
    
def loadupdatebeverage(request):
    drinkName = request.POST.get('drinkName')
    final_data = singleDrinkData(drinkName)
    return render(request,"updatebeverage.html",{'final_data':final_data})

def updatebeverage(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    name = request.POST.get('name')
    price = request.POST.get('price')
    size = request.POST.get('size')
    desc = request.POST.get('desc')
    status = request.POST.get('status')
    type = request.POST.get('drink')
    data={"price":price,"size":size,"desc":desc,"type":type,"available": status}
    db.child("resturant").child("beverages").child(name).update(data)
    final_data=getBeverageData()
    return render(request,"resturantbeveragemngt.html",{'final_data':final_data})

def deleteBeverage(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    drinkname = request.POST.get('drinkname')
    db.child("resturant").child("beverages").child(drinkname).remove()
    final_data=getBeverageData()
    return render(request,"resturantbeveragemngt.html",{'final_data':final_data})
#--------------------------------------------------------------------------
#Tables Templates
def loadBookedTables(request):
    final_data=getBookedTableData()
    return render(request,"restaurantTableMngt.html",{"final_data":final_data})

def loadFreeTables(request):
    final_data=getFreeTableData()
    return render(request,"restaurantTableMngt.html",{"final_data":final_data})

def loadTableMngt(request):
    final_data =getallTableData()
    return render(request,"restaurantTableMngt.html",{"final_data":final_data})

def loadAddTable(request):
    return render(request,"addTable.html")

def addTables(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    tbID = request.POST.get('tblid')
    noSeats = request.POST.get('noSeats')
    rlocation = request.POST.get('restaurantLocation')
    location = request.POST.get('location')
    reserveStatus = request.POST.get('rstatus')
    availableStatus = request.POST.get('aStatus')
    data={"tableID":tbID,"No Seats":noSeats,"Restaurant Location":rlocation,"Location":location,"Resereved":reserveStatus,"Available":availableStatus}
    db.child("resturant").child("tables").child(tbID).set(data)    
    return render(request,"addTable.html")

def loadupdateTables(request):
    tblname=request.POST.get('tblname')
    final_data=getSingleTableData(tblname)
    return render(request,"updatetable.html",{"final_data":final_data})

def UpdateTables(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    tbID = request.POST.get('tblid')
    noSeats = request.POST.get('noSeats')
    rlocation = request.POST.get('restaurantLocation')
    location = request.POST.get('location')
    reserveStatus = request.POST.get('rstatus')
    availableStatus = request.POST.get('aStatus')
    data={"tableID":tbID,"No Seats":noSeats,"Restaurant Location":rlocation,"Location":location,"Resereved":reserveStatus,"Available":availableStatus}
    db.child("resturant").child("tables").child(tbID).update(data)
    final_data=getallTableData()
    return render(request,"restaurantTableMngt.html",{"final_data":final_data})

def deleteTable(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    tblname = request.POST.get('tblname')
    db.child("resturant").child("tables").child(tblname).remove()
    final_data = getallTableData()
    return render(request,"restaurantTableMngt.html",{"final_data":final_data})

#meals templates
def loadmealmngt(request):
    final_data=getmealdata()
    return render(request, "resturantmealmngt.html",{'final_data':final_data})

def loadAddMeal(request):
    return render(request,"addmeal.html")

def addMeal(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    mealname = request.POST.get('name')
    price = request.POST.get('price')
    spice = request.POST.get('spicelvl')
    desc = request.POST.get('desc')
    status = request.POST.get('status')
    veg = request.POST.get('veg')
    data = {"price": price, "spicelvl": spice, "desc": desc, "veg": veg, "available": status}
    db.child("resturant").child("meals").child(mealname).set(data)
    final_data=getmealdata()
    return render(request, "resturantmealmngt.html",{'final_data':final_data})

def loadUpdatemeal(request):
    mealName = request.POST.get('mealName')
    final_data=getSingleMealdata(mealName)
    return render(request, "updatemeal.html",{"final_data":final_data})

def updateMeal(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    mealname = request.POST.get('name')
    price = request.POST.get('price')
    desc = request.POST.get('desc')
    spice = request.POST.get('spicelvl')
    status = request.POST.get('status')
    veg = request.POST.get('veg')
    data = {"price": price, "spicelvl": spice, "desc": desc, "veg": veg,"available": status}
    db.child("resturant").child("meals").child(mealname).update(data)
    final_data=getmealdata()
    return render(request, "resturantmealmngt.html",{'final_data':final_data})

def deleteMeal(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    mealname = request.POST.get('mealName')
    db.child("resturant").child("meals").child(mealname).remove()
    final_data=getmealdata()
    return render(request, "resturantmealmngt.html",{'final_data':final_data})

#---------------------------------------------------------------------------------
#Front end pages 
def loadRestaurantTypeSelection(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    rtype = request.POST.get('rtype')
    noppl = request.POST.get('noppl')
    print(rtype)
    list_tabledata=[]
    data = db.child("resturant").child("tables").shallow().get().val()
    for i in data:
        list_tabledata.append(i)
    print ("table data : ",list_tabledata)
    list_tablenames=[]
    list_restaurantname=[]
    if rtype == "Ocean by O":
        for i in list_tabledata:
            if db.child("resturant").child("tables").child(i).child("Restaurant Location").get().val() == "Ocean by O" and db.child("resturant").child("tables").child(i).child("Resereved").get().val() == "Free" and db.child("resturant").child("tables").child(i).child("No Seats").get().val() == noppl:
                query = db.child("resturant").child('tables').child(i).child("tableID").get().val()
                list_tablenames.append(query)
                print("table Names : ",list_tablenames)
        if not list_tablenames:
             return render(request,"restaurantTypeSelection.html")
        list_restaurantname.append("Ocean by O")
    elif rtype == "Ground Floor":
        for i in list_tabledata:
            if db.child("resturant").child("tables").child(i).child("Restaurant Location").get().val() == "Ground Floor" and db.child("resturant").child("tables").child(i).child("Resereved").get().val() == "Free" and db.child("resturant").child("tables").child(i).child("No Seats").get().val() == noppl:
                query = db.child("resturant").child('tables').child(i).child("tableID").get().val()
                list_tablenames.append(query)
        if not list_tablenames:
             return render(request,"restaurantTypeSelection.html")
        list_restaurantname.append("Ground Floor")
    #final_data=zip(list_tablenames,list_restaurantname)
    print("restaurant name : ",list_restaurantname)
    return render(request,"restaurantTableReservation.html",{"final_data":list_tablenames})

def addBooking(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    cname = request.POST.get('fname')
    cemail = request.POST.get('cemail')
    global cnic 
    cnic = request.POST.get('cnic')
    cnumber = request.POST.get('cnumber')
    caddress =request.POST.get('caddress')
    tblname = request.POST.get('tblname')
    arrivalDate = request.POST.get('arrivalDate')
    data={"Full Name":cname,"Email":cemail,"NIC":cnic,"Phone":cnumber,"Billing Address":caddress,"tableID":tblname,"Reservation Date":arrivalDate}
    updatetbldata = {"Resereved":"Resereved"}
    db.child("resturant").child("tables").child(tblname).update(updatetbldata)
    db.child("Restaurant Booking").child(cnic).set(data)
    
    final_data=restaurantLoadMealData()
    return render(request,"restaurantmealselection.html",{"final_data":final_data})

def addMealToCart(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    mealName = request.POST.get('mealname')
    mealPrice = request.POST.get('mealprice')
    qty = request.POST.get('qty')
    grossPrice = float(qty) * float(mealPrice)

    data = {"Dish Name":mealName,"Price":mealPrice,"QTY":qty,"Total":grossPrice}
    db.child("Restaurant Booking").child(cnic).child("cart").child(mealName).set(data)
    final_data=restaurantLoadMealData()
    return render(request,"restaurantmealselection.html",{"final_data":final_data})

def addDrinkToCart(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    Drinkname = request.POST.get('drinkname')
    drinkPrice = request.POST.get('drinkprice')
    qty = request.POST.get('qty')
    grossPrice = float(drinkPrice)*float(qty)
    data={"Drink Name":Drinkname,"Price":drinkPrice,"QTY":qty,"Total":grossPrice}
    db.child("Restaurant Booking").child(cnic).child("cart").child(Drinkname).set(data)
    final_data=restaurantLoadBeverageData()
    return render(request,"restaurantbeverageselection.html",{"final_data":final_data})

def loadTableSelection(request):
    return render(request,"restaurantTypeSelection.html")

def loadmealselection(request):
    final_data=restaurantLoadMealData()
    return render(request,"restaurantmealselection.html",{"final_data":final_data})

def loadBeverageSelection(request):
    final_data=restaurantLoadBeverageData()
    return render(request,"restaurantbeverageselection.html",{"final_data":final_data})