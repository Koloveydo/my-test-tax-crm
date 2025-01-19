
const triggerElement = document.querySelector('.under_button');
const targetElement = document.querySelector('.left_nav');
const targetElementContent = document.querySelector('.left_nav_content');

triggerElement.addEventListener('mouseover', () => {
    targetElement.classList.add('hover');
    targetElementContent.classList.add('hover');
});

targetElement.addEventListener('mouseleave', () => {
    targetElement.classList.remove('hover');
    targetElementContent.classList.remove('hover');

});


document.addEventListener("DOMContentLoaded", function () {
    const navButton = document.getElementById("left_nav_button");
    const navContent = document.getElementById("left_nav_content");
    const navSvg = document.getElementById("left_nav_svg");
    const navLeft = document.getElementById("left_nav");
    const navDople = document.getElementById("nav_dople")

    navButton.addEventListener("click", function () {
        navContent.classList.toggle("active");
        navLeft.classList.toggle("active");
        navDople.classList.toggle("active");
        navSvg.classList.toggle("active");
    });
});

const element = document.querySelector('.left_dople_nav');

element.addEventListener('mouseover', () => {
    element.classList.add('active');
});

element.addEventListener('mouseout', () => {
    element.classList.remove('active');
});

