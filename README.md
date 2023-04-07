# 'The Thing From the Future' vue.js web app

The Thing From the Future is an imagination game meant to spur creative and critical thinking. To play the game, you draw a set of cards that prompt you to create an object from an alternative future.

Based on [the original card game by Situation Lab](https://situationlab.org/project/the-thing-from-the-future/). 

## Visit https://ncsu-libraries.github.io/the-thing-from-the-future/ to play.

## Learn more about the development of the project [at this link](https://drive.google.com/file/d/1q4VBmOqpjpJMK5g2cAwZ-8lK5gFqxUno/view?usp=sharing). 

This version was used in the 2020 first-year and transfer student seminar ["Wicked Problems, Wolfpack Solutions"](https://wolfpacksolutions.ncsu.edu/) at NCSU. Additional versions of the game for other courses can be found below: 
* [Women's, Gender, and Sexuality Studies (WG 350)](https://ncsu-libraries.github.io/tftf-wgs350/)
* [Advanced Graphic Design Stuido (GD 400)](https://ncsu-libraries.github.io/tftf-gd400/)
* [Filming in a Time of Emergency: Socio-Environmental Crisis and Alternative Futures Through Film (ENG 492)](https://ncsu-libraries.github.io/tftf-ENG-492/)

## Adding a new deck

1. Create CSV that has decks in a format similar to this: https://github.com/NCSU-Libraries/the-thing-from-the-future/blob/main/src/data/all.csv
2. **The name of the csv is going to become the URL slug, make sure there are no spaces/special characters other than `-`** 
3. Upload CSV to the [data](https://github.com/NCSU-Libraries/the-thing-from-the-future/tree/main/src/data) folder (you should be able to drag and drop). 
4. Wait a minute (this allows scripts to auto run and populate data). You should see a commit on the [home page](https://github.com/NCSU-Libraries/the-thing-from-the-future) when this is done saying "update data folder".
5. Find the name of your csv in the [course_info file](https://github.com/NCSU-Libraries/the-thing-from-the-future/blob/main/src/data/course_info.json). Update with the correct form_link, course name and course. Save.
6. Your new site should be avaliable at https://ncsu-libraries.github.io/the-thing-from-the-future/?deck=name-of-your-deck in a minute.
