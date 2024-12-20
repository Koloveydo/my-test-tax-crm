document.addEventListener('DOMContentLoaded', function () {
    const profilePage = document.getElementById('my_profile_page');

    document.documentElement.style.overflowY = 'scroll';
    document.documentElement.style.setProperty('--webkit-scrollbar', 'none');
});

function openForm() {
    document.getElementById("change_profile").style.display = "block";
}

function closeForm() {
    document.getElementById("change_profile").style.display = "none";
}

function openFormSkills() {
    document.getElementById("add_skills").style.display = "block";
}

function closeFormSkills() {
    document.getElementById("add_skills").style.display = "none";
}

function toggleDropdown() {
    const dropdown = document.getElementById("dropdown");
    dropdown.style.display = dropdown.style.display === "none" ? "block" : "none";
}

function updateInput(value) {
    const input = document.getElementById("field_value");
    const selectedField = document.getElementById("selected_field");
    input.value = value;
    selectedField.value = value;
}

document.querySelectorAll('.checkbox-btn').forEach(button => {
    button.addEventListener('click', () => {
        button.classList.toggle('active');
        console.log(`${button.dataset.value} is ${button.classList.contains('active') ? 'selected' : 'deselected'}`);
    });
});

function crossClick(event) {
    const popup = document.getElementById("change_profile");

    if (event.target.id === "my_profile_page" && popup.style.display === "block") {
        closeForm();
    }
};
function activateTab(index) {
    const tabs = document.querySelectorAll(".head_tab_click");
    const sections = document.querySelectorAll(".profile_section");

    tabs.forEach(tab => tab.classList.remove("active"));

    tabs[index].classList.add("active");

    sections.forEach(section => section.style.display = "none");

    if (sections[index]) {
        sections[index].style.display = "block";
    }
    document.documentElement.style.overflowY = 'scroll';
    document.documentElement.style.setProperty('--webkit-scrollbar', 'none');
}

const containers = document.querySelectorAll('.sender_letter_container');

containers.forEach(container => {
    container.addEventListener('click', function () {
        const index = [...this.classList].find(cls => cls.startsWith('col-')).split('-')[1];

        const textContainer = document.querySelector(`.letter_text_container.col-${index}`);
        const textToDo = document.querySelector(`.to_do.col-${index}`);
        
        if (textContainer) {
            if (textContainer.style.display === 'none') {
                textContainer.style.display = 'block';
                textToDo.style.display = 'none';
            } else {
                textContainer.style.display = 'none';
                textToDo.style.display = 'block';
            }
        }
    });
});
