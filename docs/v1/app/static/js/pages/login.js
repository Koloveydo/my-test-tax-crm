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

/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
/*		circle progress ob button       */
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

const circleAnimateSubmit = (selector) => {
	if (document.querySelector(selector)) {
		const btnSubmit = document.querySelector(selector);
		var old_text = btnSubmit.innerHTML;
		
		btnSubmit.innerHTML = `
			<div class="circle-loader"></div>
		`;
		btnSubmit.style.position = "relative";
		btnSubmit.disabled = true; 	

		setTimeout(() => {
			btnSubmit.innerHTML = old_text;
			btnSubmit.disabled = false; 	
		}, 3000);
	}
}

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


    /* ~~~ vadym, valid form submit ~~~ */

    if (form === registerForm) {
        var fetch_url = "/check-data-register";
        var formData = {
            "reg-email": document.getElementById("reg-email").value,
            "reg-pass": document.getElementById("reg-pass").value,
            "reg-name": document.getElementById("reg-name").value,
            "reg-surname": document.getElementById("reg-surname").value,
            "reg-organ": document.getElementById("reg-organ").value,
            "reg-job": document.getElementById("reg-job").value,
            "reg-phone": document.getElementById("reg-phone").value,
            "reg-address": document.getElementById("reg-address").value,
        };
        var btnSelector = ".login_page_btn";
    } else {
        var fetch_url = "/check-data-login";
        var formData = {
            "log-email": document.getElementById("log-email").value,
            "log-pass": document.getElementById("log-pass").value,
        };
        var btnSelector = ".register_btn";
    }
   
   
    // анімація кнопки після відправки
    circleAnimateSubmit(btnSelector);

    // Виконуємо запит fetch із .then для обробки результату
    fetch(fetch_url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) { 
            const existingError = form.querySelector("p.form-send-error");
            if (existingError) {
                existingError.remove()
            }
            window.location.href = data.url_to_redirect;

        } else {
            var text = data.message;

            if (form.querySelector("p.form-send-error")) {
				form.querySelector("p.form-send-error").textContent = text;
				form.querySelector("p.form-send-error").style.display = "block";
			} else {
				var error_text = document.createElement('p');
				error_text.textContent = text;
				error_text.classList.add("form-send-error");
				
				form.insertBefore(error_text, form.firstChild);
			}
        }
    })
    .catch((error) => {
        console.error("Error:", error);
        alert("Виникла помилка при відправленні форми.");
    });
	
};

function validateRegisterForm() {
    const inputs = registerForm.querySelectorAll('.form_group input');
    var valid = true;

    inputs.forEach((input) => {
        const value = input.value.trim();

        clearError(input);
        if (value === '') {
            setError(input, 'Information Required!');
            document.querySelectorAll('.eye').forEach(function(element) {
                element.style.paddingBottom='12px'
            });
            valid = false; 
        }
        if (input.classList.contains('password_input') && value.length < 8) {
            setError(input, 'Password must be more than 8 symbols!');
            valid = false;
        }
    });

    return valid;
}

function validateLoginForm() {
    const inputs = loginForm.querySelectorAll('.form_group input');
    const valid = true;

    inputs.forEach((input) => {
        const value = input.value.trim();
        clearError(input);

        if (value === '') {
            setError(input, 'Information Required!');
            valid = false; 
        }
        if (input.classList.contains('password_input') && value.length < 8) {
            setError(input, 'Password must be more than 8 symbols!');
            valid = false;
        }
    });

    return valid;
}



document.addEventListener("DOMContentLoaded", function () {
    registerForm.addEventListener('submit', (e) => {
        e.preventDefault();
        if (validateRegisterForm()) {
            addDynamicValidation(registerForm);
        }
    });
    
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        if (validateLoginForm()) {
            addDynamicValidation(loginForm);
        }
    });
})