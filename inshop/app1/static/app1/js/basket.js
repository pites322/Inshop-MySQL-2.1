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
    var toDellList = [];
    $('.deleteCheckbox').click(function(){
        var id = $(this).data('id')
        if ($('#deleteCheckbox'+id).is(':checked')){
            toDellList.push(id)
            console.log(toDellList)
        } else {
            for (i=0; i < toDellList.length; i++){
                if (toDellList[i] == id){
                    toDellList[i]=''
                    console.log(toDellList)
                }else{}
            };
        }
    });
    $('.deleteBut').click(function(){
        var userId = $(this).data('userid')
        var url = '/basketdell/';
        var data = {
            'list': toDellList,
            'userId': userId
        };
        var isCheckedEny = 'No';
    for (i=0; i<toDellList.length; i++){
        if (toDellList[i] != ''){
            isCheckedEny = 'Yes';
            break;
        };
    };
    if (isCheckedEny == 'Yes'){
        $.ajax({url: url,
            data: data,
            type: 'DELETE',
            success: function(){
                location.reload();
            }
        });
    };
    });
})