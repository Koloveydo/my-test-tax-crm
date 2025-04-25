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
    attachInputListeners();
    checkInput();
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

/* -----------   change user setting popup  ------------- */

function attachInputListeners() {
    const changePopup = document.getElementById("change_setting_popup");
    document.querySelector(".pi_page_job_title").addEventListener("click", function() {

        const changeHeadText = document.getElementById("change_head_text");
        const currentSettingName = document.getElementById("current_setting_name");
        const currentUserSetting = document.getElementById("current_user_setting");
        const changedSettingName = document.getElementById("changed_setting_name");

        const value = this.dataset.value;
        const field = this.dataset.field;
        if (changePopup) changePopup.style.display = 'flex';
        if (changeHeadText) changeHeadText.textContent = "Change job title";
        if (currentSettingName) currentSettingName.textContent = "Current job title";
        if (changedSettingName) changedSettingName.textContent = "New job title";
        if (currentUserSetting) {
            currentUserSetting.value = value;
            currentUserSetting.setAttribute("data-field", field);
        }
        const inputSettingChange = document.getElementById("changed_user_setting");
        if (inputSettingChange){
            inputSettingChange.value = "";
        }
    });
}

/* ------------    close setting change popup ----------- */

document.addEventListener("click", (e) => {
    if (e.target.closest(".close_setting_popup_svg") || e.target.closest(".change_setting_cancel_btn")) {
        const changePopup = document.getElementById("change_setting_popup");
        changePopup.style.display = 'none';
    }
});

/* ------------  checking that we have text in input or not  ------------*/

function checkInput() {
    const inputSettingChange = document.getElementById("changed_user_setting");
    const buttonSettingChange = document.querySelector(".change_setting_confirm_btn");

    inputSettingChange.addEventListener("input", () => {
    if (inputSettingChange.value.trim() !== "") {
        buttonSettingChange.classList.add("active");
    } else {
        buttonSettingChange.classList.remove("active");
    }
    });
}

/*   завтра розібратись чому не загружає з бд дані про юзера через джс(чат джпт якусь хню висирає, потрібно буде опшукати в інеті)
/* доробити для всіх інпутів, щоб наповнювало під кожного з них унікальним текстом попап   */
