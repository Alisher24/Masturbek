from django.shortcuts import render,redirect
from Auth.models import Recipe
from django.http import JsonResponse


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
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
            serialized_recipe = {
                'photo_url': recipe.photo.url,  # Включаем URL-адрес изображения
                'title': recipe.title,
                'category': recipe.category,
            }
            serialized_recipes.append(serialized_recipe)
        print(serialized_recipe.values())
        return JsonResponse({'data': serialized_recipes})

        # return JsonResponse({'data': list(recipes)}, safe=False)  # Возвращаем данные в формате JSON
    else:
        return JsonResponse({'error': 'Invalid request'})

def recipeCard(request):
    return render(request, 'Recipe/Recipe.html')
