'use strict';
let data = JSON.parse("{{data|escapejs}}");

const clearweather = document.querySelector('.clear');
const drizzle = document.querySelector('.drizzle');
const mostly_clear = document.querySelector('.mostly_clear');
const weather_condition = document.querySelector('.weather-condition');

clearweather.innerHTML += "{{data|escapejs}}";
drizzle.innerHTML += "{{data|escapejs}}";
mostly_clear.innerHTML += "{{data|escapejs}}";

if(weather_condition === 'clear'){
    clearweather.classList.remove('hidden');
}else if ( weather_condition === 'drizzle'){
    drizzle.classList.remove('hidden');
}else if( weather_condition === 'mostly_clear'){
    mostly_clear.classList.remove('hidden');
}

console.log(clearweather.innerHTML[weather_code])