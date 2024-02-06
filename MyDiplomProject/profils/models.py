from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class User(AbstractUser):
    """Расширяем базовую модель User"""
    mail = models.EmailField(unique=True, blank=True, null=True)
    number = models.CharField(max_length=12,blank=True, null=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class Projcets(models.Model):
    """Модель проектов"""
    is_wireless_tech = models.BooleanField()
    is_cloud_tech = models.BooleanField()
    is_virtual_tech = models.BooleanField()
    protection_class = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
class R_person(models.Model):
    name = models.CharField(max_length=255)
    appointment = models.CharField(max_length=255)
