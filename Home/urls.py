from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ajax/recipes/', views.ajax_recipes_view, name='ajax_recipes'),
    path('like-recipe/', views.like_recipe, name='like_recipe'),
    path('recipe/', views.recipe_redirect, name='recipe'),
]
