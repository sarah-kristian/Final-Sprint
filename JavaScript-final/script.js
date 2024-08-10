// ANSI escape codes for styling
const reset = "\x1b[0m";
const bold = "\x1b[1m";
const underline = "\x1b[4m";



function printJson(obj, indent = 2) {
  const spacing = ' '.repeat(indent);
  for (let key in obj) {
      if (typeof obj[key] === 'object' && !Array.isArray(obj[key])) {
          console.log(`${spacing}${key}:`);
          printJson(obj[key], indent + 2);
      } else if (Array.isArray(obj[key])) {
          console.log(`${spacing}${key}:`);
          obj[key].forEach(item => console.log(`${spacing}  - ${item}`));
      } else {
          console.log(`${spacing}${key}: ${obj[key]}`);
      }
  }
}

// Functions 1 & 3 (for step 5)

// FUNCTION 1a: return random items from lists

function getRandomItem(array) {
  // Generate a random index between 0 and array.length - 1
  const randomIndex = Math.floor(Math.random() * array.length);
  // Return the item at that index
  return array[randomIndex];  
}


// FUNCTION 1b: select random index number from array

function getRandomIndex(array) {
  // Generate a random index between 0 and array.length - 1
  const randomIndex = Math.floor(Math.random() * array.length);
  // Return the item at that index
  return randomIndex;
}


// FUNCTION 2: return random items from lists
// Use this as a Method to create a randomly generated instance of a story
function getRandomVersion(animateNouns, inanimateNouns, adjectives, verbs) {
  let randomIndex 

  randomIndex = getRandomIndex(animateNouns.singular);
  let noun1a = animateNouns.singular[randomIndex];
  let noun1b = animateNouns.plural[randomIndex];

  randomIndex = getRandomIndex(animateNouns.singular);
  let noun2a = animateNouns.singular[randomIndex];
  let noun2b = animateNouns.plural[randomIndex];

  randomIndex = getRandomIndex(inanimateNouns.singular);
  let noun3a = inanimateNouns.singular[randomIndex];
  let noun3b = inanimateNouns.plural[randomIndex];

  randomIndex = getRandomIndex(inanimateNouns.singular);
  let noun4a = inanimateNouns.singular[randomIndex];
  let noun4b = inanimateNouns.plural[randomIndex];

  let adj1 = getRandomItem(adjectives);
  let adj2 = getRandomItem(adjectives);
  let adj3 = getRandomItem(adjectives);
  let adj4 = getRandomItem(adjectives);
  let adj5 = getRandomItem(adjectives);

  randomIndex = getRandomIndex(verbs.present);
  let verb1a = verbs.present[randomIndex];
  let verb1b = verbs.past[randomIndex];

  randomIndex = getRandomIndex(verbs.present);
  let verb2a = verbs.present[randomIndex];
  let verb2b = verbs.past[randomIndex];

  const randomVersion = new storyVersion(
    noun1a, noun1b,
    noun2a, noun2b,
    noun3a, noun3b,
    noun4a, noun4b,
    adj1, adj2, adj3, adj4, adj5,
    verb1a, verb1b,
    verb2a, verb2b,
    );

  return randomVersion;  
  }


// Story class so we can create multiple versions of the story

class storyVersion {
  constructor(noun1a, noun1b, noun2a, noun2b, noun3a, noun3b, noun4a, noun4b, adj1, adj2, adj3, adj4, adj5, verb1a, verb1b, verb2a, verb2b, prep) {
    this.noun1 = {
      noun1a: noun1a
      ,noun1b: noun1b
    };
    this.noun2 = {
      noun2a: noun2a
      ,noun2b: noun2b
    };
    this.noun3 = {
      noun3a: noun3a
      ,noun3b: noun3b
    };
    this.noun4 = {
      noun4a: noun4a
      ,noun4b: noun4b
    };
    this.adj1 = adj1;
    this.adj2 = adj2;
    this.adj3 = adj3;
    this.adj4 = adj4;
    this.adj5 = adj5;
    this.verb1 = {
      verb1a: verb1a
      ,verb1b: verb1b
    };
    this.verb2 = {
      verb2a: verb2a
      ,verb2b: verb2b
    };
    this.prep = prep;
  }


  // Story Methods (relevant for step 5)

  // FUNCTION 3: concatenate random adjectives to the nouns
  // Method to grown nouns in story with random adjectives (N = Adj + N)

  growNoun(adjectives) {
    const newAdj1 = getRandomItem(adjectives);
    const newAdj2 = getRandomItem(adjectives);
    const newAdj3 = getRandomItem(adjectives);
    const newAdj4 = getRandomItem(adjectives);

    this.noun1.noun1a = newAdj1 + " " + this.noun1.noun1a;
    this.noun1.noun1b = newAdj1 + " " + this.noun1.noun1b;
    this.noun2.noun2a = newAdj2 + " " + this.noun2.noun2a;
    this.noun2.noun2b = newAdj2 + " " + this.noun2.noun2b;
    this.noun3.noun3a = newAdj3 + " " + this.noun3.noun3a;
    this.noun3.noun3b = newAdj3 + " " + this.noun3.noun3b;
    this.noun4.noun4a = newAdj4 + " " + this.noun4.noun4a;
    this.noun4.noun4b = newAdj4 + " " + this.noun4.noun4b;
  }

  // FUNCTION 4: Method to create a story
  // Method to create a story with the current values of the instance and
  // a template literal string

  getStory() {
    return `
    A RETELLING OF THE THREE ${underline}${bold}${this.adj1.toUpperCase()}${reset} ${underline}${bold}${this.noun1.noun1b.toUpperCase()}${reset}
    
    Once upon a time there were three ${underline}${bold}${this.adj1}${reset} ${underline}${bold}${this.noun1.noun1b}${reset} who lived on the same street. One day, a(n) ${underline}${bold}${this.noun2.noun2a}${reset} happened to pass by the street where the three ${underline}${bold}${this.adj1}${reset} ${underline}${bold}${this.noun1.noun1a}${reset} lived. She stopped at the first house that was made of ${underline}${bold}${this.noun3.noun3a}${reset} and she smelled the ${underline}${bold}${this.noun1.noun1a}${reset} inside. She thought the ${underline}${bold}${this.noun1.noun1a}${reset} would make a mighty ${underline}${bold}${this.adj2}${reset} meal and her mouth began to water. So she knocked on the door and said: “${underline}${bold}${this.adj1}${reset} ${underline}${bold}${this.noun1.noun1a}${reset}! ${underline}${bold}${this.adj1}${reset} ${underline}${bold}${this.noun1.noun1a}${reset}! Let me in!”
    
    But the ${underline}${bold}${this.adj1}${reset} ${underline}${bold}${this.noun1.noun1a}${reset} saw the ${underline}${bold}${this.noun2.noun2a}${reset}'s ${underline}${bold}${this.adj3}${reset} paws through the keyhole, so he answered back: “No! Not by the hairs on my chinny chin chin!”

    Then the ${underline}${bold}${this.noun2.noun2a}${reset} showed her teeth and said: “Then I’ll ${underline}${bold}${this.verb1.verb1a}${reset} and ${underline}${bold}${this.verb2.verb2a}${reset} and blow your house in.”

    So she started to ${underline}${bold}${this.verb1.verb1a}${reset} and to ${underline}${bold}${this.verb2.verb2a}${reset} and she blew the house down! The ${underline}${bold}${this.noun2.noun2a}${reset} opened her jaws very wide and bit down as hard as she could, but the first ${underline}${bold}${this.adj1}${reset} ${underline}${bold}${this.noun1.noun1a}${reset} escaped and ran away to hide with the second ${underline}${bold}${this.adj1}${reset} ${underline}${bold}${this.noun1.noun1a}${reset}.

    The second house (a stick house) went much like the first house, and now there were three ${underline}${bold}${this.adj1}${reset} ${underline}${bold}${this.noun1.noun1b}${reset} hiding in one brick house.
    
    The ${underline}${bold}${this.noun2.noun2a}${reset} hadn't eaten all day and she had worked up a(n) ${underline}${bold}${this.adj4}${reset} appetite, chasing the ${underline}${bold}${this.adj1}${reset} ${underline}${bold}${this.noun1.noun1b}${reset} around. She stood outside the brick house. Though it was much sturdier than the other houses, she could still smell all three of the ${underline}${bold}${this.noun1.noun1b}${reset} inside. She knew that they would make a(n) ${underline}${bold}${this.adj5}${reset} ${underline}${bold}${this.noun4.noun4a}${reset}.
    
    So, the ${underline}${bold}${this.noun2.noun2a}${reset} knocked on the door and said: "${underline}${bold}${this.adj1}${reset} ${underline}${bold}${this.noun1.noun1b}${reset}! ${underline}${bold}${this.adj1}${reset} ${underline}${bold}${this.noun1.noun1b}${reset}! Let me in!"

    But the ${underline}${bold}${this.adj1}${reset} ${underline}${bold}${this.noun1.noun1b}${reset} saw the ${underline}${bold}${this.noun2.noun2a}${reset}'s narrow eyes through the keyhole, so they answered back:  "No! No! No! Not by the hairs on our chinny chin chin!"

    So the ${underline}${bold}${this.noun2.noun2a}${reset} showed her teeth and said: “Then I’ll ${underline}${bold}${this.verb1.verb1a}${reset} and I’ll ${underline}${bold}${this.verb2.verb2a}${reset} and I’ll blow your house in!”

    Well, she ${underline}${bold}${this.verb1.verb1b}${reset} and she ${underline}${bold}${this.verb2.verb2b}${reset}. She ${underline}${bold}${this.verb2.verb2b}${reset} and she ${underline}${bold}${this.verb1.verb1b}${reset}. And she ${underline}${bold}${this.verb1.verb1b}${reset}, ${underline}${bold}${this.verb1.verb1b}${reset}, and she ${underline}${bold}${this.verb2.verb2b}${reset}, ${underline}${bold}${this.verb2.verb2b}${reset}; but she could not blow the house down. At last, the ${underline}${bold}${this.noun2.noun2a}${reset} was so out of breath that she couldn't ${underline}${bold}${this.verb1.verb1a}${reset} and she couldn't ${underline}${bold}${this.verb2.verb2a}${reset} anymore. So, she left and went to the restaurant further down the street.
    `;
  }


// Functions for formatted HTML strings

  // HTML STRING FUNCTION 2: concatenate random adjectives to the nouns
  // Method to generate HTML representation of the object (corresponds to FUNCTION 3)
  getObjectHTML() {
    return `
      <p><strong>Noun1:</strong> <u class="noun">${this.noun1.noun1a}, ${this.noun1.noun1b}</u></p>
      <p><strong>Noun2:</strong> <u class="noun">${this.noun2.noun2a}, ${this.noun2.noun2b}</u></p>
      <p><strong>Noun3:</strong> <u class="noun">${this.noun3.noun3a}, ${this.noun3.noun3b}</u></p>
      <p><strong>Noun4:</strong> <u class="noun">${this.noun4.noun4a}, ${this.noun4.noun4b}</u></p>
      <p><strong>Adjectives:</strong> <u class="adj">${this.adj1}, ${this.adj2}, ${this.adj3}, ${this.adj4}, ${this.adj5}</u></p>
      <p><strong>Verbs 1:</strong> <u class="verb">${this.verb1.verb1a}, ${this.verb1.verb1b}</u></p>
      <p><strong>Verbs 2:</strong> <u class="verb">${this.verb2.verb2a}, ${this.verb2.verb2b}</u></p>
    `;
  }


  // HTML STRING FUNCTION 3: concatenate random adjectives to the nouns
  growNounStr(adjectives) {
    const nAdj1 = getRandomItem(adjectives);
    const nAdj2 = getRandomItem(adjectives);
    const nAdj3 = getRandomItem(adjectives);
    const nAdj4 = getRandomItem(adjectives);

    return `
    <u class="noun">${this.noun1.noun1a}</u> --> <u class="adj">${nAdj1}</u> <u class="noun">${this.noun1.noun1a}</u><br />
    <u class="noun">${this.noun1.noun1b}</u> --> <u class="adj">${nAdj1}</u> <u class="noun">${this.noun1.noun1b}</u><br />
    <u class="noun">${this.noun2.noun2a}</u> --> <u class="adj">${nAdj2}</u> <u class="noun">${this.noun2.noun2a}</u><br />
    <u class="noun">${this.noun2.noun2b}</u> --> <u class="adj">${nAdj2}</u> <u class="noun">${this.noun2.noun2b}</u><br />
    <u class="noun">${this.noun3.noun3a}</u> --> <u class="adj">${nAdj3}</u> <u class="noun">${this.noun3.noun3a}</u><br />
    <u class="noun">${this.noun3.noun3b}</u> --> <u class="adj">${nAdj3}</u> <u class="noun">${this.noun3.noun3b}</u><br />
    <u class="noun">${this.noun4.noun4a}</u> --> <u class="adj">${nAdj4}</u> <u class="noun">${this.noun4.noun4a}</u><br />
    <u class="noun">${this.noun4.noun4b}</u> --> <u class="adj">${nAdj4}</u> <u class="noun">${this.noun4.noun4b}</u><br />`;
  }

  // HTML STRING FUNCTION 4: print the story in html
  getStoryHTML() {
    return `A RETELLING OF THE THREE <u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1b}</u><br /><br />
    
    Once upon a time there were three <u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1b}</u> who lived on the same street. One day, a(n) <u class="noun">${this.noun2.noun2a}</u> happened to pass by the street where the three <u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1a}</u> lived. She stopped at the first house that was made of <u class="noun">${this.noun3.noun3a}</u> and she smelled the <u class="noun">${this.noun1.noun1a}</u> inside. She thought the <u class="noun">${this.noun1.noun1a}</u> would make a mighty <u class="adj">${this.adj2}</u> meal and her mouth began to water. So she knocked on the door and said: “<u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1a}</u>! <u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1a}</u>! Let me in!”<br /><br />
    But the <u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1a}</u> saw the <u class="noun">${this.noun2.noun2a}</u>'s <u class="adj">${this.adj3}</u> paws through the keyhole, so he answered back: “No! Not by the hairs on my chinny chin chin!”<br /><br />
    Then the <u class="noun">${this.noun2.noun2a}</u> showed her teeth and said: “Then I’ll <u class="verb">${this.verb1.verb1a}</u> and <u class="verb">${this.verb2.verb2b}</u> and blow your house in.”<br /><br />
    So she started to <u class="verb">${this.verb1.verb1a}</u> and to <u class="verb">${this.verb2.verb2a}</u> and she blew the house down! The <u class="noun">${this.noun2.noun2a}</u> opened her jaws very wide and bit down as hard as she could, but the first <u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1a}</u> escaped and ran away to hide with the second <u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1a}</u>.<br /><br />
    The second house (a stick house) went much like the first house, and now there were three <u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1b}</u> hiding in one brick house.  <br /><br />
    
    The <u class="noun">${this.noun2.noun2a}</u> hadn't eaten all day and she had worked up a(n) <u class="adj">${this.adj4}</u> appetite, chasing the <u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1b}</u> around. She stood outside the brick house. Though it was much sturdier than the other houses, she could still smell all three of the <u class="noun">${this.noun1.noun1b}</u> inside. She knew that they would make a(n) <u class="adj">${this.adj5}</u> <u class="noun">${this.noun4.noun4a}</u>. <br /><br />
    
    So, the <u class="noun">${this.noun2.noun2a}</u> knocked on the door and said: "<u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1b}</u>! <u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1b}</u>! Let me in!"<br /><br />
    But the <u class="adj">${this.adj1}</u> <u class="noun">${this.noun1.noun1b}</u> saw the <u class="noun">${this.noun2.noun2a}</u>'s narrow eyes through the keyhole, so they answered back:  "No! No! No! Not by the hairs on our chinny chin chin!"<br /><br />
    So the <u class="noun">${this.noun2.noun2a}</u> showed her teeth and said: “Then I’ll <u class="verb">${this.verb1.verb1a}</u> and I’ll <u class="verb">${this.verb2.verb2a}</u> and I’ll blow your house in!”<br /><br />
    Well, she <u class="verb">${this.verb1.verb1b}</u> and she <u class="verb">${this.verb2.verb2b}</u>. She <u class="verb">${this.verb2.verb2b}</u> and she <u class="verb">${this.verb1.verb1b}</u>. And she <u class="verb">${this.verb1.verb1b}</u>, <u class="verb">${this.verb1.verb1b}</u>, and she <u class="verb">${this.verb2.verb2b}</u>, <u class="verb">${this.verb2.verb2b}</u>; but she could not blow the house down. At last, the <u class="noun">${this.noun2.noun2a}</u> was so out of breath that she couldn't <u class="verb">${this.verb1.verb1a}</u> and she couldn't <u class="verb">${this.verb2.verb2a}</u> anymore. So, she left and went to the restaurant further down the street.<br /><br />
    `;
  }

}



// STEPS FOR THE PROJECT
  // Create an instance of the Story class

// Step 1: Testing script.js is linked to index and will print to console
console.log('Step 1: script.js is linked to index.html.');

// Step 2: Create a JSON file with sample data
console.log('Step 2: storyData.joson file created with sample data.');


// Step 3: Fetch data from local JSON file
console.log('Step 3: Fetch data from local JSON file.');

fetch('storyData.json')
    .then(response => response.json())
    .then(data => {
      const animateNouns = data.wordLists.animateNouns;
      const inanimateNouns = data.wordLists.inanimateNouns;
      const adjectives = data.wordLists.adjectives;
      const verbs = data.wordLists.IVs;          

// Step 4: Loop through data and print to console.

        console.log('Step 4: Loop through data and print to console.');

        // Loop through all data (<-- this is a recursive function from chatGPT; my version follows, but is commented out)
        // if the data contains a nested object, print the key, then loop through the nested object
        // if the data contains an array, print the key, then loop through the array
        // otherwise, print the key and value

        printJson(data);
      
        // Loop through all data (<-- Sarah's version)

        // console.log("  a) loop through all data:");
        // for (const key in data) {
        //     console.log(`     ${key}: ${data[key]}`);
        // }
        
        // // Loop through Wordlists
        // console.log("  b) loop through Wordlists:");
        // for (const key in data.wordLists) {
        //     console.log(`     ${key}: ${data.wordLists[key]}`);
        // }
        
        // // Loop through default values
        // console.log("  c) loop through Default Values:");
        // for (const key in data.defaultValues) {
        //     console.log(`     ${key}: ${data.defaultValues[key]}`);
        // }



// Before we go further, we need to process some data. 

          let nounPairs = []
          let adjList = []
          let verbPairs = []

    // get nouns
          if (animateNouns && animateNouns.singular) {
            animateNouns.singular.forEach((noun, index) => {
                // Save each pair as an array [singular, plural]
                nounPairs.push([noun, animateNouns.plural[index]]);
            });
        } else {
            console.error('The animateNouns or singular is not defined in the JSON data');
        }

          if (inanimateNouns && inanimateNouns.singular) {
          inanimateNouns.singular.forEach((noun, index) => {
              // Save each pair as an array [singular, plural]
              nounPairs.push([noun, inanimateNouns.plural[index]]);
          });
          } else {
            console.error('the (in)animate noun or singular is not defined in the JSON data');
          }

    // get adjectives
          adjectives.forEach((adj) => {
            adjList.push(adj);
          });

    // get verbs
          if (verbs && verbs.present) {
            verbs.present.forEach((verb, index) => {
                // Save each pair as an array [present, past]
                verbPairs.push([verb, verbs.past[index]]);
            });
          } else {
            console.error('the verb or present is not defined in the JSON data');
          }

          
    // get random items
        let randomAdj = getRandomItem(adjectives);
        let randomVerbIndex = getRandomIndex(verbs.present);
        let randomPresVerb = verbs.present[randomVerbIndex];
        let randomPastVerb = verbs.past[randomVerbIndex];
        
    // Create an instance of a story using random values
        const randomVersion = getRandomVersion(animateNouns, inanimateNouns, adjectives, verbs);
              

    // Create an instance of a story using default data
           const williamVersion = new storyVersion(
            data.defaultValues.noun1a,
            data.defaultValues.noun1b,
            data.defaultValues.noun2a,
            data.defaultValues.noun2b,
            data.defaultValues.noun3a,
            data.defaultValues.noun3b,
            data.defaultValues.noun4a,
            data.defaultValues.noun4b,
            data.defaultValues.adj1,
            data.defaultValues.adj2,
            data.defaultValues.adj3,
            data.defaultValues.adj4,
            data.defaultValues.adj5,
            data.defaultValues.verb1a,
            data.defaultValues.verb1b,
            data.defaultValues.verb2a,
            data.defaultValues.verb2b,
        );
        

// Step 5: Describing the contents of the JSON file with functions.
// Or rather, we will create functions that return strings of the data.

        // Display HTML
        document.getElementById('funct0').innerHTML += williamVersion.getObjectHTML();
        document.getElementById('funct1a').innerHTML += `Random adjective: <u class="adj">${randomAdj}</u>`;
        document.getElementById('funct1b').innerHTML += `Random verb pair: <u class="verb">${randomPresVerb}, ${randomPastVerb}</u>`;
        document.getElementById('funct2').innerHTML += randomVersion.getObjectHTML();
        document.getElementById('funct3').innerHTML += randomVersion.growNounStr(adjectives);
        document.getElementById('funct4').innerHTML += randomVersion.getStoryHTML();


        // Display in console

        console.log('');        
        console.log('Step 5: Displaying the contents of the JSON file with functions.');
        console.log('  - The data contains word lists for nouns, adjectives, and verbs and default values for a story.');
        console.log('  - We can use these to along with a class to play something like madLibs!')

        console.log('  ');
        console.log('First let us make the an instance of the class storyVersion using a set of default values');
        console.log('  Default instance:', williamVersion);
        console.log('  ');

        console.log('Now, let us create an instance of the class by randomly choosing items from the correct word lists');
        console.log('  ');
        console.log('  FUNCTION 1a returns random items from lists');
        console.log('      example usage: getRandomItem(adjectives):', randomAdj);

        console.log('  ');
        console.log('  FUNCTION 1b selects random index number from array');
        console.log('      example usage: getRandomIndex(verbs.present):', randomVerbIndex);
        console.log('      example: verb pair:', randomPresVerb, randomPastVerb);
        console.log('  ');
        console.log('  FUNCTION 2 returns an instance of the class storyVersion using the random words');
        console.log('      example usage: getRandomVersion(animateNouns, inanimateNouns, adjectives, verbs):', randomVersion);
        
        console.log('  ');

        console.log('Now that we have a random story, we can use the class methods to manipulate the story.');
        console.log('  FUNCTION 3 adds an adjective in front of each noun: ');

        

        console.log('  ');
        console.log('  FUNCTION 4 applies an instance to a template literal, giving us a retelling of The Three Little Pigs.');
        randomVersion.growNoun(adjectives);
        console.log(randomVersion.getStory());

        console.log('  ');
        console.log('If you would like to try it out, you can! Options are on the webpage.')




     
    
})    
.catch(error => {
  console.error('Error fetching data:', error);
});