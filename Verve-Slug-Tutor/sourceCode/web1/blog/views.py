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

print(firebase);

#CC:  End of API ----------------------------------------------------------------------------------------------------------------

posts = [
    {
        'author': 'Brian Alegria',
        'title': 'Tutoring Post 1',
        'content': 'I need tutoring in advanced physics 8A and I am excellent web dev',
        'date_posted': 'June 30th, 2019'
    },
    {
        'author': 'Another User',
        'title': 'Tutoring Post 2',
        'content': 'Second Post Content',
        'date_posted': 'June 30th, 2019'
    }

]

def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def signup(request):
    return render(request, 'blog/signup.html', {'title': 'Signup'})

def knowledge(request):
    return render(request, 'blog/knowledge.html', {'title': 'Knowledge'})

def login(request):
    return render(request, "blog/login.html", {'title': 'Login'})

def contact(request):
    return render(request, "blog/contact.html", {'title': 'Contact'})

def profile(request):
    return render(request, 'blog/profile.html', {'title': 'Profile'})

def post(request):
    form = UserCreationForm()
    return render(request, 'blog/post_form.html', {'form': form})

class PostCreateView(CreateView):
    model = Post
    fields = ['Title', 'Need', 'Offering', 'Description']

# CC:added postsign which gets the email, and if information is entered correctly it will send you to -----------------------------
def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid credentials"
        return render(request,"knowledge.html",{"messg":message}) #login changed to knowledge so we dont get kicked out

    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)


    return render(request, "blog/knowledge.html",{"e":email})

def postsignup(request):

    name=request.POST.get('name')
    name2=request.POST.get('name2')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    passw=request.POST.get('pass')


    # data={
    #     "ID":id,
    #     "PW":pw,
    #     "FN":fname.lower(),
    #     "LN":lname.lower(),
    #     "EMAIL":email,
    #     "CONTACT":contact
    # }

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
