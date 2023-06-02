from django.shortcuts import render,redirect
from Auth.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'Home/index.html', context)

def recipeCard(request):
    return render(request, 'Recipe/Recipe.html')