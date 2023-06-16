from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from Auth.models import CustomerUser, Recipe, Like, SavedRecipe, Comment
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def index(request):
    recipe_id = request.POST.get('recipe_id')
    recipe = get_object_or_404(Recipe, id=recipe_id)
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
        'recipe': recipe,
        'heart_style': 'Active',
        'save_style': 'Active',
        'comments': Comment.objects.filter(recipe_id=recipe.id),
    }
    return render(request, 'Recipe/Recipe.html', context)

def add_comment(request):
    if request.method == 'POST':
        user = request.user
        recipe_id = request.POST.get('recipe_id')
        text = request.POST.get('comment_text')
        print(recipe_id)
        # Создание нового комментария
        comment = Comment.objects.create(user=user, text=text, recipe_id=recipe_id)

        # Возвращение данных комментария в JSON-ответе
        response_data = {
            'comment': {
                'id': comment.id,
                'user': comment.user.username,
                'text': comment.text,
                'created_at': comment.created_at.strftime('%d.%m.%Y'),  # Форматирование даты по вашему предпочтению
            },
            'user': {
                'username': user.username,
                'photo_url': user.photo.url,
            }
        }

        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request method.'})

