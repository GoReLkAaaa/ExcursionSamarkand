$(document).ready(function () {
    const $scrollToTopButton = $('#scrollToTop');


    $(window).on('scroll', function () {
        if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
            $scrollToTopButton.addClass('show');
        } else {
            $scrollToTopButton.removeClass('show');
        }
    });


    $scrollToTopButton.on('click', function () {
        $('html, body').animate({ scrollTop: 0 }, 800);
    });
});


$(document).ready(function() {
    $('a[href^="#"]').click(function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top
        }, 600);
    });
});
