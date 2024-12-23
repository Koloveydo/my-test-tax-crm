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

function updateInput(value) {
    const input = document.getElementById("field_value");
    const selectedField = document.getElementById("selected_field");
    input.value = value;
    if (selectedField) {
        selectedField.value = value;
    }
    input.removeAttribute("readonly");
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
    const tabs = document.querySelectorAll(".head_tab_click, .nav-item");
    const sections = document.querySelectorAll(".profile_section");

    tabs.forEach(tab => tab.classList.remove("active"));

    tabs[index].classList.add("active");

    sections.forEach(section => section.style.display = "none");

    if (sections[index]) {
        sections[index].style.display = "block";
    }
    if (document.body.classList.contains("dark-theme")) {
        tabs[index].classList.add("active");
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
                textContainer.style.display = 'flex';
                textToDo.style.display = 'none';
            } else {
                textContainer.style.display = 'none';
                textToDo.style.display = 'flex';
            }
        }
    });
});
function openPopup() {
    console.log('WorkPOPUP');
    document.querySelector('.background_popup').classList.add('active');
    document.body.style.overflow = 'hidden';
}
function closePopup() {
    document.querySelector('.background_popup').classList.remove('active');
}
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

function addSkill() {
    const input = document.getElementById("newSkillInput");
    const skillName = input.value.trim();
    const skillsContainer = document.getElementById("skillsContainer");

    if (!skillName) {
        alert("Please enter a skill name!");
        return;
    }

    const currentSkills = skillsContainer.querySelectorAll(".checkbox-btn");
    if (currentSkills.length >= 10) {
        alert("You can only add up to 5 custom skills!");
        return;
    }

    const existingSkill = Array.from(currentSkills).some(
        (skill) => skill.dataset.value.toLowerCase() === skillName.toLowerCase()
    );
    if (existingSkill) {
        alert("This skill already exists!");
        return;
    }

    const newSkillButton = document.createElement("button");
    newSkillButton.type = "button";
    newSkillButton.className = "checkbox-btn active";
    newSkillButton.dataset.value = skillName;
    newSkillButton.textContent = skillName;

    skillsContainer.appendChild(newSkillButton);

    input.value = "";
}

function openMessages(index) {
    const senders = document.querySelectorAll(".sender_icon");
    const letters = document.querySelectorAll(".letters");

    senders.forEach((sender, i) => {
        sender.classList.remove("active");
        letters[i].style.display = "none";
    });

    senders[index].classList.add("active");
    letters[index].style.display = "flex";
}

document.addEventListener("DOMContentLoaded", () => {
    openMessages(0);
});

function sendMessage() {
    const input = document.getElementById("user_message");
    const messageText = input.value.trim();

    if (messageText === "") return;

    const messagesContainer = document.querySelector(".messages_container");

    const newMessage = document.createElement("div");
    newMessage.className = "message_user";

    const userIcon = userData.url_image && userData.url_image !== "None"
        ? `<img class="circle_flname5" src="${userData.url_image}" alt="User Image">`
        : `<span class="circle_flname5">${userData.firstname[0].toUpperCase()}${userData.lastname[0].toUpperCase()}</span>`;

    newMessage.innerHTML = `
        ${userIcon}
        <div class="full_message">
            <div class="sender_message">${messageText}</div>
            <div class="message_data">${new Date().toLocaleString()}</div>
        </div>
    `;

    messagesContainer.prepend(newMessage);

    input.value = "";
}




