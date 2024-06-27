from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    organization = models.CharField(max_length=255, blank=True, verbose_name='Организация')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
