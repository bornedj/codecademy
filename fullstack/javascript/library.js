class Media {
    constructor(title){
        this._title = title;
        this._ratings = [];
        this._isCheckedOut = false;
    }

    get title() {
        return this._title;
    }

    get ratings() {
        return this._ratings;
    }

    get isCheckedOut() {
        return this._isCheckedOut;
    }

    set isCheckedOut(value) {
        this._isCheckedOut = value;
    }

    toggleCheckOutStatus() {
        this._isCheckedOut ? this._isCheckedOut = false : this._isCheckedOut = true;
    }

    //returns the average of the ratings array using reduce
    getAverageRating() {
        return this._ratings.reduce((accum, currentValue) => accum + currentValue, 0) / this._ratings.length;
    }

    addRating(rating) {
        this._ratings.push(rating);
    }

}

// book subclass only adds the author property
class Book extends Media {
    constructor(title, author, pages) {
        super(title);
        this._author = author;
        this._pages = pages;
    }

    get author() {
        return this._author;
    }

    get pages() {
        return this._pages;
    }

}

// movie sub class will add director and runtime
class Movie extends Media {
    constructor(title, director, runTime) {
        super(title);
        this._director = director;
        this._runTime = runTime;
    }

    get director() {
        return this._director;
    }

    get runTime() {
        return this._runTime;
    }

}

const historyOfEverything = new Book('A short history of nearly everything', 'Bill Byrson', 544);
historyOfEverything.toggleCheckOutStatus;
console.log(historyOfEverything.isCheckedOut);
historyOfEverything.addRating(4);
historyOfEverything.addRating(5);
historyOfEverything.addRating(5);
console.log(historyOfEverything.getAverageRating());