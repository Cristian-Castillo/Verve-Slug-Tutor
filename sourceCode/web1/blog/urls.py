from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('login/', views.login, name='blog-login'),
    path('signup/', views.signup, name='blog-signup'),
<<<<<<< HEAD
=======
    path('knowledge/', views.knowledge, name='blog-knowledge'),
>>>>>>> 3ce55acb55acd8e5597a28d03090589ddfdc31ae
]
