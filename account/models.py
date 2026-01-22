from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserManager

class User(AbstractBaseUser):

    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email