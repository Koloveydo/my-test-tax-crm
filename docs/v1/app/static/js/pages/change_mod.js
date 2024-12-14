document.addEventListener("DOMContentLoaded", function () {
    var body_element = document.querySelector('body');
    var change_mode = document.querySelectorAll('.change_mode_button');
    var dark_mode = document.querySelectorAll('.dark_mode');

    let timer = false;

    for (let i = 0; i < 2; i++) {
        var btn = change_mode[i];

        if (!btn.classList.contains("fin")) {
            btn.addEventListener('click', () => {
                if (timer) return; 
            
                body_element.classList.toggle('dark-theme');
                console.log("change mode");
            
                if   (body_element.classList.contains('dark-theme')) { dark_mode[i].classList.add('dark_mode_active'); } 
                else { dark_mode[i].classList.remove('dark_mode_active'); }
            
                timer = true;
            
                setTimeout(() => {
                    timer = false;
                }, 450);
            });
            btn.classList.toggle("fin");
        }
        
    }
})