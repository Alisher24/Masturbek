from django.contrib.auth.models import User
from django.db import models

class CustomerUser(User):
    phone_number = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='user_photos', blank=True, null=True, default='C:\StudentRecipe\static\imgs\image 2.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="custom_user")
