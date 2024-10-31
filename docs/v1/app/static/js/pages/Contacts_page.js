document.addEventListener("DOMContentLoaded", function () {
    const item = document.querySelector(".item");
    const information_content = document.querySelector(".information_content");

    item.forEach(item => {
        item.addEventListener('click', () => {

            item.forEach(i => i.classList.remove('active'));
            information_content.forEach(content => {
                content.classList.remove('active');
                content.querySelector('.All_content').style.display = 'none';
            });
            item.classList.add('active');

            const activeContent = document.querySelector(`#${information.dataset.active}`);
            activeContent.classList.add('active');
            activeContent.querySelector('.All_content').style.display = 'block';
        });
    });

    document.querySelector('.All_content').style.display = 'block';  