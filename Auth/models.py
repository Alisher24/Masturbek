from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomerUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='user_photos', blank=True, null=True, default='alisher.jpg')

    def __str__(self):
        return self.username