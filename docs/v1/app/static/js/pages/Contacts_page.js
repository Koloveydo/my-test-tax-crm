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
