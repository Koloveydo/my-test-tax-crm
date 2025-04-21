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
