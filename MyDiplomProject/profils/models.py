from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    mail = models.EmailField(unique=True, blank=True, null=True)
    number = models.CharField(max_length=12,blank=True, null=True)
