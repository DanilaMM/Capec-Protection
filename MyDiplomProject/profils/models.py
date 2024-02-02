from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Расширяем базовую модель User"""
    mail = models.EmailField(unique=True, blank=True, null=True)
    number = models.CharField(max_length=12,blank=True, null=True)


class Projcets(models.Model):
    """Модель проектов"""
    is_wireless_tech = models.BooleanField()
    is_cloud_tech = models.BooleanField()
    is_virtual_tech = models.BooleanField()
    protection_class = models.CharField()

class R_person(models.Model):
    name = models.CharField()
    appointment = models.CharField()
