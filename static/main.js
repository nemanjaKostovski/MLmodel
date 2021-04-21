// Adding functionality to form submit

const form = document.querySelector('.form');
const result = document.querySelector('.result');

form.addEventListener('onsubmit', showResult());

function showResult(){
    result.style.display = block;
}

