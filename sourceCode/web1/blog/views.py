from django.shortcuts import render
import pyrebase # CC: imported pyrebase wrapper, essentially derives from firebase July 9, 2019
from django.contrib import auth

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

#CC:  End of API ----------------------------------------------------------------------------------------------------------------

posts = [
    {
        'author': 'Brian Alegria',
        'title': 'Tutoring Post 1',
        'content': 'I need tutoring in advanced physica 8A and I am excellent web dev',
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
    context = {
    'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def signup(request):
    return render(request, 'blog/signup.html', {'title': 'Signup'})

def knowledge(request):
    return render(request, 'blog/knowledge.html', {'title': 'Knowledge'})

def login(request):
    return render(request, "blog/login.html", {'title': 'Login'})

# CC:added postsign which gets the email, and if information is entered correctly it will send you to -----------------------------
def postsign(request): 
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid credentials"
        return render(request,"login.html",{"messg":message})

    print(user['idToken']) 
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request, "blog/knowledge.html",{"e":email})
# CC: from print down --------------------------------------------------------------------------------------------------------------



