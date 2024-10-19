const inputName = document.querySelector('.text_required_input')
const name_error = document.querySelector('.text_label_required_input')
const submitBtn = document.querySelector('.sumbit_btn')

submitBtn.addEventListener('click', (e) => {
    e.preventDefault(); 

    name_error.innerHTML = 'Text';
    inputName.style.border = '';

    if (inputName.value === '' || inputName.value == null) {
        name_error.innerHTML = 'Write Text! <p style="color: red; padding: 0px;">*</p>'; 
        inputName.style.border= "1px, solid red";
    }
    if (inputName.value !=='') {
        form.submit()
    }
});
