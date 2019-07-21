from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import(
    PostCreateView
    )

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('login/', views.login, name='blog-login'),  #the href links in the html pages are using the "names" here to link themselves with these url patterns which are of course calling functions from the Views.py file
    path('knowledge/', views.knowledge, name='blog-knowledge'),
    path('knowledge_content/',views.knowledge_content, name='blog-knowledge_content'),
    path('knowledge_content/update',views.knowledge_content_update, name='blog-knowledge_content_update'),
    path('signup/',views.signup, name='blog-signup'),
    path('postsignup/',views.postsignup, name='blog-postsignup'),
    path('contact/',views.contact, name='blog-contact'),
    path('profile/',views.profile, name='blog-profile'),
    path('postsign/', views.postsign),
    path('post/', PostCreateView.as_view(), name='blog-post_form'),
    path('logout/', views.logout, name="blog-logout"),

    path('editProfile/',views.editProfile, name='blog-editProfile'),
    path('myProfile/', views.myProfile, name='blog-myProfile'),
    path('postprofile/', views.postprofile, name='blog-postprofile'),
    path('passwordReset/', views.passwordReset, name='blog-passwordReset'),
    path('postpasswordreset/', views.postpasswordreset),
]



# CC note: you will not be able to access the knowledge board page unless you login. You may add
#      yourself manually from Verve-Slug-Tutor firebase console under the authentication tab to gain entrance!
