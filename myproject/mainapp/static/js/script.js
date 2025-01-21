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


function toggleDropdown() {
    const menu = document.querySelector('.custom-dropdown-menu');
    menu.classList.toggle('show');
}

function selectLanguage(language, flagUrl) {
    // Меняем текст и картинку в кнопке
    const toggle = document.querySelector('.custom-dropdown-toggle');
    toggle.innerHTML = `
        <img src="${flagUrl}" alt="${language}">
        <span>${language}</span>
    `;

    // Закрываем выпадающий список
    const menu = document.querySelector('.custom-dropdown-menu');
    menu.classList.remove('show');
}

// Закрыть выпадающий список при клике вне его
document.addEventListener('click', (event) => {
    const dropdown = document.querySelector('.custom-dropdown');
    if (!dropdown.contains(event.target)) {
        document.querySelector('.custom-dropdown-menu').classList.remove('show');
    }
});