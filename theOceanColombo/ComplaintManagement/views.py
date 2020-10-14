from django.shortcuts import render

# Create your views here.
import pyrebase

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

def complaintFrontendLoad(request):
    return render(request, "complaintfrontend.html")
def complaintFrontend(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    name = request.POST.get('cusname')
    email = request.POST.get('email')
    phnNo = request.POST.get('phn')
    feed = request.POST.get('feed')
    data = {"Name": name, "Email": email, "phnNumber": phnNo, "Feed": feed}
    db.child("AComplaint").child("customerFeed").child(name).set(data)
    return render(request, "complaintfrontend.html")


#display and  path to reply complaints

def complaintReplytableLoad(request):
    list_all = getcomplaintsdetails()
    return render(request, "complaintreplaytable.html",{'list_all':list_all})

def getcomplaintsdetails():

    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    cusName = db.child("Complaint").child("customerFeedback").shallow().get().val()
    list_cusName = []
    for i in cusName:
        list_cusName.append(i)


    list_email = []
    for i in list_cusName:
        email = db.child("Complaint").child("customerFeedback").child(i).child("Email").get().val()
        list_email.append(email)


    list_phnNo = []
    for i in list_cusName:
        phnNo = db.child("Complaint").child("customerFeedback").child(i).child("phnNumber").get().val()
        list_phnNo.append(phnNo)


    list_feedback = []
    for i in list_cusName:
        feedback = db.child("Complaint").child("customerFeedback").child(i).child("Feed").get().val()
        list_feedback.append(feedback)


    list_all = zip(list_cusName,list_email,list_feedback)
    return list_all


def complaintTypereplyLoad(request):
    return render(request, "complaintTypereply.html")
def complaintTypereply(request):
    return render(request, "complaintCheckReply.html")




