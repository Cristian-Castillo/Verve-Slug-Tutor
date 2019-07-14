from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Need = models.CharField(max_length=100)
    Offering = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)


    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
