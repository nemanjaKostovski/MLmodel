// Adding functionality to form submit

const form = document.querySelector('.form');
const result = document.querySelector('.result');

function showResult(evt){
    evt.preventDefault();
    result.style.display = 'block';
}

form.addEventListener('submit', showResult);

