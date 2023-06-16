from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ajax/recipes/', views.ajax_recipes_view, name='ajax_recipes'),
    path('like-recipe/', views.like_recipe, name='like_recipe'),
    path('save-recipe/', views.save_recipe, name='save_recipe'),
    path('', include('Recipe.urls'), name='recipe'),
]
