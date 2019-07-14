from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    AbstractBaseUser
    )

class User(AbstractBaseUser):
    email = models.EmailField()

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Need = models.CharField(max_length=100)
    Offering = models.CharField(max_length=100)
    Description = models.TextField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)


    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
