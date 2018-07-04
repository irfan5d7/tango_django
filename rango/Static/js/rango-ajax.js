$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/like_category/', {category_id: catid}, function(data){
    $('#like_count').html(data);
    $('#likes').hide();
    });
});

$('#suggestion').keyup(function(){
var query;
query = $(this).val();
$.get('/suggest/', {suggestion: query}, function(data){
$('#cats').html(data);
});
});