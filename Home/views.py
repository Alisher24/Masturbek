from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from Auth.models import Recipe
from django.http import JsonResponse
from Auth.models import Like

def index(request):
    recipes = Recipe.objects.all()

    for recipe in recipes:
        recipe.likes_count = Like.objects.filter(recipe_id=recipe.id).count()
        if request.user.is_authenticated:
            recipe.is_liked = Like.objects.filter(recipe_id=recipe.id, user=request.user.id).exists()
        else: recipe.is_liked = Like.objects.filter(recipe_id=recipe.id).exists()

    context = {
        'recipes': recipes,
        'heart_style': 'Active'  # Здесь укажите нужный стиль (например, 'Active' или 'Usuall')
    }
    return render(request, 'Home/index.html', context)

def ajax_recipes_view(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        selected_category = request.GET.get('category')
        if selected_category == 'all':
            recipes = Recipe.objects.all()
        else:
            recipes = Recipe.objects.filter(category=selected_category)
        if not recipes:
            recipes = Recipe.objects.all()
        print(selected_category)

        serialized_recipes = []
        for recipe in recipes:
            recipe.likes_count = Like.objects.filter(recipe_id=recipe.id).count()
            if request.user.is_authenticated:
                recipe.is_liked = Like.objects.filter(recipe_id=recipe.id, user=request.user.id).exists()
            else:
                recipe.is_liked = Like.objects.filter(recipe_id=recipe.id).exists()

            serialized_recipe = {
                'id': recipe.id,
                'title': recipe.title,
                'category': recipe.category,
                'photo_url': recipe.photo.url,
                'likes_count': recipe.likes_count,
                'is_liked': recipe.is_liked,
            }
            serialized_recipes.append(serialized_recipe)
        print(serialized_recipe.values())
        return JsonResponse({'data': serialized_recipes})

    else:
        return JsonResponse({'error': 'Invalid request'})


def recipe_list(request):
    recipes = Recipe.objects.all()

    for recipe in recipes:
        recipe.likes_count = recipe.like_set.count()  # Получаем количество лайков для каждого рецепта

    context = {'recipes': recipes}
    return render(request, 'Home/index.html', context)
def like_recipe(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        recipe_id = request.POST.get('recipe_id')
        user = request.user  # Получаем текущего пользователя

        # Проверяем, существует ли лайк для данного пользователя и рецепта
        like_exists = Like.objects.filter(recipe_id=recipe_id, user=user).exists()

        if like_exists:
            # Лайк уже существует - удаляем его
            Like.objects.filter(recipe_id=recipe_id, user=user).delete()
            likes_count = Like.objects.filter(recipe_id=recipe_id).count()
            is_liked = False
        else:
            # Лайка нет - создаем новый
            like = Like(recipe_id=recipe_id, user=user)
            like.save()
            likes_count = Like.objects.filter(recipe_id=recipe_id).count()
            is_liked = True

        return JsonResponse({'success': True, 'likes_count': likes_count, 'is_liked': is_liked})
    else:
        return JsonResponse({'error': 'Invalid request'})

@csrf_exempt
def recipe_redirect(request):
    recipe_id = request.POST.get('recipe_id')
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.likes_count = Like.objects.filter(recipe_id=recipe.id).count()
    if request.user.is_authenticated:
        recipe.is_liked = Like.objects.filter(recipe_id=recipe.id, user=request.user.id).exists()
    else:
        recipe.is_liked = Like.objects.filter(recipe_id=recipe.id).exists()
    context = {
        'recipe': recipe,
        'heart_style': 'Active'  # Здесь укажите нужный стиль (например, 'Active' или 'Usuall')
    }
    return render(request, 'Recipe/Recipe.html', context)


