const prompt = require('prompt-sync')({sigint: true});

const hat = '^';
const hole = 'O';
const fieldCharacter = '░';
const pathCharacter = '*';


//Creating the field class
class Field {
    constructor(field) {
        this._field = field;
    }

    get field(){
        return this._field;
    }

    print() {
        for (row in this._field) {
            console.log(row.join(''));
        }
    }

}

const testField = new Field([['*', '░', 'O'],
  ['░', 'O', '░'],
  ['░', '^', '░'],]);

//testing print
testField.print();
