from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('signup/', views.signup, name='blog-login'),
    path('signup/', views.signup, name='blog-signup'),
]
