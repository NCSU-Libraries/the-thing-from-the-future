<template>
  <div>
    <h1><i>{{ msg }}</i></h1>
    <p>
      The Thing From the Future is an imagination game meant to spur creative and critical thinking.<br>
      To play the game, you draw a set of cards that prompt you to create an object from an alternative future.
    </p>
  </div>

  <div class="wrapper">
    <div class="box a">
      <h1> ARC </h1>
      <br>
      <h2>{{ arccards }}</h2>
    </div>
    <div class="box b">
      <h1> OBJECT </h1>
      <br>
      <h2> there is a <br><b>{{ objectcards[0] }}</b></h2>
    </div>
    <div class="box c">
      <h1> TERRAIN </h1>
      <br>
      <h2> related to <br><b>{{ terraincards[0] }}</b>.</h2>
    </div>
    

    
  </div>
  
  <div class="app">
    <h3><i> What is it? </i></h3>
    <br>
    <p><button v-on:click="deal_cards()" class="btn btn-primary">Deal Cards</button></p>
    <br>
    <p> About the Card Decks: </p>
      <ul class="list-group">
        <li v-for="(deck, index) in card_decks" :key="index">{{deck.desc}}</li>
      </ul>
      <br>
  </div>

  <div>
    <p>
      Made by <a href="https://www.lib.ncsu.edu/spaces/innovation-studio">the Innovation Studio at NCSU Libraries</a><br>
      Based on <a href="http://situationlab.org/project/the-thing-from-the-future/">TFTF by Situation Lab</a><br>
      2021 <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-BY-NC-SA</a>
    </p>
  </div>
</template>

<script>
export default {
  name: 'tftf',
  props: {
    msg: String
  },
  inject:['papaparse'],
  data() {
    return {
        arccards: [],
        objectcards: [],
        terraincards: [],
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
        this.papaparse.parse('https://raw.githubusercontent.com/cullerth/tftf-webapp/main/src/data/tftf_data_all.csv', {
        header: true,
        download: true, 
        complete: function(results) {
          console.log('parsing done', results)
          vue.cards = results['data']

          var arccards = vue.cards[0]['Description']
          var objectcards = []
          var terraincards = []
          // var arccards = []
          vue.cards.forEach(function(card) {
            if (card['Deck'] == 'Object') {
              objectcards.push(card['Title'])
            } else if (card['Deck'] == 'Terrain') {
              terraincards.push(card['Title'])
            } //else if (card['Deck'] == 'Arc') {
            //   arccards.push('In a "' + card['Title'] + '" future,' + card['Description'] + ", ")
            // } 
          });

          vue.arccards = arccards;
          vue.objectcards = objectcards;
          vue.terraincards = terraincards;

        }
      });
    },
    deal_cards() {
      this.objectcards[0] = this.objectcards[Math.floor(Math.random() * this.objectcards.length)]
      this.terraincards[0] = this.terraincards[Math.floor(Math.random() * this.terraincards.length)]
    }
  }
}
</script>

<style scoped>
h3 {
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
a {
  color: #42b983;
}
.wrapper {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  background-color: #fff;
  color: rgb(202, 189, 189);
  max-width: 825px;
  margin: 0 auto; 
  padding: 25px; 
  column-gap: 15px; 
}
.box {
  background-color: #fff;
  color: #444;
  border-color: rgb(10, 10, 10);
  border-radius: 25px;
  border-width: 10px;
  padding: 25px;
  font-size: 150%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-align: center;
  /* outline: solid; 
  outline-color: black; */
}
</style>
