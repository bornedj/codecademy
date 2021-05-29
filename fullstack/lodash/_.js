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
    }

};
// // testing clamp
// console.log(_.clamp(5,10,15))
// console.log(_.clamp(17,10,15))


// Do not write or modify code below this line.
module.exports = _;