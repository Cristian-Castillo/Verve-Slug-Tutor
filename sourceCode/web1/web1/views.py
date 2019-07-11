from django.shortcuts import render
import pyrebase
from django.contrib import auth

config = {
    'apiKey': "AIzaSyBHHg2e5gRop8tcO2RReu8paiEXJbGomVw",
    'authDomain': "verve-slug-tutor.firebaseapp.com",
    'databaseURL': "https://verve-slug-tutor.firebaseio.com",
    'projectId': "verve-slug-tutor",
    'storageBucket': "verve-slug-tutor.appspot.com",
    'messagingSenderId': "1013220996189",
    "serviceAccount": "verve-slug-tutor-firebase-adminsdk-6nqeg-bc0cd1c99d.json",
    'appId': "1:1013220996189:web:3e2186a9da25103e"
}
firebase = pyrebase.initialize_app(config)
database=firebase.database()
authe=firebase.auth()

# user = auth.sign_in_with_email_and_password()

def login(request):
    return render(request, "base.html")

def postsign(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')

    #    message="invalid credentials"
    #    return render(request, "login.html", {"messg":message})
    #print(user['idToken'])
    #session_id=user['idToken']
    #request.session['uid']=str(session_id)
    return render(request, "base.html", {"e":email})

def logout(request):
    authe.logout(request)
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def checkid(request):
    id=request.POST.get('id')
    for user in database.child("userdata").get().each():
        if(id==user.val().get("id")):
            print("Already existed ID")
            return render(request, "base.html")


def postsignup(request):

    id=request.POST.get('id')
    pw = request.POST.get('pw1')
    pwcf = request.POST.get('pw2')
    fname = request.POST.get('name1')
    lname = request.POST.get('name2')
    email = request.POST.get('email')
    contact = request.POST.get('contact')

    # if (id=='')|(pw=='')|(pw!=pwcf)|(fname=='')|(lname=='')|(email=='')|(contact==''):
    #     print("Wrong Input")
    #     return render(request, "base.html")
    # else:
    data={
        "ID":id,
        "PW":pw,
        "FN":fname.lower(),
        "LN":lname.lower(),
        "EMAIL":email,
        "CONTACT":contact
    }
    database.child("users").child(uid).child("details").set(data)
    return render(request, "knowledge.html")
