
const triggerElement = document.querySelector('.under_button');
const targetElement = document.querySelector('.left_nav');
const targetElementContent = document.querySelector('.left_nav_content');

let showTimeout;

triggerElement.addEventListener('mouseover', () => {
    clearTimeout(showTimeout);
    targetElement.classList.add('hover');
    showTimeout = setTimeout(() => {
        requestAnimationFrame(() => {
            targetElementContent.classList.add('hover');
        });
    }, 100); 
});

targetElement.addEventListener('mouseleave', () => {
    clearTimeout(showTimeout);
    targetElement.classList.remove('hover');
    targetElementContent.classList.remove('hover');

});


document.addEventListener("DOMContentLoaded", function () {
    const navButton = document.getElementById("left_nav_button");
    const navContent = document.getElementById("left_nav_content");
    const navSvg = document.getElementById("left_nav_svg");
    const navLeft = document.getElementById("left_nav");
    const navDople = document.getElementById("nav_dople")

    let showTimeout;

    navButton.addEventListener("click", function () {
        navLeft.classList.toggle("active");
        navDople.classList.toggle("active");
        navSvg.classList.toggle("active");
        showTimeout = setTimeout(() => {
            requestAnimationFrame(() => {
                navContent.classList.toggle("active");
            });
        }, 100); 
    });
});

const element = document.querySelector('.left_dople_nav');

element.addEventListener('mouseover', () => {
    element.classList.add('active');
});

element.addEventListener('mouseout', () => {
    element.classList.remove('active');
});

function updateActiveNavItem() {
    const navItems = document.querySelectorAll('.left_nav_text_container');
    const currentPath = window.location.pathname;

    navItems.forEach(item => {
        const href = item.getAttribute('data-href');

        if (href === currentPath) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });
}

const navItems = document.querySelectorAll('.left_nav_text_container');
navItems.forEach(item => {
    item.addEventListener('click', () => {
        const href = item.getAttribute('data-href');
        if (href) {
            window.location.href = href;
        }
    });
});

document.addEventListener('DOMContentLoaded', updateActiveNavItem);

