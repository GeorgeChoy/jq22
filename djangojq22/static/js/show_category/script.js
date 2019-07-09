$('#likes').click(function(){
    var categoryid;
    categoryid=$(this).attr('data-categoryid');
    $.get('/djangojq22/category_like/',{category_pk:categoryid},
    function(data){
      $('#like_count').html(data);
        $('likes').hide()
    }
    );
});

