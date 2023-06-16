from django.shortcuts import render, redirect
from Auth.models import CustomerUser, Recipe, Like, SavedRecipe, Comment
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def index(request):
    recipes = Recipe.objects.filter(user=request.user)
    recipes_liked = Recipe.objects.filter(likes__user_id=request.user.id)
    recipes_saved = Recipe.objects.filter(saved_recipes__user_id=request.user.id)
    for recipe in recipes:
        recipe.likes_count = Like.objects.filter(recipe_id=recipe.id).count()
        recipe.saves_count = SavedRecipe.objects.filter(recipe_id=recipe.id).count()
        recipe.comments_count = Comment.objects.filter(recipe_id=recipe.id).count()
        if request.user.is_authenticated:
            recipe.is_liked = Like.objects.filter(recipe_id=recipe.id, user=request.user.id).exists()
            recipe.is_saved = SavedRecipe.objects.filter(recipe_id=recipe.id, user=request.user.id).exists()
        else:
            recipe.is_liked = Like.objects.filter(recipe_id=recipe.id).exists()
            recipe.is_saved = SavedRecipe.objects.filter(recipe_id=recipe.id).exists()

    context = {
        'recipes': recipes,
        'heart_style': 'Active',
        'save_style': 'Active',
        'recipe_count': recipes.count(),
        'saves_count': recipes_saved.count(),
        'likes_count': recipes_liked.count(),
    }
    return render(request, 'Profile/Profile.html', context)

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


def likes_user(request):
    liked_recipes = Recipe.objects.filter(likes__user_id=request.user.id)
    for recipe in liked_recipes:
        recipe.likes_count = Like.objects.filter(recipe_id=recipe.id).count()
        recipe.saves_count = SavedRecipe.objects.filter(recipe_id=recipe.id).count()
        recipe.is_liked = Like.objects.filter(recipe_id=recipe.id, user=request.user).exists()
        recipe.is_saved = SavedRecipe.objects.filter(recipe_id=recipe.id, user=request.user).exists()

    context = {
        'recipes': liked_recipes,
        'heart_style': 'Active',
        'save_style': 'Active',
    }

    return render(request, 'Profile/LikedRecipe.html', context)

def saves_user(request):
    saved_recipes = Recipe.objects.filter(saved_recipes__user_id=request.user.id)
    for recipe in saved_recipes:
        recipe.likes_count = Like.objects.filter(recipe_id=recipe.id).count()
        recipe.saves_count = SavedRecipe.objects.filter(recipe_id=recipe.id).count()
        recipe.is_liked = Like.objects.filter(recipe_id=recipe.id, user=request.user).exists()
        recipe.is_saved = SavedRecipe.objects.filter(recipe_id=recipe.id, user=request.user).exists()

    context = {
        'recipes': saved_recipes,
        'heart_style': 'Active',
        'save_style': 'Active',
    }
    return render(request, 'Profile/SavedRecipe.html', context)