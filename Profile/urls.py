from django.urls import path, include

import Home
from . import views
urlpatterns = [
    path('', views.index),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('recipe/', Home.views.recipe_redirect, name='recipe'),
    path('saved/', views.savedRecipes)
]