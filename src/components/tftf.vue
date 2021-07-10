<template>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <div>
    <h2>{{ msg }}</h2>
    <p>
      The Thing From the Future is an imagination game meant to spur creative and critical thinking.<br>
      To play the game, you draw a set of cards that prompt you to create an object from an alternative future.
    </p>
  </div>

  <div class="wrapper">

    <div class = "boxcontainer a">
      <div class="box a">
        <p> ARC </p>
        <h4>{{ arccards }}</h4>
      </div>
    </div>

    <div class = "boxcontainer b">
      <div class="box b">
        <p> OBJECT </p>
        <h4> there is a <br><em>{{ objectcards[0] }}</em></h4>
      </div>
      <br>
      <label class = "checkboxcontainer a"> Do Not Redeal
        <input type="checkbox" id = "objectCheckBox">
        <span class="checkmark"></span>
      </label>
    </div>

    <div class = "boxcontainer c">

      <div class="box c">
        <p> TERRAIN </p>
        <h4> related to <br><em>{{ terraincards[0] }}</em>.</h4>
      </div>
      <br>
      <label class = "checkboxcontainer b"> Do Not Redeal
        <input type="checkbox" id = "terrainCheckBox">
        <span class="checkmark"></span>
      </label>
    </div>

    
  </div>
  
  <div class="app">
    <br>
    <p><button v-on:click="deal_cards()" class="btn btn-primary">Deal Cards</button></p>
    <br>
    <h2><i> What is it? </i></h2>
    <p>
      Use <a href="https://docs.google.com/presentation/d/1VoBZTmjG2UpjqwyJLg8GF4JeLEkhmag5Ru-uG4kXxes/copy">this template</a> to respond to the prompt. 
      <br>
    </p>  
    <h3>  </h3>
    <h3> About the card decks: </h3>
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
var dealBeenClckd = false;
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
        this.papaparse.parse('https://raw.githubusercontent.com/NCSU-Libraries/the-thing-from-the-future/main/src/data/tftf_data_all.csv', {
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
      if (!dealBeenClckd){ //makes the checkmarks visible after the first time the deal button has been clicked
        dealBeenClckd = true;
        var checkBoxes = document.getElementsByClassName("checkboxcontainer");
        checkBoxes.forEach(element => element.style.display = "block");
      }
      //randomly selects another card if its respective checkbox is unchecked
      if(!document.getElementById("objectCheckBox").checked){
        this.objectcards[0] = this.objectcards[Math.floor(Math.random() * this.objectcards.length)]
      }
      if(!document.getElementById("terrainCheckBox").checked){
        this.terraincards[0] = this.terraincards[Math.floor(Math.random() * this.terraincards.length)]
      }
      
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

@media screen and (min-width: 630px){
  .wrapper {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));;
    background-color: #fff;
    color: rgb(202, 189, 189);
    max-width: 800px;
    max-height: 375px;
    margin: 0 auto; 
    padding: 25px; 
    column-gap: 15px;
    row-gap: 15px; 
  }
  
  .box {
    min-height: 250px;
    max-height: 250px;
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

  .checkboxcontainer{/*the container for the custom checkbox and its text*/
    display:none;
    position: relative;
    padding-left:35px;
    margin-bottom: 12 px;
    cursor: pointer;
    font-size: 22px;
    color:black;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }

  .checkboxcontainer input {/*hides the default checkbox so it can be replaced by the custom one*/
    position: absolute;
    opacity: 0;
    cursor: pointer;
    height: 0;
    width: 0;
  }

  .checkmark {/*the custom checkbox*/
    position: absolute;
    top: 0;
    left: 0;
    height: 25px;
    width: 25px;
    background-color: #eee;
    border-style: solid;
    border-color: black;
    border-width: 4px;
    border-radius: 6px;
  }

  .checkmark:after{/*hides the actual check of the checkmark by default*/
    content:"";
    position: absolute;
    display: none;
  }

  .checkboxcontainer input:checked ~ .checkmark:after{/*makes the actual check of the checkmark visible when the user clicks on the checkbox*/
    display:block;
  }

  .checkboxcontainer .checkmark:after{ /*the check*/
    left:4px;
    top: 0px;
    width: 9px;
    height:16px;
    border:solid white;
    border-width: 0 3px 3px 0;
    -webkit-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    transform: rotate(45deg);
  }

  .wrapper .boxcontainer:nth-child(1)  .box {    background:#8ec741;           }
  .wrapper .boxcontainer:nth-child(2) .box {    background:#00bef3;            }
  .wrapper .boxcontainer:nth-child(3) .box {    background:#f36d7d;         }
  /*sets the background of the checkboxes to the background color of its corresponding boxcontainer*/
  .wrapper .boxcontainer:nth-child(2)  .checkboxcontainer .checkmark {    background-color:#00bef3;           }
  .wrapper .boxcontainer:nth-child(3) .checkboxcontainer .checkmark {    background-color:#f36d7d;            }       

}

@media screen and (max-width: 629px){
  .wrapper {
    display: grid;
    grid-template-rows: repeat(3, minmax(0, 1fr));
    background-color: #fff;
    color: rgb(202, 189, 189);
    max-width: 300px;
    max-height: 975px;
    margin: 0 auto; 
    padding: 25px; 
    column-gap: 15px;
    row-gap: 15px; 
  }

  .box {
    background-color: #fff;
    color: black;
    min-height: 250px;
    max-height: 250px;
    border-style: solid;
    border-color: black;
    border-radius: 23px;
    border-width: 10px;
    padding: 25px;
    font-size: 150%;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    text-align: center;
  }

  .checkboxcontainer{/*the container for the custom checkbox and its text*/
    display:none;
    position: relative;
    padding-left:35px;
    margin-bottom: 15 px;
    cursor: pointer;
    font-size: 22px;
    color:black;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }

  .checkboxcontainer input {/*hides the default checkbox so it can be replaced by the custom one*/
    position: absolute;
    opacity: 0;
    cursor: pointer;
    height: 0;
    width: 0;
  }

  .checkmark {/*the custom checkbox*/
    position: absolute;
    top: 0;
    left: 0;
    height: 25px;
    width: 25px;
    background-color: #eee;
    border-style: solid;
    border-color: black;
    border-width: 4px;
    border-radius: 6px;
  }

  .checkmark:after{/*hides the actual check of the checkmark by default*/
    content:"";
    position: absolute;
    display: none;
  }

  .checkboxcontainer input:checked ~ .checkmark:after{/*makes the actual check of the checkmark visible when the user clicks on the checkbox*/
    display:block;
  }

  .checkboxcontainer .checkmark:after{/*the check*/
    left:4px;
    top: 0px;
    width: 9px;
    height:16px;
    border:solid white;
    border-width: 0 3px 3px 0;
    -webkit-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    transform: rotate(45deg);
  }

  .wrapper .boxcontainer:nth-child(1)  .box {    background:#8ec741;           }
  .wrapper .boxcontainer:nth-child(2) .box {    background:#00bef3;            }
  .wrapper .boxcontainer:nth-child(3) .box {    background:#f36d7d;         }
  /*sets the background of the checkboxes to the background color of its corresponding boxcontainer*/
  .wrapper .boxcontainer:nth-child(2)  .checkboxcontainer .checkmark {    background-color:#00bef3;           }
  .wrapper .boxcontainer:nth-child(3) .checkboxcontainer .checkmark {    background-color:#f36d7d;            } 
}
</style>