// this file will create the object literals that I will use to create the random messages.
//array of all the signs
const signNames = ['Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn']
//array of all their starting and ending dates
const signDates = [[new Date('01-20'),new Date('02-18')], [new Date('02-19'), new Date('03-20')], [new Date('03-21'), new Date('04-19')],
[new Date('04-20'), new Date('05-20')], [new Date('05-21'), new Date('06-20')], [new Date('06-21'), new Date('07-22')],
[new Date('07-23'), new Date('08-22')], [new Date('08-23'), new Date('09-22')], [new Date('09-23'), new Date('10-22')], 
[new Date('10-23'), new Date('11-21')], [new Date('11-22'), new Date('12-21')], [new Date('12-22'), new Date('01-19')]];

//using a factory function to create an object for each star sign
const signFactory = (name, startDate, endDate, messages) => {
    return {

    }
};

console.log(signDates);