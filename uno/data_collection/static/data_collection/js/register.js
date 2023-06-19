let add_more = document.getElementById('btn-add-more');
let added_field = []

add_more.addEventListener('click', () =>{
    let newFeild = document.createElement('input');
    newFeild.setAttribute('type', 'file');
    newFeild.setAttribute('name', 'identification-card');
    newFeild.setAttribute('class', 'identification-card');
    newFeild.setAttribute('style', 'margin-bottom:10px');
    survey_options.appendChild(newFeild);
    added_field.push(2)
})


document.addEventListener('DOMContentLoaded', () => {

    let form = document.querySelector('form');

    var inputs = document.querySelectorAll('input[type="text"], input[type="email"], input[type="file"], input[type="password"], input[type="number"], select');

    form.addEventListener('submit', function (e) {
        let errorCounter = [];

        for (var i = 0; i < inputs.length; i++) {
            if (inputs[i].value === "" || inputs[i].value == null) {
                inputs[i].style.border = "1px solid red";
                getErrorElement(inputs[i].name).innerHTML = getInputName(inputs[i].name) + " field must not be empty";
                errorCounter.push(2);
            } else {
                inputs[i].style.border = "";
                getErrorElement(inputs[i].name).innerHTML = "";
            }
        }
        if (errorCounter.length > 0) {
            e.preventDefault();
        }
        
    }) 
})

function printError(inputs) {
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].value === "" || inputs[i].value == null) {
            inputs[i].style.border = "1px solid red";
            getErrorElement(inputs[i].name).innerHTML = getInputName(inputs[i].name) + " field must not be empty";
            errorCounter.push(2);
        } else {
            inputs[i].style.border = "";
            getErrorElement(inputs[i].name).innerHTML = "";
        }
    }
    if (errorCounter.length > 0) {
        e.preventDefault();
    }
    
}

function getErrorElement(inputName) {
    var errorClassName = "." + inputName + "-error";
    var errorElement = document.querySelector(errorClassName)
    return errorElement;
}

function getInputName(message) {
    let newString = ""
    let hyphens = message.replace("-", " ");
    for (let sentence of hyphens.split(". ")) {
        newString += sentence.charAt(0).toUpperCase() + sentence.slice(1);
    }
    return newString
} 


  