//setting up readline so that we can get user input
const prompt = require('prompt-sync')();

//getting user name
const userName = prompt('What is your name? ');

// get user birthday
const birthday = prompt('What is your birthday? Please enter it in the MM-DD format: ');
const birthdate = new Date(birthday);
