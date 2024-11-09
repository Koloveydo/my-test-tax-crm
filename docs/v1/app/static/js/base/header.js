const menu_button = document.querySelector('.header_menu_button')
const close_menu = document.querySelector('.close_menu')
const phone_menu = document.querySelector('.phone_menu_content')

menu_button.addEventListener('click', () => {
    menu_button.classList.toggle('active')
    close_menu.classList.toggle('active')  
    phone_menu.classList.toggle('active')    
})
close_menu.addEventListener('click', () => {
    menu_button.classList.toggle('active')   
    close_menu.classList.toggle('active')   
    phone_menu.classList.toggle('active')    
})

let clicks = 0;
let clicks_2 = 0;

const link_button = document.querySelector('.contacts_link');
const link_button_2 = document.querySelector('.my_profile_link');
const mediaQuery = window.matchMedia('screen and (max-width: 1400px)');

link_button.addEventListener('click', function(event) {
    if (mediaQuery.matches) {
        event.preventDefault();
        clicks++;

        if (clicks === 2) {
            window.location.href = window.location.origin + '/';
            clicks = 0;
        }
    }
});
link_button_2.addEventListener('click', function(event) {
    if (mediaQuery.matches) {
        event.preventDefault();
        clicks_2++;

        if (clicks_2 === 2) {
            window.location.href = window.location.origin + '/';
            clicks_2 = 0;
        }
    }
});