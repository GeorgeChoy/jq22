 $(function() {
    $( "#slider" ).slider(
        {
            value: $('#id_likes').val(),    // set value when updating
            change: function( event, ui ) {
                $('#id_likes').val(ui.value);
                $("#label").html(labelArr[ui.value]);
            }
        }
        );
 });