from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



class UserModel(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
    