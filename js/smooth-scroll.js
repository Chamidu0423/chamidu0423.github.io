$(document).ready(function(){
    $('a[data-scroll]').on('click', function(e){
        e.preventDefault();
        var target = $(this).data('scroll');
        $('html, body').animate({
            scrollTop: $('#' + target).offset().top
        }, 1000);
    });
});

$('#goToTopBtn').on('click', function(e){
    e.preventDefault();
    $('html, body').animate({
        scrollTop: 0
    }, 1000);
});
