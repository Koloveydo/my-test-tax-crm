
//статус ліда у таблиці

const leadTable = document.querySelector('.leads_bottom')
leadTable.addEventListener("click", function (event) {
    if (event.target.closest(".status_btn")) {
        const statusBtn = event.target.closest(".status_btn");
        const statusPopup = statusBtn.nextElementSibling;

        if (statusPopup) {
            statusPopup.style.display = "flex";
        }
    }

    if (event.target.classList.contains("variant")) {
        const selectedVariant = event.target.textContent;
        const statusPopup = event.target.closest(".status_popup");
        const statusBtn = statusPopup.previousElementSibling;

        statusBtn.innerHTML = `<div class="variant ${event.target.classList[1]}">${selectedVariant}</div>`;
        statusPopup.style.display = "none";
    }
});

//Створити рядок у таблиці

const createNewRow = document.querySelector(".leads_bottom")
createNewRow.addEventListener("click", function(event) {
    if (event.target.closest(".new_lead")) {
        const selectedTable = event.target.closest(".leads_table");
        const leadTable = selectedTable.querySelector("#ltable_all");
        const creationPosition = selectedTable.querySelector(".ltable_create");

        const newRow = document.createElement('div');
        newRow.classList.add("ltable_body");
        newRow.innerHTML = `
                    <div class="check_current_lead">
                <label class="custom_checkbox">
                    <input type="checkbox">
                    <span class="checkmark"></span>
                </label>
            </div>
            <div class="current_lead_name">
                <input type="text" class="board_input" value="" placeholder="Type lead name">
            </div>
            <div class="board current_status">
                <div class="status_btn">
                    <div class="variant vnew">New Lead</div>
                </div>
                <div class="status_popup">
                    <div class="status_variant">
                        <div class="variant vnew">New Lead</div>
                        <div class="variant vcontacted">Contacted</div>
                        <div class="variant vuncontacted">Uncontacted</div>
                        <div class="variant vblocked">Blocked</div>
                    </div>
                </div>
            </div>
            <div class="board current_organization">
                <input type="text" class="board_input" value="">
            </div>
            <div class="board current_email">
                <input type="text" class="board_input" value="">
            </div>
            <div class="board current_phone">
                <input type="text" class="board_input" value="">
            </div>
            <div class="board current_address">
                <input type="text" class="board_input" value="">
            </div>
            <div class="board current_title">
                <input type="text" class="board_input" value="">
            </div>
            <div class="board current_comment">
                <input type="text" class="board_input" value="">
            </div>
        `;
    
        leadTable.insertBefore(newRow, creationPosition);
    
        const inputField = newRow.querySelector(".board_input");
        inputField.focus();
    }
})


//чекбокс у таблиці для вибору одного ліда або всіх

document.addEventListener("change", function (event) {
    if (event.target.matches(".custom_checkbox input")) {
        const selectAll = event.target.closest(".all_rows");

        if (selectAll) {
            const table = event.target.closest(".leads_table");
            const allCheckboxes = table.querySelectorAll(".custom_checkbox input:not(.all_rows input)"); 

            allCheckboxes.forEach(checkbox => {
                checkbox.checked = event.target.checked;
                const row = checkbox.closest(".ltable_body");
                if (row) {
                    row.classList.toggle("checked_row", checkbox.checked);
                }
            });
        } else {
            const selectedRow = event.target.closest(".ltable_body");
            if (selectedRow) {
                selectedRow.classList.toggle("checked_row", event.target.checked);
            }
        }
    }
});


//Створити таблицю

document.getElementById('plus_table').addEventListener('click', function() {
    const mainTable = document.querySelector('.leads_bottom');
    const invisTable = document.getElementById('invisible_table');
    const newTable = document.createElement('div');
    
    newTable.classList.add('leads_table');
    newTable.innerHTML = `
        <div id="leads_top" class="leads_top">
            <svg id="arrow_open_lead" class="arrow_svg arr_lead" width="24" height="24" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8 12L16 20L24 12" stroke="#1E1E1E" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <div class="leads_top_name_container">
                <input type="text" class="leads_top_name" value="" placeholder="Type name of your table">
            </div>
            <div class="lead_amount"> 0 Leads</div>
        </div>
        <div id="ltable_all" class="ltable_all">
            <div class="ltable_head">
                <div class="check_all_leads">
                    <label class="custom_checkbox all_rows">
                        <input type="checkbox">
                        <span class="checkmark"></span>
                    </label>
                </div>
                <div class="board tname">Lead</div>
                <div class="board tstatus">Status</div>
                <div class="board torg">Organization</div>
                <div class="board temail">Email</div>
                <div class="board tphone">Phone</div>
                <div class="board taddress">Address</div>
                <div class="board ttitle">Title</div>
                <div class="board tcomment">Comment</div>
            </div>
            <div class="ltable_body">
                <div class="check_current_lead">
                    <label class="custom_checkbox">
                        <input type="checkbox">
                        <span class="checkmark"></span>
                    </label>
                </div>
                <div class="current_lead_name">
                    <input type="text" class="board_input" value="">
                </div>
                <div class="board current_status">
                    <div class="status_btn" id="status_btn">
                        <div class="variant vnew">New Lead</div>
                    </div>
                    <div class="status_popup" id="status_popup">
                        <div class="status_variant">
                            <div class="variant vnew">New Lead</div>
                            <div class="variant vcontacted">Contacted</div>
                            <div class="variant vuncontacted">Uncontacted</div>
                            <div class="variant vblocked">Blocked</div>
                        </div>
                    </div>
                </div>
                <div class="board current_organization">
                    <input type="text" class="board_input" value="">
                </div>
                <div class="board current_email">
                    <input type="text" class="board_input" value="">
                </div>
                <div class="board current_phone">
                    <input type="text" class="board_input" value="">
                </div>
                <div class="board current_address">
                    <input type="text" class="board_input" value="">
                </div>
                <div class="board current_title">
                    <input type="text" class="board_input" value="">
                </div>
                <div class="board current_comment">
                    <input type="text" class="board_input" value="">
                </div>
            </div>
            <div class="ltable_create">
                <div class="check_current_lead unactive">
                    <label class="custom_checkbox unactive">
                        <input type="checkbox">
                        <span class="checkmark"></span>
                    </label>
                </div>
                <div class="new_lead" id="create_row">+Add lead</div>
            </div>
        </div>
`;
    mainTable.insertBefore(newTable, invisTable);
    //mainTable.appendChild(newTable); 

    const inputField = newTable.querySelector(".leads_top_name");
    const inputArrow = newTable.querySelector("#arrow_open_lead path");
    const borderColor = newTable.querySelector("#ltable_all");
    inputField.focus();

    const colors = ["#2D64AB", "#D9534F", "#5CB85C", "#F0AD4E", "#2D64AB", "#800080", "#FFFFFF", "#FF69B4", "#40E0D0", "#FFA500" ];

    const randomColor = colors[Math.floor(Math.random() * colors.length)];

    inputField.style.color = randomColor;
    inputArrow.style.stroke = randomColor;
    borderColor.style.borderLeft = `5px solid ${randomColor}`;
});

//Сховати таблицю

document.addEventListener("click", function (event) {
    if (event.target.matches("#arrow_open_lead")) {
        const selectedTable = event.target.closest(".leads_table");
        if (selectedTable) {
            const openTable = selectedTable.querySelector("#arrow_open_lead");
            const hiddenTable = selectedTable.querySelector(".leads_top");
            const openedTable = selectedTable.querySelector(".ltable_all");

            if (openTable && hiddenTable && openedTable) {
                openTable.classList.toggle("active");
                hiddenTable.classList.toggle("active");
                openedTable.classList.toggle("active");
            }
        }
    }
});

//Пошук у таблиці на моїй сторінці
const searchIcon = document.querySelector(".pic-4");
const searchBtn = document.querySelector(".search_btn_lcont");
const searchInput = document.getElementById("search_input");
const searchText = document.querySelector(".search_text");

function toggleSearch() {
    searchInput.classList.toggle("active");
    searchText.classList.toggle("active");
    searchInput.focus();
}

searchIcon.addEventListener("click", toggleSearch);
searchText.addEventListener("click", toggleSearch);
document.getElementById("search_input").addEventListener("input", function () {
    const searchText = this.value.trim().toLowerCase();
    const leadsBottom = document.querySelector(".leads_bottom");
    const allElements = leadsBottom.querySelectorAll(".board_input");

    allElements.forEach(element => {
        let text = element.innerText.toLowerCase();
        if (element.tagName === "INPUT") {
            text = element.value.toLowerCase();
        }

        if (searchText && text.includes(searchText)) {
            element.style.backgroundColor = "#0E435D";
            element.style.color = "#fff";
        } else {
            element.style.backgroundColor = "";
            element.style.color = "";
        }
    });
});

// Кнопка коли клікаю фільтр за персоною

document.getElementById("person_container").addEventListener("click", function() {
    const personPop = document.getElementById("person_popup");
    personPop.classList.toggle("pop");
});






