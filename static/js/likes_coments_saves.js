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