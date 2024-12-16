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

// Знаходимо всі контейнери з класом sender_letter_container
const containers = document.querySelectorAll('.sender_letter_container');

containers.forEach(container => {
    container.addEventListener('click', function () {
        // Отримуємо індекс поточного контейнера
        const index = [...this.classList].find(cls => cls.startsWith('col-')).split('-')[1];

        // Знаходимо відповідний елемент із класом letter_text_container
        const textContainer = document.querySelector(`.letter_text_container.col-${index}`);
        
        if (textContainer) {
            // Перемикаємо display між none і block
            if (textContainer.style.display === 'none') {
                textContainer.style.display = 'block';
            } else {
                textContainer.style.display = 'none';
            }
        }
    });
});
