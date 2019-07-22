from django.shortcuts import render
import pyrebase # CC: imported pyrebase wrapper, essentially derives from firebase July 9, 2019
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (CreateView)
from .models import Post

# CC: Included API from Verve-Slug-Tutor and succesfully integrated authentication ------------------------------------------
config = {
    'apiKey': "AIzaSyBHHg2e5gRop8tcO2RReu8paiEXJbGomVw",
    'authDomain': "verve-slug-tutor.firebaseapp.com",
    'databaseURL': "https://verve-slug-tutor.firebaseio.com",
    'projectId': "verve-slug-tutor",
    'storageBucket': "verve-slug-tutor.appspot.com",
    'messagingSenderId': "1013220996189",
    'appId': "1:1013220996189:web:462bd852caeea191"
  }

firebase = pyrebase.initialize_app(config) # enables the pyrebase wrapper to be used, passed API into function
authe = firebase.auth()
database= firebase.database() # created the database

#CC:  End of API ----------------------------------------------------------------------------------------------------------------



def home(request):

    message = "hide"
    try:
        idtoken = request.session['uid']
        print(idtoken)
        localID = authe.get_account_info(idtoken)['users'][0]['localId']
        return render(request, "blog/home.html", {"title": "Profile"})

    except KeyError:
        return render(request, "blog/home.html", {"messg": message})



def about(request):
    message = "hide"
    try:
        idtoken = request.session['uid']
        return render(request, "blog/about.html", {"title": "About"})

    except KeyError:
        return render(request, "blog/about.html", {"messg": message})



def signup(request):
    return render(request, 'blog/signup.html', {'title': 'Signup'})



def post(request):
    form = UserCreationForm()
    try:
        idtoken = request.session['uid']
        return render(request, 'blog/post_form.html', {'form': form})

    except KeyError:
        return render(request, "blog/login.html", {"messg": message})



class PostCreateView(CreateView):
    model = Post
    fields = ['Title', 'Need', 'Offering', 'Description']



def knowledge(request):
    message = "Please log in to access this feature."
    try:
        idtoken = request.session['uid']
        localID = authe.get_account_info(idtoken)['users'][0]['localId']
        name = database.child('users').child(localID).child('details').child('name').get().val()
        return render(request, "blog/knowledge.html", {"e": name})

    except KeyError:
        return render(request, "blog/login.html", {"messg": message})



def passwordReset(request):
    return render(request, "blog/passwordReset.html")



def postpasswordreset(request):
    message1 = "Email link sent!"
    message2 = "No such email address is registered with Tutor Trade."
    email=request.POST.get('passResetEmail')
    try:
        authe.send_password_reset_email(email)
        return render(request, "blog/login.html", {"messg": message1})

    except:
        return render(request, "blog/login.html", {"messg": message2})



def login(request):
    return render(request, "blog/login.html", {'title': 'Login'})



def contact(request):
    message = "hide"
    try:
        idtoken = request.session['uid']
        return render(request, "blog/contact.html", {"title": "Contact"})

    except KeyError:
        return render(request, "blog/contact.html", {"messg": message})



def profile(request):
    message = "Please log in to access this feature."
    try:
        idtoken = request.session['uid']
        return render(request, "blog/profile.html", {"title": "Profile"})

    except KeyError:
        return render(request, "blog/login.html", {"messg": message})



def editProfile(request):
    message = "Please log in to access this feature."
    try:
        idtoken = request.session['uid']
        localID = authe.get_account_info(idtoken)['users'][0]['localId']
        storedFirstname = database.child('users').child(localID).child('details').child('name').get().val()
        return render(request, "blog/editProfile.html", {"headerName": storedFirstname})

    except KeyError:
        return render(request, "blog/login.html", {"messg": message})



def myProfile(request):
    message = "Please log in to access this feature."
    try:
        idtoken = request.session['uid']
        localID = authe.get_account_info(idtoken)['users'][0]['localId']

        storedFirstname = database.child('users').child(localID).child('details').child('name').get().val()
        storedLastname = database.child('users').child(localID).child('details').child('name2').get().val()
        storedContact = database.child('users').child(localID).child('details').child('contact').get().val()
        storedLocation = database.child('users').child(localID).child('details').child('location').get().val()
        storedCurMaj = database.child('users').child(localID).child('details').child('current_major').get().val()
        # storedHobbies = database.child('users').child(localID).child('details').child('Hobbies').get().val()

        List1 = [storedFirstname, storedLastname, storedContact, storedLocation, storedCurMaj]
        List2 = ["First Name:", "Last Name:", "Contact Info:", "Location:", "Current Major:"]
        return render(request, "blog/myProfile.html", {"detailList": List1, "headerName": storedFirstname, "labelList": List2})

    except KeyError:
        return render(request, "blog/login.html", {"messg": message})



# CC:added postsign which gets the email, and if information is entered correctly it will send you to -----------------------------
def postsign(request): #Changes made by JR in order to display name instead of email
    email=request.POST.get('email')
    passw = request.POST.get('pass')

    print(email)
    print(passw)
    try:
        user = authe.sign_in_with_email_and_password(email,passw)

    except:
        message = "invalid credentials"
        return render(request,"login.html",{"messg":message})

    session_id=user['idToken']
    request.session['uid']=str(session_id)
    idtoken = request.session['uid']
    #a = authe.get_account_info

    localID = authe.get_account_info(idtoken)['users'][0]['localId']
    name = database.child('users').child(localID).child('details').child('name').get().val()
    return render(request, "blog/knowledge.html",{"localID": localID, "e": name})


def postsignup(request):

    name=request.POST.get('name')
    name2=request.POST.get('name2')
    email=request.POST.get('email')
    passw=request.POST.get('pass')

    if(request.POST.get('contact') != ''):
        contact = request.POST.get('contact')
    else:
        contact = "contact"

    if(request.POST.get('current_major') != ''):
        current_major = request.POST.get('contact')
    else:
        current_major = "current major"

    if(request.POST.get('location') != ''):
        location = request.POST.get('location')
    else:
        location ="location"

    user=authe.create_user_with_email_and_password(email,passw)
    uid = user['localId']
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    idtoken = request.session['uid']
    localID = authe.get_account_info(idtoken)['users'][0]['localId']
    print(localID)

    data = {"name":name, "name2":name2, "email":email, "contact":contact, "current_major":current_major, "location":location ,"status":"1"}
    # to push the data into the database, 1 means account is enabled
    # from above name and email from form and enabled the account
    # database constructor with multiple users
    database.child("users").child(uid).child("details").set(data)
    return render(request,"knowledge.html", {"localID": localID, "e":name})

# CC: from print down --------------------------------------------------------------------------------------------------------------
def logout(request): #JR deletes session; if there is no session to delete, render login page regardless
    try:
        del request.session['uid']

    except KeyError:
        pass

    return render(request, 'login.html')


def knowledge_content(request):
    message = "Please log in to access this feature."

    try:
        idtoken = request.session['uid']
        localID = authe.get_account_info(idtoken)['users'][0]['localId']
        name = database.child('users').child(localID).child('details').child('name').get().val()
        return render(request, "blog/knowledge_content.html", {"e": name})

    except KeyError:
        return render(request, "blog/login.html", {"messg": message})

def knowledge_content_update(request):
    message = "Please log in to access this feature."

    try:
        idtoken = request.session['uid']
        localID = authe.get_account_info(idtoken)['users'][0]['localId']
        name = database.child('users').child(localID).child('details').child('name').get().val()
        return render(request, "blog/knowledge_content_update.html", {"e": name})

    except KeyError:
        return render(request, "blog/login.html", {"messg": message})



def postprofile(request):
    message = "Profile updated!"

    #JR: getting input from text fields from front end for use in conditional statements.

    name = request.POST.get("name1")
    name2 = request.POST.get("name2")
    contact = request.POST.get("contact")
    location = request.POST.get("location")
    current_major = request.POST.get("major")
    # hobbies = request.POST.get("hobbies")

    idtoken = request.session['uid']
    localID = authe.get_account_info(idtoken)['users'][0]['localId']

    #JR: Getting stored values from database and putting them into variables for use in conditional statements.
    storedFirstname = database.child('users').child(localID).child('details').child('name').get().val()
    storedLastname = database.child('users').child(localID).child('details').child('name2').get().val()
    storedContact = database.child('users').child(localID).child('details').child('contact').get().val()
    storedLocation = database.child('users').child(localID).child('details').child('location').get().val()
    storedCurMaj = database.child('users').child(localID).child('details').child('current_major').get().val()
    # storedHobbies = database.child('users').child(localID).child('details').child('Hobbies').get().val()

    #JR: Conditional statments that determine whether or not to update profile information.

    if(storedFirstname != name and name != ''):
        database.child('users').child(localID).child('details').child('name').set(name)
    if(storedLastname != name2 and name2 != ''):
        database.child('users').child(localID).child('details').child('name2').set(name2)
    if(storedContact != contact and contact != ''):
        database.child('users').child(localID).child('details').child('contact').set(contact)
    if(storedLocation != location and location != ''):
        database.child('users').child(localID).child('details').child('location').set(location)
    if(storedCurMaj != current_major and current_major != ''):
        database.child('users').child(localID).child('details').child('current_major').set(current_major)
    # if(storedHobbies != hobbies and hobbies != ''):
        # database.child('users').child(localID).child('details').child('Hobbies').set(hobbies)


    storedFirstname = database.child('users').child(localID).child('details').child('name').get().val()
    storedLastname = database.child('users').child(localID).child('details').child('name2').get().val()
    storedContact = database.child('users').child(localID).child('details').child('contact').get().val()
    storedLocation = database.child('users').child(localID).child('details').child('location').get().val()
    storedCurMaj = database.child('users').child(localID).child('details').child('current_major').get().val()
    # storedHobbies = database.child('users').child(localID).child('details').child('Hobbies').get().val()

    # List1 = [storedFirstname, storedLastname, storedContact, storedLocation, storedCurMaj, storedHobbies]
    # List2 = ["First Name:", "Last Name:", "Contact Info:", "Location:", "Current Major:", "Hobbies:"]
    List1 = [storedFirstname, storedLastname, storedContact, storedLocation, storedCurMaj]
    List2 = ["First Name:", "Last Name:", "Contact Info:", "Location:", "Current Major:"]

    return render(request, 'myProfile.html', {"messg": message, "detailList": List1, "labelList": List2, "headerName": storedFirstname})
