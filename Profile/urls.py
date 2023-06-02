from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('saved/', views.savedRecipes)
]