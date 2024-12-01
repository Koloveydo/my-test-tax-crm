function open_register() {
    console.log("switched to register");
    document.querySelector('.register').classList.add('active');
    document.querySelector('.login_page').classList.remove('active');
}
function open_login() {
    console.log("switched to login");
    document.querySelector('.login_page').classList.add('active');
    document.querySelector('.register').classList.remove('active');
}

let show_passwords = document.querySelectorAll('.eye_svg');
let hide_passwords = document.querySelectorAll('.close_eye_svg');
let passwords = document.querySelectorAll('.password_input');

passwords.forEach((password, position) => {
    const show_eye = show_passwords[position];
    const hide_eye = hide_passwords[position];

    show_eye.onclick = function () {
        show_eye.classList.add('active');
        hide_eye.classList.add('active');
        password.type = "text";
    };

    hide_eye.onclick = function () {
        show_eye.classList.remove('active');
        hide_eye.classList.remove('active');
        password.type = "password"; 
    };
});



const setError = (element, message) => {
    const formGroup = element.parentElement;
    const errorP = formGroup.querySelector('.error');
    errorP.innerText = message;
    formGroup.classList.add('error');
    document.querySelectorAll('.eye').forEach(function(element) {
        element.style.paddingBottom='12px'
    });
};
const clearError = (element) => {
    const formGroup = element.parentElement;
    const errorP = formGroup.querySelector('.error');
    errorP.innerText = '';
    formGroup.classList.remove('error');
    document.querySelectorAll('.eye').forEach(function(element) {
        element.style.paddingBottom='0px'
    });
};

const registerForm = document.querySelector('.login_form');
const loginForm = document.querySelector('.register form');

const addDynamicValidation = (form) => {
    const inputs = form.querySelectorAll('.form_group input');

    inputs.forEach((input) => {
        input.addEventListener('focus', () => {
            clearError(input);
        });
        input.addEventListener('blur', () => {
            if (input.value.trim() === '') {
                setError(input, 'Information Required!');
            }
        });
    });
};

function validateRegisterForm() {
    const inputs = registerForm.querySelectorAll('.form_group input');

    inputs.forEach((input) => {
        const value = input.value.trim();

        clearError(input);
        if (value === '') {
            setError(input, 'Information Required!');
            document.querySelectorAll('.eye').forEach(function(element) {
                element.style.paddingBottom='12px'
            });
            return; 
        }
        if (input.classList.contains('password_input') && value.length < 8) {
            setError(input, 'Password must be more than 8 symbols!');
            return;
        }
    });
}

function validateLoginForm() {
    const inputs = loginForm.querySelectorAll('.form_group input');

    inputs.forEach((input) => {
        const value = input.value.trim();
        clearError(input);

        if (value === '') {
            setError(input, 'Information Required!');
            return; 
        }
        if (input.classList.contains('password_input') && value.length < 8) {
            setError(input, 'Password must be more than 8 symbols!');
            return;
        }
    });
}

registerForm.addEventListener('submit', (e) => {
    e.preventDefault();
    validateRegisterForm();
    addDynamicValidation(registerForm);
});

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    validateLoginForm();
    addDynamicValidation(loginForm);
});
