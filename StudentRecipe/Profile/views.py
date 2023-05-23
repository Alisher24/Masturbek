from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from globalUtils import HandleUploadedFile
# Create your views here.
def index(request):
    return render(request, 'Profile/Profile.html')