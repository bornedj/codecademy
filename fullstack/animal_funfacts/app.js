import { animals } from './animals';
import React from 'react'
import ReactDOM from 'react-dom'

//adding the background
const background = <img
className="background"
alt='ocean'
src='/images/ocean.jpg'/>;

//title element
const title = '';
//images array
let images = []
for (const animal in animals) {//getting image tags from the imported animals object
  let img = <img key={animal} className='animal' alt={animal} src={animals[animal].image} aria-label={animal} role='button'
  onClick={displayFact(document.getElementById(animal))}/>;
  images.push(img);
}

//display fact function will be passed to an event handler
const displayFact = e => {
  const animal = e.target.alt;
  const randIdx = Math.floor(Math.random()* animals[animal].facts.length);
  //saving the random fun fact about the animal
  const funFact = animals[animal].facts[randIdx];
  //changing the fact to the selected fact
  document.getElementById('fact').innerHTML = funFact;
}
//animalFacts is div container for the project
const animalFacts = (
  <div>
    <h1>{title === '' ? 'Click and animal for fun fact' : title}</h1>
    {background}
    <div className='animals'>
      {images}
    </div>
    <p id='fact'></p>
  </div>
);

//rendering
ReactDOM.render(animalFacts, document.getElementById('root'))