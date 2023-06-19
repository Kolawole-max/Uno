let share_btn
document.addEventListener('DOMContentLoaded', () => {

    let code_textfield = document.querySelector('.copy_text');
    code_textfield.value = generateCode()

    share_btn = document.getElementById("copy-button")
    share_btn.addEventListener('click', () => save_share_code(code_textfield));
    
})

function copyToClipboard(text) {
    navigator.clipboard.writeText(text)
      .then(() => {
        console.log('Text copied to clipboard');
      })
      .catch((error) => {
        console.error('Could not copy text: ', error);
      });
}

function generateCode(){
    let randomString = '';
    const possibleChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';

    for (let i = 0; i < 15; i++) {
    const randomIndex = Math.floor(Math.random() * possibleChars.length);
    const randomChar = possibleChars.charAt(randomIndex);
    randomString += randomChar;
    }
    console.log(randomString)
    return randomString;
}

async function save_share_code(code_textfield){
    code = code_textfield.value
    copyToClipboard(code)
    code_textfield.classList.add("active");
    window.getSelection().removeAllRanges();
    setTimeout(function(){
        code_textfield.classList.remove("active");
    },2500);

    // Display a successfull message

    await fetch('savecode/', {
        method: 'POST',
        body: JSON.stringify({
            code : code
        })
    })
        .then(response => response.json())
        .then(result => {
        // Print result
        console.log(result);
        Swal.fire({
            title: 'The share code is created sucessfully!',
            text: 'Paste the copied code on the company`s form.',
            icon: 'success',
            confirmButtonText: 'Okay'
        })
    });
}

  