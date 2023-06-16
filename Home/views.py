from django.db.models import Count
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from Auth.models import Recipe, Like, SavedRecipe, Comment
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
# @cache_page(60 * 5)
def index(request):
    recipes = Recipe.objects.annotate(likes_count=Count('likes')).order_by('-likes_count')

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
        'heart_style': 'Active',  # Здесь укажите нужный стиль (например, 'Active' или 'Usuall')
        'save_style': 'Active',
    }
    return render(request, 'Home/index.html', context)

def ajax_recipes_view(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        selected_category = request.GET.get('category')
        if selected_category == 'all':
            recipes = Recipe.objects.annotate(likes_count=Count('likes')).order_by('-likes_count')
        else:
            recipes = Recipe.objects.filter(category=selected_category)
        if not recipes:
            recipes = Recipe.objects.all()
        print(selected_category)

        serialized_recipes = []
        for recipe in recipes:
            recipe.likes_count = Like.objects.filter(recipe_id=recipe.id).count()
            recipe.saves_count = SavedRecipe.objects.filter(recipe_id=recipe.id).count()
            if request.user.is_authenticated:
                recipe.is_liked = Like.objects.filter(recipe_id=recipe.id, user=request.user.id).exists()
                recipe.is_saved = SavedRecipe.objects.filter(recipe_id=recipe.id, user=request.user.id).exists()
            else:
                recipe.is_liked = Like.objects.filter(recipe_id=recipe.id).exists()
                recipe.is_saved = SavedRecipe.objects.filter(recipe_id=recipe.id).exists()

            serialized_recipe = {
                'id': recipe.id,
                'title': recipe.title,
                'category': recipe.category,
                'photo_url': recipe.photo.url,
                'likes_count': recipe.likes_count,
                'saves_count': recipe.saves_count,
                'is_liked': recipe.is_liked,
                'is_saved': recipe.is_saved,
                'csrf_token': get_token(request),
            }
            serialized_recipes.append(serialized_recipe)
        print(serialized_recipe.values())
        return JsonResponse({'data': serialized_recipes})

    else:
        return JsonResponse({'error': 'Invalid request'})


# def recipe_list(request):
#     recipes = Recipe.objects.all()
#
#     for recipe in recipes:
#         recipe.likes_count = Like.objects.filter(recipe_id=recipe.id).count()
#         recipe.saves_count = SavedRecipe.objects.filter(recipe_id=recipe.id).count()
#         recipe.comments_count = Comment.objects.filter(recipe_id=recipe.id).count()
#         if request.user.is_authenticated:
#             recipe.is_liked = Like.objects.filter(recipe_id=recipe.id, user=request.user.id).exists()
#             recipe.is_saved = SavedRecipe.objects.filter(recipe_id=recipe.id, user=request.user.id).exists()
#         else:
#             recipe.is_liked = Like.objects.filter(recipe_id=recipe.id).exists()
#             recipe.is_saved = SavedRecipe.objects.filter(recipe_id=recipe.id).exists()
#
#     context = {
#         'recipes': recipes,
#         'heart_style': 'Active',  # Здесь укажите нужный стиль (например, 'Active' или 'Usuall')
#         'save_style': 'Active',
#     }
#     return render(request, 'Home/index.html', context)
def handle_action(request, model_class, count_field, is_field):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        recipe_id = request.POST.get('recipe_id')
        user = request.user  # Получаем текущего пользователя

        # Проверяем, существует ли запись для данного пользователя и рецепта
        action_exists = model_class.objects.filter(recipe_id=recipe_id, user=user).exists()

        if action_exists:
            # Запись уже существует - удаляем ее
            model_class.objects.filter(recipe_id=recipe_id, user=user).delete()
            count = model_class.objects.filter(recipe_id=recipe_id).count()
            is_action = False
        else:
            # Записи нет - создаем новую
            action = model_class(recipe_id=recipe_id, user=user)
            action.save()
            count = model_class.objects.filter(recipe_id=recipe_id).count()
            is_action = True

        return JsonResponse({'success': True, count_field: count, is_field: is_action})
    else:
        return JsonResponse({'error': 'Invalid request'})

def like_recipe(request):
    return handle_action(request, Like, 'likes_count', 'is_liked')

def save_recipe(request):
    return handle_action(request, SavedRecipe, 'saves_count', 'is_saved')

