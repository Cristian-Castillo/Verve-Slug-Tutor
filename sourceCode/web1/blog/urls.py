from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('login/', views.login, name='blog-login'),
    path('knowledge/', views.knowledge, name='blog-knowledge'),
    path('signup/',views.signup, name='blog-signup'),
    path('contact/',views.contact, name='blog-contact'),
    path('profile/',views.profile, name='blog-profile'),
    path('logout/',views.logout, name='blog-logout')
]


# CC note: you will not be able to access the knowledge board page unless you login. You may add
#      yourself manually from Verve-Slug-Tutor firebase console under the authentication tab to gain entrance!
