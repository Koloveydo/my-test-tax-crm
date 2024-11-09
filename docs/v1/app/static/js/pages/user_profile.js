const My_accaunt = document.querySelector('.my_accaunt')

const user_profile_navigation = () => {
    const user_profile_menu = document.querySelectorAll('.user_profile_menu');
    const blueHelpingNavBar = document.querySelector('.blue_helping_nav_bar');

    user_profile_menu.forEach(option => {
        option.addEventListener("click", function () {
            const My_account_option = document.querySelector('.user_profile_menu.active');

            if (option !== My_account_option) {
                My_account_option.classList.remove('active');
                option.classList.toggle('active');
                
                blueHelpingNavBar.style.transform = `translateX(${option.offsetLeft + option.offsetWidth / 1.7 - blueHelpingNavBar.offsetWidth / 1.3}px)`;

            }

            if (option === My_account_option)
                console.log("jjj"); {
                My_accaunt.classList.toggle('active')
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', function () {
    user_profile_navigation();
});

// CHECKING FORMS
const form = document.querySelector('.user_password_inputs')
const old_password = document.querySelector('.old_password')
const new_password = document.querySelector('.new_password')
const confirm_new_passsword = document.querySelector('.confirm_new_pswrd')

form.addEventListener('submit', e => {
    e.preventDefault();
    checkInputs();
});

const setError = (element, message) => {
    const formGroup = element.parentElement;
    const errorP = formGroup.querySelector('.error');
    errorP.innerText = message;
    formGroup.classList.add('error');
}
const clearError = (element) => {
    const formGroup = element.parentElement;
    const errorText = formGroup.querySelector('.error');
    errorText.innerText = '';
    formGroup.classList.remove('error');
}

const checkInputs = () => {
    const oldpassword_value = old_password.value.trim();
    const newPasssword_value = new_password.value.trim();
    const confirm_new_passswordValue = confirm_new_passsword.value.trim();

    if (oldpassword_value === '') {
        setError(old_password, 'Required pass');
    // } else if (oldpassword_value !== oldpassword_value) {
    //     setError(old_password, 'Fail passsword try again'); 
    } else {
        clearError(old_password);
    }

    if (newPasssword_value === '') {
        setError(new_password, 'Required pass');
    } else if (oldpassword_value.length === 0) {
        setError(new_password, 'Enter your old password first');
    } else if (newPasssword_value.length < 8) {
        setError(new_password, 'Password must be 8 or more symbols')
    } else {
        clearError(new_password);
    }

    if (confirm_new_passswordValue === '') {
        setError(confirm_new_passsword, 'Required pass');
    } else if (newPasssword_value !== confirm_new_passswordValue) {
        setError(confirm_new_passsword, 'Not the same as new password');
    } else {
        clearError(confirm_new_passsword);
    }
    
};
