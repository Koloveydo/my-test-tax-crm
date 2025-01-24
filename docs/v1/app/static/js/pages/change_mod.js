document.addEventListener("DOMContentLoaded", function () {
    var body_element = document.querySelector('body');
    var change_mode = document.querySelectorAll('.change_mode_button');
    var dark_mode = document.querySelectorAll('.dark_mode');

    let timer = false;

    // Перевірка стану теми при завантаженні сторінки
    const darkThemeEnabled = localStorage.getItem('dark-theme') === 'true';
    if (darkThemeEnabled) {
        body_element.classList.add('dark-theme');
        dark_mode.forEach(item => item.classList.add('dark_mode_active'));
    }

    for (let i = 0; i < change_mode.length; i++) {
        var btn = change_mode[i];

        if (!btn.classList.contains("fin")) {
            btn.addEventListener('click', () => {
                if (timer) return;

                // Перемикаємо тему
                body_element.classList.toggle('dark-theme');

                // Зберігаємо стан теми в Local Storage
                const isDarkTheme = body_element.classList.contains('dark-theme');
                localStorage.setItem('dark-theme', isDarkTheme);

                // Додаємо або видаляємо клас для кнопок
                if (isDarkTheme) {
                    dark_mode[i].classList.add('dark_mode_active');
                } else {
                    dark_mode[i].classList.remove('dark_mode_active');
                }

                timer = true;

                setTimeout(() => {
                    timer = false;
                }, 450);
            });
            btn.classList.toggle("fin");
        }
    }
});
