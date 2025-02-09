const leadTable = document.querySelector('.leads_table')
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

document.getElementById('create_row').addEventListener('click', function() {
    const leadTable = document.querySelector('.leads_table')
    const createNewRow = document.querySelector('.ltable_create')
    const newRow = document.createElement('div');

    newRow.classList.add('ltable_body');
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

    leadTable.insertBefore(newRow, createNewRow);
})

