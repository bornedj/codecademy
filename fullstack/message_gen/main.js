//importing objects from signs.js
const signs = require('./signs.js');

//setting up readline so that we can get user input
const prompt = require('prompt-sync')();

//getting user name
const userName = prompt('What is your name? ');

// get user birthday
const birthday = prompt('What is your birthday? Please enter it in the MM-DD format: ');
const birthdate = new Date(birthday);

function checkSign(birthdate, sign){//defining a function to check if the user is a specific star sign
    if (birthdate >= sign.startDate && birthdate <= sign.endDate){
        return true;
    } else{
        return false;
    }
}

let sign;
//loop to see which sign the user is 
for (let i =0; i < signs.length; i++){
    if (checkSign(birthdate, signs[i])){
        sign = signs[i];
        break;
    }else if (i === signs.length - 1){// the date function doesn't apply very well to the capricorn sign so I will use a catch case
        sign = signs[i];//they are a capricorn
    }
}
