document.addEventListener("DOMContentLoaded", function () {
    const tableContainer = document.querySelector(".table-container");

    tableContainer.addEventListener("wheel", function (event) {
        if (event.shiftKey) {
            event.preventDefault();
            tableContainer.scrollLeft += event.deltaY;
        }
    });
});

/* ----- open setting popup ------ */

async function openSettings() {
    const response = await fetch("/setting");
    const html = await response.text();
    document.body.insertAdjacentHTML("beforeend", html);
    attachMenuListeners();
}

document.addEventListener("click", (e) => {
    const elSetting = e.target.closest("[data_open_settings]");
    if (elSetting) {
        e.preventDefault();
        openSettings();
    }
});

/* ------- close setting popup --------- */

document.addEventListener("click", (e) => {
    if (e.target.closest(".close_setting_svg")) {
        const modal = document.getElementById("setting-popup");
        if (modal) {
            modal.remove();
        }
    }
});

/* ------ change setting page popup --------- */

function attachMenuListeners() {
    const settingMenu = document.querySelectorAll('.setting_menu_text_container');
    const settingPage = document.querySelectorAll('.setting_list_page_container');

    settingMenu.forEach(menuItem => {
        menuItem.addEventListener('click', () => {
            const index = menuItem.getAttribute('data-index');

            settingMenu.forEach(el => el.classList.remove('active'));
            settingPage.forEach(page => page.classList.remove('active'));

            menuItem.classList.add('active');

            const matchingPage = document.querySelector(`.setting_list_page_container[data-index="${index}"]`); // виправлено
            if (matchingPage) {
                matchingPage.classList.add('active');
            }
        });
    });
}

