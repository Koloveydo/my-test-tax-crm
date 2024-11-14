const user_profile_navigation = () => {
    const user_profile_menu = document.querySelectorAll('.user_profile_menu');
    const blueHelpingNavBar = document.querySelector('.blue_helping_nav_bar');

    user_profile_menu.forEach(option => {
        option.addEventListener("click", function () {
            var activeOption = document.querySelector('.user_profile_menu.active');

            if (option !== activeOption) {
                activeOption.classList.toggle('active');
                option.classList.toggle('active');
                document.querySelectorAll(".user_profile_main").forEach(page_content => page_content.classList.toggle('active'));

                var index = parseInt(document.querySelector(".user_profile_main.active").getAttribute("page-index"));
                blueHelpingNavBar.style.transform = `translateX(calc( ${index - 1} * (100% + 11px)))`;
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

    const sumbit_btn = document.querySelector('.apply_button');


    if (oldpassword_value !== '' && newPasssword_value !== '' && confirm_new_passswordValue !=='') {
        console.log('kkkk');
        sumbit_btn.classList.add('succes');
    } 

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

// old_password.addEventListener('input', checkInputs);
// new_password.addEventListener('input', checkInputs);
// confirm_new_passsword.addEventListener('input', checkInputs);

function openPopup() {
    console.log('WorkPOPUP');
    document.querySelector('.background_popup').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closePopup() {
    document.querySelector('.background_popup').classList.remove('active');
}

// DROPIMAGE
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

