document.querySelector("form").addEventListener("submit", function(event) {
    let isValid = true;
  
    // Get all the form fields
    let fields = document.querySelectorAll("input, select, textarea");
  
    // Loop through the fields and check if they're filled out
    for (let field of fields) {
      if (!field.value) {
        isValid = false;
        field.style.border = "1px solid red";
      } else {
        field.style.border = "";
      }
    }
  
    // If the form is not valid, prevent it from submitting
    if (!isValid) {
      event.preventDefault();
    }
  });
  
