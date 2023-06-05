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
    saves.append('<p><b>0</b></p>');
    saves.append('<img src="/static/icons/save-instagram.png" alt="картинка лайка" class="Usuall">');
    saves.append('<img src="/static/icons/Active save-instagram.png" alt="картинка лайка" class="Active">');
    statistics.append(saves);

    var button = $('<a href="#" class="btn btn-primary">Перейти куда-нибудь</a>');
    cardBody.append(button);

    return card;
  }

  $('#category-select').change(function() {
    var selectedCategory = $(this).val();

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