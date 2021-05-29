const { throws } = require("node:assert");
const { count } = require("node:console");

// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G'];
  return dnaBases[Math.floor(Math.random() * 4)];
};

// Returns a random single stand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = [];
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase());
  }
  return newStrand;
};


//we will need to create several of these dna strands: making factory
const pAequorFactory = (number, arr) => {//number is the number of the dna, arr is an array of 15 dna bases(1 strand)
  return {//return obj
    specimenNum: number,
    dna: arr,
    mutate() {//mutate function changes a selected dna base and changes it to another one
      const strandIdx = Math.floor(Math.random()*15);// gets a random number between 0 - 14 inclusive
      const currentStrand = this.dna[strandIdx]//assings it the current strand value
      let pos;
      do{//using do while to generate a new value for current strand
        pos = returnRandBase();//pos for possible value
      }while (pos === currentStrand)

      //change the strand
      this.dna[strandIdx] = pos;
    },// end mutate
    compareDNA(pAequor) {//checks two strands of dna, if value == at == index increment counter, return formatted string
      let counter = 0;
      for (let i = 0; i < this.dna.length; i++){//loop through dna length
        if (this.dna[i] === pAequor.dna[i]){
          counter++;
        }
      }//end for
      const percentage = Math.floor((counter / this.dna.length) * 100);
      console.log(`Specimen ${this.specimenNum} and specimen ${pAequor.specimenNum} have ${percentage}% in common.`)
    }
  }

}





