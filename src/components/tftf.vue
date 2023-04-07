<template>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <div>
    <h2 v-if="course_name || course">
      <div class="course-code" v-if="course">for {{course}}: </div>
      <div class="course-name" v-if="course_name">{{course_name}}</div>
    </h2>
    <p>
      The Thing From the Future is an imagination game meant to spur creative and critical thinking.<br>
      To play the game, you draw a set of cards that prompt you to create an object from an alternative future.
    </p>
  </div>

  <div class="wrapper">
    <div class="box a">
      <p> ARC </p>
      <h3>{{ current['arc'] }}</h3>
    </div>
    <div class="box b">
      <p> OBJECT </p>
      <h3> there is a <br><em>{{ current['object'] }}</em></h3>
    </div>
    <div class="box c">
      <p> TERRAIN </p>
      <h3> related to <br><em>{{ current['terrain'] }}</em>.</h3>
    </div>
    

    
  </div>
  
  <div class="app">
    <br>
    <p><button v-on:click="deal_cards()" class="btn btn-primary">Deal Cards</button></p>
    <br>
    <h2><i> What is it? </i></h2>
    <p>
      Use <a v-bind:href="form_link">this template</a> to respond to the prompt. 
      <br>
    </p>  
    <br/>
    <h2> About the card decks: </h2>
      <ul class="list-group">
        <li v-for="(deck, index) in card_decks" :key="index">{{deck.desc}}</li>
        <br>
        <li><i> Drawn a wildcard? Fill in your own idea! </i></li>
      </ul>
      <br>
  </div>

  <div>
    <p>
      Made by <a href="https://www.lib.ncsu.edu/spaces/innovation-studio">the Innovation Studio at NC State University Libraries</a><br>
      Based on <a href="http://situationlab.org/project/the-thing-from-the-future/">TFTF by Situation Lab</a><br>
      2021 <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-BY-NC-SA</a>
    </p>
  </div>
</template>


<script>
import all_decks from '../data/all_decks.json';
import course_info from '../data/course_info.json';
export default {
  name: 'tftf',
  data() {
    return {
        arccards: [],
        objectcards: [],
        terraincards: [],
        current: {'arc': '', 'terrain': '', 'object': ''},
        course: "",
        course_name: "",
        form_link: "https://docs.google.com/presentation/d/1VoBZTmjG2UpjqwyJLg8GF4JeLEkhmag5Ru-uG4kXxes/copy",
        card_decks: [ 
          {deck: "Arc", desc: "ARC outlines the type of future world that the “thing” comes from, and how far away it is from today."}, // There are four types of Arc, each an umbrella for countless possible scenarios: growth, collapse, discipline, transformation.
          {deck: "Object" , desc: "OBJECT is the focus for your imagination: a specific cultural artifact that reveals something about how this future is different from today."},
          {deck: "Terrain", desc: "TERRAIN is the thematic context or location where this object could be found in that future."
      }] 
    }
  },
  created() {
    this.parse()
  },
  methods: {
    parse() {
      var vue = this;
      const queryString = window.location.search;
      const urlParams = new URLSearchParams(queryString);
      const urlDeck = urlParams.get('deck');
      var deck = urlDeck && Object.keys(all_decks).indexOf(urlDeck) > -1 ? urlDeck : 'all';
      console.log(deck)

      if (course_info[deck]['courses']){
        this.course = course_info[deck]['courses'];
      }
      if (course_info[deck]['course_name']) {
        this.course_name = course_info[deck]['course_name'];
      }
      if (course_info[deck]['form_link']){
        this.form_link = course_info[deck]['form_link'];
      }
      vue.cards = all_decks[deck];
        var objectcards = []
        var terraincards = []
        var arccards = []
        vue.cards.forEach(function(card) {
          if (card['Deck'] == 'Object') {
            objectcards.push(card['Title'])
          } else if (card['Deck'] == 'Terrain') {
            terraincards.push(card['Title'])
          } else if (card['Deck'] == 'Arc') {
             var arctext = 'In a "' + card['Title'] + '" future, ' + card['Description'];
             arctext += arctext.slice(-1)[0] != ',' ? ',' : '';
             arccards.push(arctext)
          }
        });

        vue.arccards = arccards;
        vue.objectcards = objectcards;
        vue.terraincards = terraincards;
        this.deal_cards();

    },
    deal_cards() {
      this.current['object'] = this.objectcards[Math.floor(Math.random() * this.objectcards.length)]
      this.current['terrain'] = this.terraincards[Math.floor(Math.random() * this.terraincards.length)]
      this.current['arc'] = this.arccards[Math.floor(Math.random() * this.arccards.length)]
    }
  }
}
</script>

<style scoped>

h4 {
    margin: 40px 0 0;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}

.box h3 {
  font-size: 1.5rem;
}

a {
 color: #004C9E;
}

.course-name {
  font-style: italic;
}

.course-name, .course-code {
  font-size: 1.5rem;
}

.btn-primary {
  background-color: #004C9E;
  border-color: #004C9E;
}
@media screen and (min-width: 601px){
  .wrapper {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));;
    background-color: #fff;
    color: rgb(202, 189, 189);
    max-width: 800px;
    max-height: 300px;
    margin: 0 auto; 
    padding: 25px; 
    column-gap: 15px;
    row-gap: 15px; 
  }
  .box {
    background-color: #fff;
    color: black;
    border-style: solid;
    border-color: black;
    border-radius: 23px;
    border-width: 10px;
    padding: 25px;
    font-size: 150%;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    text-align: center;
    }
  .wrapper .box:nth-child(1) {    background:#8ec741;           }
  .wrapper .box:nth-child(2) {    background:#00bef3;            }
  .wrapper .box:nth-child(3) {    background:#f36d7d;         }
}

@media screen and (max-width: 600px){
  .wrapper {
    display: grid;
    grid-template-rows: repeat(3, minmax(0, 1fr));
    background-color: #fff;
    color: rgb(202, 189, 189);
    max-width: 300px;
    max-height: 800px;
    margin: 0 auto; 
    padding: 25px; 
    column-gap: 15px;
    row-gap: 15px; 
  }
  .box {
    background-color: #fff;
    color: black;
    border-style: solid;
    border-color: black;
    border-radius: 23px;
    border-width: 10px;
    padding: 25px;
    font-size: 150%;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    text-align: center;
  }
  .wrapper .box:nth-child(1) {    background:#8ec741;           }
  .wrapper .box:nth-child(2) {    background:#00bef3;            }
  .wrapper .box:nth-child(3) {    background:#f36d7d;         }
}
</style>
