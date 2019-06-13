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
    $('.addButton').click(function(){
        var prodPk = $(this).data('prodpk');
        var buyerPk = $(this).data('buyerid');
        var price = $(this).data('price');
        var url = '/basketdell/';
        var data = {
            'prod_id': prodPk,
            'buyer_id': buyerPk
        };
        $.ajax({url: url,
            data: data,
            type: 'POST',
            success: function(){
                var basketState = $('.basketState').text();
                basketState = parseFloat(basketState) + parseFloat(price);
                $('.basketState').text(basketState.toFixed(2));
            }
        });
    });
});