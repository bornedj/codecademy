class School {
    constructor(name, level, numberOfStudents){
        this._name = name;
        this._level = level;
        this._numberOfStudents = numberOfStudents;
    }

    get name() {
        return this._name;
    }

    get level() {
        return this._level;
    }

    get numberOfStudents() {
        return this._numberOfStudents;
    }

    set numberOfStudents(students) {
        if (typeof(students) === 'number') {
            this._numberOfStudents = students;
        } else {
            console.log('Invalid: please input a number');
        }
    }

    quickFacts() {
        console.log(`${this._name} educates ${this._numberOfStudents} at the ${this._level} level.`);
    }

    static pickSubstituteTeacher(substituteTeacher) {
        const index = Math.floor(Math.random() * substituteTeacher.length);
        return substituteTeacher[index];
    }
}