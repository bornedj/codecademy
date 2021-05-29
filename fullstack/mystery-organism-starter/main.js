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
const pAequorFactory = (number, arr){//number is the number of the dna, arr is an array of 15 dna bases(1 strand)
  return {//return obj
    specimenNum: number,
    dna: arr
  }

}





