from django.shortcuts import render

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

def login(request):
    return render(request, 'blog/login.html', {'title': 'Login'})

def signup(request):
    return render(request, 'blog/signup.html', {'title': 'Signup'})
<<<<<<< HEAD
=======

def knowledge(request):
    return render(request, 'blog/knowledge.html', {'title': 'Knowledge'})


>>>>>>> 3ce55acb55acd8e5597a28d03090589ddfdc31ae
