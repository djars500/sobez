from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):    
    name = models.CharField('Аты',max_length=255, )
    surName = models.CharField('Тегі', max_length=255,)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=255)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        if self.username == 'Демеуші':
            return f"{self.username}: {self.surName} {self.name}"
        else: 
            return self.username
            