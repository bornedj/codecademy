const prompt = require('prompt-sync')({sigint: true});

const hat = '^';
const hole = 'O';
const fieldCharacter = '░';
const pathCharacter = '*';

class Field {
    constructor(field) {
        this._field = field;
        this.horizontalLocation = 0;
        this.verticalLocation = 0;
    }

    get field() {
        return this._field;
    }

    //function to print out the field in a readable fashion
    print() {
        for (let row of this._field){
            console.log(row.join(''));
        }
    }

    static generateField(rows, cols) {//function to generate a random field
        let hatLocaiton;
        do {
            hatLocaiton = [Math.floor(Math.random() * rows), Math.floor(Math.random() * cols)];
        } while (hatLocaiton === [0,0])
        const newField = [];
        for (let i = 0; i < rows; i++) {//loop for the number of rows

            let row = [];
            for (let j = 0; j < cols; j++) {
                if (i === hatLocaiton[0] && j === hatLocaiton[1]){row.push(hat)}
                else if (i===0 && j === 0){row.push(pathCharacter)}
                else {
                    let random = Math.floor(Math.random() * 2);
                    if (random === 0) {
                        row.push(hole);
                    } else {
                        row.push(fieldCharacter);
                    }
                }
            }
            newField.push(row);
        }
        return newField; 
    }

    //function to check the if the location the user is on
    checkState() {
        //0 is lost, 1 is won and 2 is in progress game
        if (this.verticalLocation < 0 || this.horizontalLocation < 0) {
            return 0;
        } else if (this.horizontalLocation > this._field[this.verticalLocation].length || this.verticalLocation > this._field.length) {
            return 0;
        } else if (this._field[this.verticalLocation][this.horizontalLocation] === hole) {
            return 0;
        } else if (this._field[this.verticalLocation][this.horizontalLocation] === hat){
            return 1;
        } else {
           return 2; 
        }
    }

    //takes user input and moves on the board
    move() {
        let input;
        do {
            input = Number(prompt('Type 0 to move right, 1 to move left, 2 to move up, and 3 to move down'))
        } while (![0,1,2,3].includes(input, 0));//checks to see if the number is in 0,1,2,3 if it is continue the function

        if (input === 0){//move right
            this.horizontalLocation++;
        } else if (input === 1) {
            this.horizontalLocation--;
        } else if (input === 2) {
            this.verticalLocation--;
        } else {
            this.verticalLocation++;
        }

        //check the game state and return the value
        const state = this.checkState();
        if (state === 2) {//if the game is still in play
            this._field[this.verticalLocation][this.horizontalLocation] = pathCharacter;//add to the path
            this.print();
        } else if (state === 0) {
            console.log('You lost')
        } else {
            console.log('You won')
        }
        
    }
}


// const test = new Field(Field.generateField(3,3));
const test = new Field([
  ['*', '░', 'O'],
  ['░', 'O', '░'],
  ['░', '^', '░']
]);
test.print();
test.move();
test.move();