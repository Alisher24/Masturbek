from django.db import models


class Users(models.Model):
    login = models.CharField(max_length=128, blank=False, null=False)
    password = models.CharField(max_length=24, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    name = models.CharField(max_length=128, blank=True, null=True)
    photo = models.ImageField(upload_to="users/img/")
    address = models.CharField(max_length=128, blank=True, null=True, default=None)
    telephone = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_blocked = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)