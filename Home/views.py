from django.shortcuts import render,redirect


def index(request):
    return render(request, 'Home/index.html')

def recipeCard(request):
    return render(request, 'Recipe/Recipe.html')