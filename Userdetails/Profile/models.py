from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_photo = models.ImageField('/profile')
   
    def __str__(self):
        return self.user.username
