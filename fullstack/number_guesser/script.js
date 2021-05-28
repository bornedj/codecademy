let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

//defining the function to determine the target of the guessing game
const generateTarget = () => num = Math.floor(Math.random() * 10);

//function will compare the guesses between the human and computer
function compareGuesses(human, computer, target){
    //absolute difference of guess
    const humanDiff = Math.abs(target - human);
    const computerDiff = Math.abs(target - computer);

    if (computerDiff < humanDiff){
        return false;
    }else{
        return true;
    }
}

function updateScore(string){
    if (string === 'human'){
        humanScore++;
    }else if (string === 'computer'){
        computerScore++;
    }
}

//testing some values for the written functions
/*let target = generateTarget();
console.log(5, 7, target)
console.log(compareGuesses(5, 7, target));*/