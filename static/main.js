// Adding functionality to form submit

const button = document.querySelector('.button');
const result = document.querySelector('.result');

button.addEventListener('onsubmit', showResult);

function showResult(){
    result.style.display = 'block';
}

