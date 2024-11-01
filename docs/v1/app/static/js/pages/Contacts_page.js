function showTabContent(contentClass) {
    document.querySelectorAll('.all_contact_content, .clients_content, .leads_content').forEach(function (content) {
        content.style.display = 'none';
    });
    document.querySelector(`.${contentClass}`).style.display = 'block';
    document.querySelectorAll('.tabs > div').forEach(function (tab) {
        tab.classList.remove('active');
    });
    const activeTab = [...document.querySelectorAll('.tabs > div')].find(tab => {
        return tab.getAttribute('onclick').includes(contentClass);
    });
    if (activeTab) {
        activeTab.classList.add('active');
    }
}
showTabContent('all_contact_content');
const contacts = [
    {
        photo: '',
        name: 'John',
        surname: 'Doe',
        organization: 'Company A',
        email: 'john@example.com',
        phone: '123-456-7890',
        skills: 'JavaScript, HTML, CSS, Flask, Java'
    },
    {
        photo: '',
        name: 'John',
        surname: 'Doe',
        organization: 'Company A',
        email: 'john@example.com',
        phone: '123-456-7890',
        skills: 'JavaScript, HTML, CSS, Flask, Java'
    },
    {
        photo: '',
        name: 'John',
        surname: 'Doe',
        organization: 'Company A',
        email: 'john@example.com',
        phone: '123-456-7890',
        skills: 'JavaScript, HTML, CSS, Flask, Java'
    },
    {
        photo: '',
        name: 'John',
        surname: 'Doe',
        organization: 'Company A',
        email: 'john@example.com',
        phone: '123-456-7890',
        skills: 'JavaScript, HTML, CSS, Flask, Java'
    },
];
function createContactCard(contact) {
    const skillsArray = contact.skills.split(', ');
    const firstThreeSkills = skillsArray.slice(0, 3).join(', ');
    const remainingSkills = skillsArray.slice(3).join(', ');
    return `
        <div class="contact_card">
            <div class="contact_photo"></div>
            <div class="contact_info">
                <p style="padding-left: 145px;">${contact.name}</p>
                <p style="padding-left: 180px;">${contact.surname}</p>
                <p style="padding-left: 200px;">${contact.organization}</p>
                <p style="padding-left: 140px;">${contact.email}</p>
                <p style="padding-left: 105px;">${contact.phone}</p>
                <div class="skills">
                <p style="display: inline; padding-left: 90px;">${firstThreeSkills}</p>
                <p style="padding-left: 125px; margin-top: 5px;">${remainingSkills}</p>
                </div>
            </div>
        </div>
    `;
}
function renderContactCards() {
    const container = document.querySelector('.contact_cards_container');
    contacts.forEach(contact => {
        container.innerHTML += createContactCard(contact);
    });
}
renderContactCards();
