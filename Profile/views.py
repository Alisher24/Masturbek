from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from globalUtils import HandleUploadedFile
# Create your views here.
def index(request):
    return render(request, 'Profile/Profile.html')


def edit_profile(request):
    if request.method == 'POST':
        edit_name = request.POST.get('edit_name')
        edit_phone = request.POST.get('edit_phone')
        edit_email = request.POST.get('edit_email')

        # Обновление данных пользователя в базе данных
        user = request.user
        user.first_name = edit_name
        user.phone_number = edit_phone
        user.email = edit_email
        user.save()

        return redirect('profile')  # Перенаправление на страницу профиля

    return render(request, 'Profile/Profile.html')
