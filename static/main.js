// Adding functionality to form submit

const form = document.querySelector('.form');
const result = document.querySelector('.result');

function showResult(e){
    result.style.visibility = 'visible';
    e.preventDefault();
}

form.addEventListener('submit', showResult);