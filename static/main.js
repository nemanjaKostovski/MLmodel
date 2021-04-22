// Adding functionality to form submit

const form = document.querySelector('.form');
const result = document.querySelector('.result');

function showResult(){
    result.style.visibility = 'visible';
}

form.addEventListener('submit', showResult);

