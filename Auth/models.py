from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
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
    publication_date = models.DateField(default=date.today)
    def __str__(self):
        return self.title

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class SavedRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='saved_recipes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
