// Adding functionality to form submit

const button = document.querySelector('.button');
const result = document.querySelector('.result');

button.addEventListener('submit', showResult);

function showResult(){
    result.style.display = 'block';
}

