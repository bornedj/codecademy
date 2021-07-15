const express = require('express');
const app = express();

const { quotes } = require('./data');
const { getRandomElement } = require('./utils');

const PORT = process.env.PORT || 4001;

app.use(express.static('public'));

// get all quotes
app.get('/api/quotes', (req, res, next) => {
    res.send({quotes: quotes})
})

// get random quotes
app.get('/api/quotes/random', (req, res, next) => {
    const element = getRandomElement(quotes);
    const toReturn = {
        quote: element
    }
    res.send(toReturn)
})

// post new quote
app.post('/api/quotes', (req, res, next) => {
    if (req.query.quote && req.query.person) {
        quotes.push({quote: req.query.quote, person: req.query.person});
        res.status(201).send({quote: {quote: req.query.quote, person: req.query.person}})
    } else {
        res.status(400).send();
    }
})

app.listen(PORT, () => {
    console.log('app is listening');
})