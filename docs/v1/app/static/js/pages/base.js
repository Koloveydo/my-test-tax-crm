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
};

/* -----------   change user setting popup  ------------- */

function attachInputListeners() {
    let selectedButton = null;
    const changePopup = document.getElementById("change_setting_popup");
    const inputSettingChange = document.getElementById("changed_user_setting");
    document.querySelectorAll(".pi_page_first_small_info_input").forEach(button => {
        button.addEventListener("click", function () {
            const changeHeadText = document.getElementById("change_head_text");
            const currentSettingName = document.getElementById("current_setting_name");
            const currentUserSetting = document.getElementById("current_user_setting");
            const changedSettingName = document.getElementById("changed_setting_name");
            
            selectedButton = this;
            if (changePopup) changePopup.style.display = 'flex';
    
            if (changeHeadText) changeHeadText.textContent = this.dataset.changeHead || "Change setting"; 
            if (currentSettingName) currentSettingName.textContent = this.dataset.settingName || "Current setting";
            if (changedSettingName) changedSettingName.textContent = this.dataset.changeName || "New setting"; 
    
            if (currentUserSetting) {
                const textFromButton = this.textContent.trim();
                currentUserSetting.value = textFromButton;
            }
            if (inputSettingChange){
                inputSettingChange.value = "";
            }
        });
        document.getElementById("change_setting_confirm_btn").addEventListener("click", function() {
            if (!this.classList.contains("active")) {
                return; // Якщо немає класу active — просто вийти і нічого не робити
            }
            
            if (selectedButton) {
                selectedButton.textContent = inputSettingChange.value.trim();
                changePopup.style.display = 'none';
                selectedButton = null;
                this.classList.remove("active");
            }
        });
    });
    
};

/* ------------    close setting change popup ----------- */

document.addEventListener("click", (e) => {
    if (e.target.closest(".close_setting_popup_svg") || e.target.closest(".change_setting_cancel_btn")) {
        const changePopup = document.getElementById("change_setting_popup");
        const buttonSettingChange = document.querySelector(".change_setting_confirm_btn");
        changePopup.style.display = 'none';
        buttonSettingChange.classList.remove('active');
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

/*  --------- change photo script  ------------  */

function openPopup() {
    console.log('WorkPOPUP');
    document.querySelector('.background_popup').classList.add('active');
}

function closePopup() {
    document.querySelector('.background_popup').classList.remove('active');
}

/* ---------------- DROPIMAGE ------------------- */
const imageView =document.querySelector('.drop_img_container');
const inputFile = document.getElementById('input-file');
const drop_imageButton = document.querySelector('.drop_img_input')
const drop_image_txt = document.querySelector('.drop_img_container_txt')

inputFile.addEventListener("change", uploadImage);

function uploadImage(){
    let imgLink = URL.createObjectURL(inputFile.files[0]);
    imageView.style.backgroundImage = `url(${imgLink})`;
    drop_imageButton.style.display = 'none';
    drop_image_txt.style.display = 'none';
}

/* -------------- demo popup ------------*/

const demoContainer = document.getElementById("global_demo_popup");
const closeDemoContainer = document.getElementById("global_demo_close_btn");

function globalDemoPopup() {
    demoContainer.style.display = 'flex';
}

closeDemoContainer.addEventListener("click", function(){
    demoContainer.style.display = 'none';
});

/* доробити решту сторінок налаштування*/
/* зробити фідбек сторінку with ajax */
/* добавити фідбек сторінку інпутам */
/* полагодити анімацію навбару */
/* адаптацію доробити для масс емейлу, чат джпт порадив як ( оверфлоф видний + скрол)
/* не забути у налаштуваннях в останньому пункті добавити лог аут, він є у мобільному меню хедера, там є підказка */
