from django.shortcuts import render, redirect
from Auth.models import CustomerUser

def index(request):
    return render(request, 'Profile/Profile.html')

def edit_profile(request):
    if request.method == 'POST':
        edit_name = request.POST.get('edit_name')
        edit_phone = request.POST.get('edit_phone')
        edit_email = request.POST.get('edit_email')

        # Обновление данных пользователя в базе данных
        user = request.user
        try:
            customer_user = CustomerUser.objects.get(pk=user.pk)
        except CustomerUser.DoesNotExist:
            customer_user = CustomerUser(user=user)

        customer_user.first_name = edit_name
        customer_user.phone_number = edit_phone
        customer_user.email = edit_email
        customer_user.save()

        return redirect('profile')  # Перенаправление на страницу профиля

    return render(request, 'Profile/Profile.html')