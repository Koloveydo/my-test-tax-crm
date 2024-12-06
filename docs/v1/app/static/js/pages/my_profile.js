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
}
