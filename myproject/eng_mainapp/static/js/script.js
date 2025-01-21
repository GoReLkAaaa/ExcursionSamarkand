let next = document.querySelector('.next')
let prev = document.querySelector('.prev')

next.addEventListener('click', function(){
    let items = document.querySelectorAll('.item')
    document.querySelector('.slide').appendChild(items[1])
})

prev.addEventListener('click', function(){
    let items = document.querySelectorAll('.item')
    document.querySelector('.slide').prepend(items[items.length - 1]) // here the length of items = 6
})

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}

$(document).ready(function() {
    $('a[href^="#"]').click(function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top
        }, 600);
    });
});

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
