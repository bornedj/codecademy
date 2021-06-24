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

    move(direction) {
        // 0: right, 1: left, 2: up, 3: down
        if (direction === 0) {
            this._horizontalLocation++;
        } else if (direction === 1) {
            this._horizontalLocation--;
        } else if (direction === 2) {
            this._verticalLocation++;
        } else if (direction === 3) {
            this._verticalLocation--;
        }

        if (this.checkState() === 2) {
            this.updateField();
            this.print();
        } else {
            return this.checkState();
        }
    }

    updateField() {
        this._field[this._verticalLocation][this._horizontalLocation] = pathCharacter;
    }
}

const testField = new Field([['*', '░', 'O'],
  ['░', 'O', '░'],
  ['░', '^', '░'],]);

//testing print
testField.print();
console.log(testField.checkState());
console.log(testField.move(0));