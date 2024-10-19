const body = document.querySelector('body');
const change_mode = document.querySelector('.change_mode_button');
const light_mode = document.querySelector('.light_mode');
const dark_mode = document.querySelector('.dark_mode');

let timer = false;

change_mode.addEventListener('click', () => {
    if (timer) return; 

    body.classList.toggle('dark-theme');

    if (body.classList.contains('dark-theme')) {
        dark_mode.classList.add('dark_mode_active');
    } else {
        dark_mode.classList.remove('dark_mode_active');
    }

    timer = true;

    setTimeout(() => {
        timer = false;
    }, 450);
});
