from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import Profile
from .models import CustomerUser
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
    print(111)
    if request.method == "POST":
        print(222)
        if 'login_button' in request.POST:
            print(333)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Перенаправление на страницу профиля
            else:
                return HttpResponseBadRequest("Неверные учетные данные")

        elif 'register_button' in request.POST:
            print(444)
            username = request.POST['username_register']
            password = request.POST['password_first']
            email = request.POST['email']
            first_name = request.POST['first_name']
            password2 = request.POST['repeat_password']
            if not username or not password or not email or not first_name or not password2:
                return HttpResponseBadRequest('Пожалуйста, заполните все поля')
            if CustomerUser.objects.filter(username=username).exists():
                return HttpResponseBadRequest('Пользователь с таким именем уже существует')
            elif CustomerUser.objects.filter(email=email).exists():
                return HttpResponseBadRequest('Пользователь с такой электронной почтой уже существует')
            if password == password2:
                # Создаем нового пользователя
                user = CustomerUser.objects.create_user(username=username, password=password, email=email,
                                                        first_name=first_name)
                user.save()
                login(request, user)
                return JsonResponse({'success': True})  # Возвращаем успешный JSON-ответ
            else:
                return HttpResponseBadRequest('Пароли не совпадают')

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
