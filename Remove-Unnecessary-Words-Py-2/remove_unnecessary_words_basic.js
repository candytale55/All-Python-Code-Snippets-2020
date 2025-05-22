let story = 'Last weekend, I took literally the most beautiful bike ride of my life. The route is called "The 9W to Nyack" and it actually stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it basically took me an entire day. I stopped at Riverbank State Park to take some extremely artsy photos. It was a short stop, though, because I had a really long way left to go. After a quick photo op at the very popular Little Red Lighthouse, I began my trek across the George Washington Bridge into New Jersey.  The GW is actually very long - 4,760 feet! I was already very tired by the time I got to the other side.  An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautiful park along the coast of the Hudson.  Something that was very surprising to me was that near the end of the route you actually cross back into New York! At this point, you are very close to the end.';


// The string "story" splitted into individual words in array storyWords.
let storyWords = story.split(' ');
//console.log(storyWords); // Testing

let unnecessaryWords = ['extremely', 'literally', 'actually' ];

// The words inside storyWords are compared to unnecessaryWords and counted.
extremelyCount = 0;
literallyCount = 0;
actuallyCount = 0;

for (word of storyWords){
  if (word === "extremely"){
    extremelyCount ++;
  } else if (word === "literally"){
    literallyCount ++;
  } else if (word === "actually"){
    actuallyCount ++;
  }
}

console.log("Extremely: " + extremelyCount + " , Literally: " + literallyCount + " , Actually: " + actuallyCount);


// words in storyWords are compared to unnecessaryWords and if matched they are not added to new array filteredWords. The result is that unnecessaryWords are removed from the text. The way to return only words that are not a match with any unnecessaryWords is the "!" sign. 

let filteredWords =  storyWords.filter(function(word){
    return !unnecessaryWords.includes(word)
  })
  //console.log(filteredWords);
  console.log(filteredWords.join(" "));
  
