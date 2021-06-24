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

    print() {
        for (let row of this._field){
            console.log(row.join(''));
        }
    }

    static generateField(rows, cols) {
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
}


const test = new Field(Field.generateField(3,3));
test.print();