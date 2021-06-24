const prompt = require('prompt-sync')({sigint: true});

const hat = '^';
const hole = 'O';
const fieldCharacter = '░';
const pathCharacter = '*';


//Creating the field class
class Field {
    constructor(field) {
        this._field = field;
        this._horizontalLocation = 0;
        this._verticalLocation = 0;
    }

    get field(){
        return this._field;
    }

    get horizontalLocation(){
        return this._horizontalLocation;
    }

    get verticalLocation(){
        return this._verticalLocation;
    }

    print() {
        for (let row of this._field) {
            console.log(row.join(''));
        }
    }

    checkState() {
        console.log(this._field[this._verticalLocation]);
        if (this._horizontalLocation >= this._field[this._verticalLocation].length || this._verticalLocation >= this._field.length) {
            return 0;
        } else if (this._field[this._verticalLocation][this._horizontalLocation] === hole){
            return 0;
        } else if (this._field[this._verticalLocation][this._horizontalLocation] === hat) {
            return 1;
        } else {
            return 2;
        }
    }

    move() {
        // 0: right, 1: left, 2: up, 3: down
        let input = Number(prompt('Type 0 to move right, 1 to move left, 2 to move up, and 3 to move down: '));
        while (![0,1,2,3].includes(input, 0)){
            input = Number(prompt('Please input the right number. Type 0 to move right, 1 to move left, 2 to move up, and 3 to move down: '));
        }
        if (input === 0) {
            this._horizontalLocation++;
        } else if (input === 1) {
            this._horizontalLocation--;
        } else if (input === 2) {
            this._verticalLocation--;
        } else if (input === 3) {
            this._verticalLocation++;
        }

        if (this.checkState() === 2) {
            this.updateField();
            this.print();
            return this.checkState();
        } else {
            return this.checkState();
        }
    }

    updateField() {
        this._field[this._verticalLocation][this._horizontalLocation] = pathCharacter;
    }

    static generateField(rows, cols) {
        const hatLocation = [Math.floor(Math.random() * rows), Math.floor(Math.random() * cols)]
        const newField = [];
        for (let i = 0; i < rows; i++) {
            let row = [];
            for (let j = 0; j < cols; j++) {
                if (i === hatLocation[0] && j === hatLocation[1]){
                    row.push(hat);
                } else if (i===0 && j===0) {
                   row.push(pathCharacter);
                } else {
                    let random = Math.floor(Math.random() * 2);
                    if (random === 0){
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
}


// creating a game function to play a game using recursion
let flag = true;//boolean flag
let game = true;
console.log("Welcome to find you hat");
while (flag) {

    let rows = Number(prompt('Enter the number of rows for the field'));
    let cols = Number(prompt('Enter the number of columns for the field'));
    let field = new Field(Field.generateField(rows, cols))
    field.print();
    while (game) {
        let turn = field.move();
        if (turn === 0){
            console.log("You lost");
            game = false;
        } else if (turn === 1){
            console.log('You won!')
        }
    } 
    let again = prompt("Type y if you want to continue playing. Type anything else to stop");
    if (again !== 'y') {
        flag = false;
    }
}