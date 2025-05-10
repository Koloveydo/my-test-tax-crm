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
    getLocation();
    getLocalIP();
    getUserDate();
    showSessionDuration()
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

            const matchingPage = document.querySelector(`.setting_list_page_container[data-index="${index}"]`);
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
                return;
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

/* ---------------  checking input password  ---------------*/

document.addEventListener("input", function (e) {
    if (e.target && e.target.id === "log-pass") {
        const passwordInput = e.target.value;
        const newPass = document.getElementById("new_pass");
        const confirmPass = document.getElementById("confirm_pass");
        const savePassBtn = document.getElementById("save_password_btn");
        const outputDiv = document.querySelector(".pass_error");

        fetch("/settings/check-password", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ password: passwordInput })
        })
        .then(response => response.json())
        .then(data => {
            if (data.match) {
                newPass?.removeAttribute('readonly');
                confirmPass?.removeAttribute('readonly');
                savePassBtn?.classList.add('active');
                outputDiv.textContent = "Correct password";
                outputDiv.style.color = "#06a600";
            } else {
                newPass?.setAttribute('readonly', true);
                newPass.value = '';
                confirmPass?.setAttribute('readonly', true);
                confirmPass.value = '';
                savePassBtn?.classList.remove('active');
                outputDiv.textContent = "Incorrect password";
                outputDiv.style.color = "#ba0000";
            }
        })
        .catch(error => {
            outputDiv.textContent = "Помилка: " + error;
        });
    }
});

/* checking that new pass = confirm pass */

function confirmPassBtn() {
    const confirmErrorText = document.querySelector(".new_pass_error");
    const newPass = document.getElementById("new_pass");
    const confirmPass = document.getElementById("confirm_pass");

    if (newPass.value === confirmPass.value && newPass.value.length >= 8 &&  newPass.value.trim() !== "" ) {
        confirmErrorText.textContent = "Valid Password";
        confirmErrorText.style.color = "#06a600";
        globalDemoPopup();
    } else {
        confirmErrorText.textContent = "Invalid Password";
        confirmErrorText.style.color = "#ba0000";
    }
};

/* checking user devise */

function detectDeviceInfo() {
    const userAgent = navigator.userAgent;
    let os = "Unknown OS";
    let browser = "Unknown Browser";

    if (userAgent.includes("Win")) os = "Windows";
    else if (userAgent.includes("Mac")) os = "macOS";
    else if (userAgent.includes("Linux")) os = "Linux";
    else if (userAgent.includes("Android")) os = "Android";
    else if (userAgent.includes("iPhone") || userAgent.includes("iPad")) os = "iOS";

    if (userAgent.includes("Chrome") && !userAgent.includes("Edg") && !userAgent.includes("OPR")) {
        browser = "Chrome";
    } else if (userAgent.includes("Firefox")) {
        browser = "Firefox";
    } else if (userAgent.includes("Safari") && !userAgent.includes("Chrome")) {
        browser = "Safari";
    } else if (userAgent.includes("Edg")) {
        browser = "Edge";
    } else if (userAgent.includes("OPR") || userAgent.includes("Opera")) {
        browser = "Opera";
    }

    const deviceText = `${os}, ${browser}`;
    const deviceBlock = document.querySelector('.session_device');
    if (deviceBlock) {
        deviceBlock.textContent = deviceText;
    }
};

/* ----------- checking user location  ----------------- */

function getLocation() {
    fetch('https://ipapi.co/json/')
  .then(response => response.json())
  .then(data => {
    const location = `${data.city}, ${data.country}`;
    document.querySelector(".session_location").textContent = location;
  })
  .catch(error => {
    console.error("Geo error:", error);
  });

};

/* -------------- checking user ip address -------------- */

function getLocalIP() {
    fetch('https://api.ipify.org?format=json')
  .then(response => response.json())
  .then(data => {
    const ip = data.ip;
    console.log("IP Address:", ip);
    document.querySelector(".session_ip").textContent = ip;
  });
};

/* ---------------- checking date ---------------------- */

function getUserDate() {
    const now = new Date();

    const formattedDate = now.getFullYear() + '-' +
        String(now.getMonth() + 1).padStart(2, '0') + '-' +
        String(now.getDate()).padStart(2, '0');

    document.querySelector(".session_last_usage").textContent = formattedDate;

    return formattedDate;
};

/* ------------------  checking login time ----------------- */

function showSessionDuration() {
    const loginTimeString = sessionStorage.getItem("login_time");

    if (!loginTimeString) return;

    const loginTime = new Date(loginTimeString);
    const now = new Date();

    const diffMs = now - loginTime;
    const diffMinutes = Math.floor(diffMs / 60000);

    document.querySelector(".session_time").textContent = `${diffMinutes} minutes ago`;
}

/* -------------------  log out ---------------- */

document.addEventListener("click", function (e) {
    const container = e.target.closest(".session_btn_container");
    if (container) {
        window.location.href = container.dataset.url;
    }
});

/* -----------------  open feedback page  --------------------- */

async function openFeedback() {
    const response = await fetch ("/feedback")
    const html = await response.text();
    document.body.insertAdjacentHTML("beforeend", html);
    feedbackNavbar();
    expandMessage();
    allReadMessages();
    initQuillEditor();
    quillDark();
    checkFeedback();
};

document.addEventListener("click", (e) => {
    const elFeedback = e.target.closest("[data_open_feedback]");
    if (elFeedback) {
        e.preventDefault();
        openFeedback();
    }
});

/* ------- close feedback page --------- */

document.addEventListener("click", (e) => {
    if (e.target.closest(".close_feedback_svg")) {
        const modal = document.getElementById("feedback-popup");
        if (modal) {
            modal.remove();
        }
    }
});

/* --------- change feedback nav page ---------- */    /* ------  доробити  ------ */

function feedbackNavbar() {
    const feedbackMenu = document.querySelectorAll('.feedback_nav_text');
    const feedbackPage = document.querySelectorAll('.feedback_page_main');
    const feedbackNamePage = document.querySelector('.feedback_page_name');

    feedbackMenu.forEach(feedbackItem => {
        feedbackItem.addEventListener('click', () => {
            const index = feedbackItem.getAttribute('data-feedback-index');

            feedbackMenu.forEach(feedline => feedline.classList.remove('active'));
            feedbackPage.forEach(feedpage => feedpage.classList.remove('active'));

            feedbackItem.classList.add('active');

            const chosenPage = document.querySelector(`.feedback_page_main[data-feedback-index="${index}"]`);
            if (chosenPage) {
                chosenPage.classList.add('active');
                feedbackNamePage.textContent = feedbackItem.textContent;
            }
        });
    });
};

/* ---------------- script to see all message -------------- */

function expandMessage() {
    document.addEventListener("click", function(event) {

        const expandBtn = event.target.closest(".feedback_message_update_more");

        if (!expandBtn) return;

        const messageContainer = expandBtn.closest(".feedback_message_container");

        if (!messageContainer) return;

        const expandedMessage = messageContainer.querySelector(".feedback_message_update_text");
        const readMessageMark = messageContainer.querySelector(".read_mark");

        if (expandedMessage) {
            expandedMessage.style.maxHeight = "none";
            expandedMessage.classList.add("expanded");
            expandBtn.style.display = "none";
        }

        if (readMessageMark) {
            readMessageMark.classList.add("read");
        }
    });
}

/* ------------  mark all messages as read  ---------------- */

function allReadMessages() {
    document.querySelector(".feedback_mark_container").addEventListener("click", function() {
        const readMessageMarks = document.querySelectorAll(".read_mark");
        readMessageMarks.forEach(readMessageMark => readMessageMark.classList.add("read"));
    });
};

/* --------------  dark-theme for editor ----------------- */
function quillDark() {
    if (document.body.classList.contains("dark-theme")) {
        document.getElementById("feedback_editor").classList.add("dark-theme");
    } else {
        document.getElementById("feedback_editor").classList.remove("dark-theme");
    }
};

/* ----------- initiation quil editor ---------------- */

function initQuillEditor() {
    const editorElement = document.querySelector('#feedback_editor');
    if (editorElement) {
        new Quill('#feedback_editor', {
            theme: 'snow'
        });
    }
};

/* --------------- send message script for feedback page ----------------- */

function checkFeedback() {
    const noFeedback = document.getElementById("zero_feedback_message");
    const yesFeedback = document.getElementById("user_feedback_message_container");
    function checkFeedbackMessages() {
        const hasFeedback = yesFeedback.querySelector(".feedback_message_container");

        if (hasFeedback) {
            yesFeedback.style.display = "flex";
            noFeedback.style.display = "none";
        } else {
            yesFeedback.style.display = "none";
            noFeedback.style.display = "flex";
        }
    }
    checkFeedbackMessages();
    const observerFeedback = new MutationObserver(checkFeedbackMessages);
    observerFeedback.observe(yesFeedback, { childList: true, subtree: true });
};

function sendFeedback() {
    const fatherContainer = document.querySelector(".write_message_main_feedback_container");
    const quillEditor = fatherContainer.querySelector(".ql-editor");
    const feedbackText = quillEditor.innerHTML;
    const feedbackPlainText = quillEditor.innerText.trim();
    const yesFeedback = document.getElementById("user_feedback_message_container");

    if (feedbackPlainText === "") return; 

    const createFeedback = document.createElement("div");
    createFeedback.className = "feedback_message_container";

    createFeedback.innerHTML = `
                                <div class="feedback_message_update_main">
                                    <div class="feedback_message_update_text"></div>
                                    <div class="feedback_message_update_more_container">
                                    <div class="feedback_message_update_more">...See more</div>
                                </div>
    
    `;

    yesFeedback.prepend(createFeedback);
    const feedbackValue = createFeedback.querySelector(".feedback_message_update_text");
    feedbackValue.innerHTML = feedbackText;
};


/* полагодити анімацію навбару */

/*------------------  + task ---------------------------*/

/* зробити аякс запит, який буде догружати контент сторінки при прокрутці до самого низу, корисний + */
