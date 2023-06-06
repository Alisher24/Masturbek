from django.shortcuts import render, redirect
from Auth.models import CustomerUser, Recipe, Like
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def index(request):

    return render(request, 'Recipe/Recipe.html')

