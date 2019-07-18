from django.shortcuts import render
import pyrebase # CC: imported pyrebase wrapper, essentially derives from firebase July 9, 2019
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (

    CreateView
    )
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

        return render(request, "blog/home.html", {"title": "Profile"})
    except KeyError:

        return render(request, "blog/home.html", {"messg": message})



def about(request):

        
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

    try:
        idtoken = request.session['uid']
        form = UserCreationForm()
        return render(request, 'blog/post_form.html', {'form': form})



        
    except KeyError:

        return render(request, "blog/about.html", {"messg": message})
    

def signup(request):
    
    return render(request, 'blog/signup.html', {'title': 'Signup'})


def post_form(request):
    message = "Please log in to access this feature."
    
    try:
        idtoken = request.session['uid']
        return render(request, 'blog/post_form.html', {'title': 'Post'})
        
    
    except KeyError:

        return render(request, "blog/login.html", {"messg": message})



def knowledge(request):
    message = "Please log in to access this feature."

    try:
        idtoken = request.session['uid']
        localID = authe.get_account_info(idtoken)['users'][0]['localId']
        name = database.child('users').child(localID).child('details').child('name').get().val()
        return render(request, "blog/knowledge.html", {"e": name})

    except KeyError:

        return render(request, "blog/login.html", {"messg": message})



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

# CC:added postsign which gets the email, and if information is entered correctly it will send you to -----------------------------
def postsign(request): #Changes made by JR in order to display name instead of email
    email=request.POST.get('email')
    passw = request.POST.get('pass')

    print("email")
    print("passw")
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid credentials"
        return render(request,"login.html",{"messg":message})

    #print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    idtoken = request.session['uid']
    #a = authe.get_account_info

    localID = authe.get_account_info(idtoken)['users'][0]['localId']
    name = database.child('users').child(localID).child('details').child('name').get().val()
    return render(request, "blog/knowledge.html",{"e": name})

def postsignup(request):

    name=request.POST.get('name')
    name2=request.POST.get('name2')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    passw=request.POST.get('pass')

    user=authe.create_user_with_email_and_password(email,passw)
    # CC: Here we create account

    uid = user['localId']
    # CC unique ID for the user

    data = {"name":name, "lastname":name2, "email":email, "contact":contact, "status":"1"}
    # to push the data into the database, 1 means account is enabled
    # from above name and email from form and enabled the account
    # database constructor with multiple users
    database.child("users").child(uid).child("details").set(data)
    return render(request,"knowledge.html")

# CC: from print down --------------------------------------------------------------------------------------------------------------
def logout(request): #JR deletes session; if there is no session to delete, render login page regardless
    try:
        del request.session['uid']

    except KeyError:
        pass
eturn render(request, 'login.html')


class PostCreateView(CreateView):
    model = Post
    fields = ['Title', 'Need', 'Offering', 'Description']

  