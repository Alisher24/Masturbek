
$(document).ready(function() {
  function createRecipeCard(recipe) {
    var card = $('<div class="card" style="width: 18rem;">');
    var cardImg = $('<img>').addClass('card-img-top').attr('src', recipe.photo_url).attr('alt', 'картинка еды');
    card.append(cardImg);

    var cardBody = $('<div class="card-body">');
    card.append(cardBody);

    var title = $('<h5>').addClass('card-title').text(recipe.title);
    cardBody.append(title);

    var category = $('<p>').addClass('card-text').text(recipe.category);
    cardBody.append(category);

    var statistics = $('<div class="RecipeBlock_ShortInfo_Statistics">');
    cardBody.append(statistics);

    var likes = $('<div class="RecipeBlock_ShortInfo_Statistics_Likes">');
    likes.append('<p><b>' + recipe.likes_count + '</b></p>');

    var likeImage = $('<img>').addClass('like-image').attr('src', recipe.is_liked ? '/static/icons/Active heart.png' : '/static/icons/heart.png');
    likeImage.attr('alt', 'картинка лайка');
    likeImage.addClass(recipe.is_liked ? 'Active' : 'Usuall');
    likeImage.attr('data-recipe-id', recipe.id);
    likes.append(likeImage);

    statistics.append(likes);

    var comments = $('<div class="RecipeBlock_ShortInfo_Statistics_Comments">');
    comments.append('<p><b>1</b></p>');
    comments.append('<img src="/static/icons/speech-bubble.png" alt="картинка комментариев">');
    statistics.append(comments);

    var saves = $('<div class="RecipeBlock_ShortInfo_Statistics_Saves">');
    saves.append('<p><b>' + recipe.saves_count + '</b></p>');

    var saveImage = $('<img>').addClass('save-image').attr('src', recipe.is_saved ? '/static/icons/Active save-instagram.png' : '/static/icons/save-instagram.png');
    saveImage.attr('alt', 'картинка сохранения');
    saveImage.addClass(recipe.is_saved ? 'Active' : 'Usuall');
    saveImage.attr('data-recipe-id', recipe.id);
    saves.append(saveImage);

    statistics.append(saves);

    var form = $('<form method="post" action="/recipe/">');
    form.append('<input type="hidden" name="csrfmiddlewaretoken" value="' + recipe.csrf_token + '">');
    form.append('<input type="hidden" name="recipe_id" value="' + recipe.id + '">');
    var button = $('<button type="submit" class="btn btn-primary">Перейти куда-нибудь</button>');
    form.append(button);
    cardBody.append(form);

    return card;
  }

  $('#category-select').change(function() {
    var selectedCategory = $(this).val();
    var categoryTitle = $('#category-title');

    categoryTitle.text(selectedCategory);

    $.ajax({
      url: '/ajax/recipes/',
      type: 'GET',
      data: { category: selectedCategory },
      dataType: 'json',
      success: function(response) {
        var recipeContainer = $('#recipe-container');
        recipeContainer.empty();

        $.each(response.data, function(index, recipe) {
          var card = createRecipeCard(recipe); // Используйте функцию createRecipeCard для создания карточки рецепта
          recipeContainer.append(card);
        });
      },
      error: function(xhr, errmsg, err) {
        console.log('Ошибка при получении рецептов');
      }
    });
  });
});

