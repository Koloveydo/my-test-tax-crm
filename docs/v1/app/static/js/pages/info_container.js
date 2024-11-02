document.addEventListener("DOMContentLoaded", function() {
    const infoIcons = document.querySelectorAll('.info-icon img');
    const margin = 10;

    function adjustHelperTextPosition(helperText) {
        helperText.style.left = '50%';
        helperText.style.right = 'auto';
        helperText.style.transform = 'translateX(-50%)';
        helperText.style.top = 'auto';
        helperText.style.bottom = '100%';

        const rect = helperText.getBoundingClientRect();
        const windowWidth = window.innerWidth;
        const windowHeight = window.innerHeight;

        if (rect.right > windowWidth - margin) {
            helperText.style.left = 'auto';
            helperText.style.right = `${margin}px`;
            helperText.style.transform = 'none';
        }

        if (rect.left < margin) {
            helperText.style.left = `${margin}px`;
            helperText.style.right = 'auto';
            helperText.style.transform = 'none';
        }

        if (rect.top < margin) {
            helperText.style.bottom = 'auto';
            helperText.style.top = '100%';
        }
    }

    infoIcons.forEach(icon => {
        const helperText = icon.nextElementSibling;

        icon.addEventListener('mouseenter', function() {
            adjustHelperTextPosition(helperText);
        });

        icon.addEventListener('touchstart', function() {
            adjustHelperTextPosition(helperText);
        });
    });
});