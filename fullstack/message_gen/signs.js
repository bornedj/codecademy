// this file will create the object literals that I will use to create the random messages.

//array of all the signs
const signNames = ['Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn']
//array of all their starting and ending dates
const signDates = [[new Date('01-20'),new Date('02-18')], [new Date('02-19'), new Date('03-20')], [new Date('03-21'), new Date('04-19')],
[new Date('04-20'), new Date('05-20')], [new Date('05-21'), new Date('06-20')], [new Date('06-21'), new Date('07-22')],
[new Date('07-23'), new Date('08-22')], [new Date('08-23'), new Date('09-22')], [new Date('09-23'), new Date('10-22')], 
[new Date('10-23'), new Date('11-21')], [new Date('11-22'), new Date('12-21')], [new Date('12-22'), new Date('01-19')]];


//will be an array of arrays: first option will be the time that the reading references, the second will be the type of message,
// and the third will be whether or not the message is good bad or neutral
const messageComponents = [
    ['Today,', 'In the recent past,', 'In the near future,'],//reference of time
    [' your love life ', ' your professional life ', ' your home life '],
    [//need two lists for the different tenses
        ['will be horrible.', 'will not see major changes.', 'will become incredible.'],
        ['has been horrible', 'has not seen major changes', 'has become incredible.']
    ]
]

//using a factory function to create an object for each star sign
const signFactory = (name, startDate, endDate, messages) => {
    return {
        name,
        startDate,
        endDate,
        messages,
        generateRand(){//getting random number between 0-2
            return Math.floor(Math.random() * 3);
        },
        generateMessage(){//function to create a message from the components passed in 
            // we need to know the time for the third option
            const randFirst = this.generateRand();
            const first = this.messages[0][randFirst];//random time
            const second = this.messages[1][this.generateRand()];
            if (randFirst === 1){
                const third = this.messages[2][1][this.generateRand()];
            }else{
                const third = this.messages[2][0][this.generateRand()];
            }
            
            return first + second + third;
        }
    }
};

//will loop through later to create the objects
let signObjs = [];//will store all of the signs objects
for (let i = 0; i < signNames.length; i++){
    signObjs.push(signFactory(signNames[i],signDates[i][0], signDates[i][1], messageComponents));
};


console.log(signObjs[0].generateMessage());
module.exports = signObjs;