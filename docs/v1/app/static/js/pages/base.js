const menu_button = document.querySelector('.header_menu_button')
const close_menu = document.querySelector('.close_menu')
const phone_menu = document.querySelector('.phone_menu_content')

menu_button.addEventListener('click', () => {
    menu_button.classList.toggle('active')
    close_menu.classList.toggle('active')  
    phone_menu.classList.toggle('active')    
})

// Close menu
close_menu.addEventListener('click', () => {
    menu_button.classList.toggle('active')   
    close_menu.classList.toggle('active')   
    phone_menu.classList.toggle('active')    
})
