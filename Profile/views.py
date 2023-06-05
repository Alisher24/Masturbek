from django.shortcuts import render, redirect
from Auth.models import CustomerUser, Recipe, Like
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def index(request):
    recipes = Recipe.objects.filter(user=request.user)
    for recipe in recipes:
        recipe.likes_count = Like.objects.filter(recipe_id=recipe.id).count()
        recipe.is_liked = Like.objects.filter(recipe_id=recipe.id, user=request.user).exists()

    context = {
        'recipes': recipes,
        'heart_style': 'Active'  # Здесь укажите нужный стиль (например, 'Active' или 'Usuall')
    }
    return render(request, 'Profile/Profile.html', context)

def savedRecipes(request):
    return render(request, 'Profile/SavedRecipe.html')
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

def create_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        photo = request.FILES.get('photo')

        recipe = Recipe(user=request.user, title=title, description=description, category=category)
        if photo:
            recipe.photo = photo
        recipe.save()

        return redirect('profile')  # Перенаправление на страницу профиля

    return render(request, 'Profile/Profile.html')