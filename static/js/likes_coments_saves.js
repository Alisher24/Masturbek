$(document).ready(function() {
  $('.like-image').on('click', function() {
    var $likeImage = $(this);
    var recipeId = $likeImage.data('recipe-id');
    var csrftoken = getCookie('csrftoken');

    $.ajax({
      url: '/like-recipe/',
      type: 'POST',
      data: {
        'recipe_id': recipeId,
        'csrfmiddlewaretoken': csrftoken
      },
      dataType: 'json',
      success: function(response) {
        if (response.success) {
          var likesCount = response.likes_count;
          $likeImage.siblings('p').find('b').text(likesCount);

          var isLiked = response.is_liked;
          if (isLiked) {
            $likeImage.attr('src', '/static/icons/Active heart.png');
            $likeImage.addClass('Active').removeClass('Usuall');
          } else {
            $likeImage.attr('src', '/static/icons/heart.png');
            $likeImage.addClass('Usuall').removeClass('Active');
          }
        }
      },
      error: function(xhr, textStatus, errorThrown) {
        console.log('Error: ' + errorThrown);
      }
    });
  });

  $('.save-image').on('click', function() {
    console.log(11111111111)
    var $saveImage = $(this);
    var recipeId = $saveImage.data('recipe-id');
    var csrftoken = getCookie('csrftoken');

    $.ajax({
      url: '/save-recipe/',
      type: 'POST',
      data: {
        'recipe_id': recipeId,
        'csrfmiddlewaretoken': csrftoken
      },
      dataType: 'json',
      success: function(response) {
        if (response.success) {
          var savesCount = response.saves_count;
          $saveImage.siblings('p').find('b').text(savesCount);

          var isSaved = response.is_saved;
          if (isSaved) {
            $saveImage.attr('src', '/static/icons/Active save-instagram.png');
            $saveImage.addClass('Active').removeClass('Usuall');
          } else {
            $saveImage.attr('src', '/static/icons/save-instagram.png');
            $saveImage.addClass('Usuall').removeClass('Active');
          }
        }
      },
      error: function(xhr, textStatus, errorThrown) {
        console.log('Error: ' + errorThrown);
      }
    });
  });

  $(document).ready(function() {
    // Обработчик отправки формы комментария
    $('#commentForm').submit(function(event) {
      event.preventDefault(); // Отменить стандартное поведение формы

      var form = $(this);
      var formData = form.serialize(); // Сериализовать данные формы
      var recipeId = form.data('recipe_id'); // Получить recipe_id из атрибута data
      var commentText = form.find('input[name="userText"]').val();
      console.log(recipeId, commentText)
      // Добавить recipe_id в данные формы
      formData += '&recipe_id=' + recipeId;
      formData += '&comment_text=' + commentText;

      // Отправить AJAX-запрос
      $.ajax({
        url: '/add_comment/',
        type: 'POST',
        data: formData,
        success: function(response) {
          // Обработать успешный ответ от сервера
          var comment = response.comment;
          var user = response.user;
          console.log(user)

          // Создать новый HTML-элемент для комментария
          var newComment = `
            <div class="Coments_Coment" data-comment-id="${comment.id}">
              <img src="${user.photo_url}" alt="аватарка">
              <div class="Coments_UserTextBlock">
                <p><b>${comment.user}</b></p>
                <p class="ComentText">${comment.text}</p>
                <p class="ComentData">${comment.created_at}</p>
              </div>
            </div>
          `;

          // Добавить новый комментарий к списку комментариев
          $('#commentsList').append(newComment);

          // Сбросить значения формы
          form.trigger('reset');
        },
        error: function(xhr, errmsg, err) {
          // Обработать ошибку
          console.log(errmsg);
        }
      });
    });
  });

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});