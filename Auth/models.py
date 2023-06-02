from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class CustomerUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='user_photos', blank=True, null=True, default='alisher.jpg')
    recipes = models.ManyToManyField('Recipe', related_name='users')
    def __str__(self):
        return self.username

User = get_user_model()

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='recipe_photos', blank=True, null=True)
    def __str__(self):
        return self.title