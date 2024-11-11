const inputName = document.querySelector('.text_required_input')
const submitBtn = document.querySelector('.sumbit_btn')

submitBtn.addEventListener('click', (e) => {
    e.preventDefault(); 

    if (inputName.value === '' || inputName.value === null) {
        var error_message = inputName.parentElement.querySelector('span.error');
        error_message.textContent = "Please fill out this field."; 
        error_message.style = 'display: block;'; 
        inputName.focus()
    }
    if (inputName.value !=='') {
        form.submit()
    }
});

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ //
//     onchange validate input    //
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ //

const clearValidateInputElement = (self) => {
    var input = self;

    if (inputName.value !== '' && inputName.value !== null) {
        var error_message = input.parentElement.querySelector('span.error');
        error_message.textContent = ""; 
        error_message.style = 'display: none;'; 
    } 
}