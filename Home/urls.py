from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ajax/recipes/', views.ajax_recipes_view, name='ajax_recipes'),
    path('recipe/', views.recipeCard, name = 'recipeCard'),
]