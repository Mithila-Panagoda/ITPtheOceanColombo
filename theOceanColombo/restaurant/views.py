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
storage = firebase.storage()

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
def loadadddrink(request):
    return render(request, "addbeverage.html")

def adddrink(request):#code not implemented
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
    type = request.POST.get('drink')
    data={"price":price,"size":size,"desc":desc,"type":type}
    db.child("resturant").child("beverages").child(name).set(data)
    
def loadupdatebeverage(request):
    return render(request,"updatebeverage.html")

def updatebeverage(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    name = request.POST.get('name')
    price = request.POST.get('price')
    size = request.POST.get('size')
    desc = request.POST.get('desc')
    drink = request.POST.get('drink')
    data={"price":price,"size":size,"desc":desc,"drink":drink}
    db.child("resturant").child("beverages").child(name).update(data)
    # return render(request, "resturantmealmngt.html")
#--------------------------------------------------------------------------
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


