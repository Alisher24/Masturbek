from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import Profile
from .models import CustomerUser

def index(request):
    if request.method == "POST":
        if 'signin_button' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Перенаправление на страницу профиля
            else:
                return HttpResponse("Неверные учетные данные")

        elif 'register_button' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            first_name = request.POST['first_name']
            password2 = request.POST['repeat_password']
            if password == password2:
                # Создаем нового пользователя
                user = CustomerUser.objects.create_user(username=username, password=password, email=email, first_name=first_name)
                user.save()
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, "Пароли не совпадают")

    return render(request, 'Auth/login.html')

@login_required
def profile(request):
    user = request.user  # Получение текущего пользователя
    context = {
        'user': user,
    }
    return Profile.views.index(request)

def logout_view(request):
    logout(request)
    return redirect('home')