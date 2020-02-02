#This is project is done for the fun#
###You have two files a input named inputPS2.txt and promptsPS2.txt.
###Your task is to get appropriate outputPS2.txt such that it contains the correct answers asked in promptsPS2.txt file using inputPS2.txt file.

## About the inputPS2.txt file ##
###This is the input file we gathering data from this file. It contains the movie name with their actors acted, they are separated by the '/' character.


## About the promptPS2.txt file ##
###This is also input file, It includes operations to find out using inputPS2.txt and stores that operations answer into outputPS2.txt file.
###What kind of operations it has?

### searchActor: actor name => It gives the name of movies in which actor acted.

### searchMovie: movie name => It displays the actors of that movie.

#### RMovies: movie1 : movie2 => It displays the relationship(common actors in both movie) between movie1 and movie2, if relationship found it display "Yes, actor name" else "No relation found between above movies"

### TMovies: movie1 : movie2 => It finds out is there any transitivity relation between movie1 and movie2 with respect to the actors acted in both movie. The answer to be display with proper manner showing how transitivity happens.###
#### Example-
#### Tmovie: Dangal : ADHM
#### Related: Yes, Dangal > Aamir Khan > PK > Anushka Sharma > ADHM


## About the outputPS2.txt file ##
### This file is an output file. All result get stored into this file after execution src.py file.

### Dependencies:
### python3

### How to run? 
#### Clone or Pull repository on your machine then just do python3 src.py
