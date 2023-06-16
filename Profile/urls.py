from django.urls import path, include

import Recipe
from . import views
urlpatterns = [
    path('', views.index),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('', Recipe.views.index, name='recipe'),
    path('saves/', views.saves_user, name='saves_user'),
    path('likes/', views.likes_user, name='likes_user'),
]