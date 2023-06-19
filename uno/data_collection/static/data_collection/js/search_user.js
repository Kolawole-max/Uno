document.addEventListener('DOMContentLoaded', () => {

    let search_button = document.getElementById("search_button")
    let display_info = document.getElementById("display_info")

    const name = JSON.parse(document.getElementById('name').textContent);
    console.log(name)

    if(!name){
        display_info.style.display = 'None';
    }
    
})

function Search(){
    

    
}