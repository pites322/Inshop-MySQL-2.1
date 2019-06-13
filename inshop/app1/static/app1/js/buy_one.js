$(document).ready(function(){
    $.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
    });
    $('.deleteButton').click(function(){
        var id = $(this).data('id');
        var url = '/basketdell/';
        var data = {
            'pk': id
        };
        $.ajax({url: url,
            data: data,
            type: 'DELETE',
            success: function(){
                window.location.replace('/account/basket');
            }
        });
    });
});