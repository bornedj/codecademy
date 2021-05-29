const _ = {
    //clamp function
    clamp(num, lower, upper){
        //setting up clamp using Math the way codecademy explains it
        num = Math.max(num, lower);
        return Math.min(num, upper);
    },

    //working on inRange
    inRange(num, start, end) {
        if (!end){
            end = start;
            start = 0;
        }else if(start > end){
            [start, end] = [end, start];
        }

        if (num < start || num >= end){
            return false;
        }else{
            return true;
        }
    },

    //words will split a string into words
    words(string){
        return string.split(' ');
    },

    //padding a string with spaces
    pad(string, len){
        if (string.length >= len){
            return string;
        }
        
        front = Math.floor((len - string.length) / 2);
        end = len - string.length - front;

        string = ' '.repeat(front) + string + ' '.repeat(end);

        return string;
    },

    //defining the has method
    has(obj, key){
        if (obj[key]){
            return true;
        }else{
            return false;
        }
    },

    //adding invert
    invert(obj){
        let tempObj = {};
        for (key in obj){
            tempObj[obj[key]] = key;
        }
        return tempObj;
    },

    //adding findkey
    findKey(obj, func){
        for (item in obj){
            if (func(obj[item])){
                return item;
            }
        }
        return undefined;
    },

    //adding drop, uses splice and defaults to dropping the first value
    drop(arr, num = 1) {
        arr.splice(0, num);
        return arr;
    },

    dropWhile(arr, func){
        let idx = 0;
        let element = arr[idx];
        while (func(element, idx, arr)){
            arr.shift()
            element = arr[idx]
        }
        return arr;
    },

    //adding chunk
    chunk(arr, size = 1){
        let newArr = [];
        while (arr.length > 0){//going to use slice
            if (arr.length <= size){
                newArr.push(arr.splice(0, arr.length))
            }else{
                newArr.push(arr.splice(0, size))
            }
        }
        return newArr;
    }
};
// // testing clamp
// console.log(_.clamp(5,10,15))
// console.log(_.clamp(17,10,15))

//testing the pad function, trying recursion
// console.log(_.pad('hello', 4))
// Do not write or modify code below this line.
module.exports = _;