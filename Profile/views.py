from django.shortcuts import render, redirect
from Auth.models import CustomerUser
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def index(request):
    return render(request, 'Profile/Profile.html')

def edit_profile(request):
    if request.method == 'POST':
        edit_name = request.POST.get('edit_name')
        edit_phone = request.POST.get('edit_phone')
        edit_email = request.POST.get('edit_email')
        edit_photo = request.FILES.get('edit_photo')

        # Обновление данных пользователя в базе данных
        user = request.user
        try:
            customer_user = CustomerUser.objects.get(pk=user.pk)
        except CustomerUser.DoesNotExist:
            customer_user = CustomerUser(user=user)

        customer_user.first_name = edit_name
        customer_user.phone_number = edit_phone
        customer_user.email = edit_email

        # Сохранение нового фото, если оно было выбрано
        if edit_photo:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            filename = fs.save(edit_photo.name, edit_photo)
            customer_user.photo = fs.url(filename).lstrip('/').lstrip('media/')
        else:
            # Если новое фото не было выбрано, сохраняем прежнее фото
            customer_user.photo = user.photo

        customer_user.save()

        return redirect('profile')  # Перенаправление на страницу профиля

    return render(request, 'Profile/Profile.html')
