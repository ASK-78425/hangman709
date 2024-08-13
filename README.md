# Hangman
This project will implement the classic game of Hangman in Python. The overall aim is to create a simple, efficient, and user-friendly version of the game.

Under the hood, the project relies on fairly simple functions, an overall game class, and of course some user input to play the game. In terms of installations/imports, we are using Python's built-in 'random' module (_see https://python.readthedocs.io/en/stable/library/random.html_) to set the word that must be guessed by the player.

The game class will take two main methods: 'check_guess' and 'ask_for_input', combining an updating process for the attributes set during the initalisation of the class and an interactive process (obviously required in order to play the game!).

In terms of usage, the milestone_5.py file contains all that is needed to run the game. A class instance has been created within the 'play_game' function, so you can simply call the function and pass a list of words as an argument, and a random word from this list will be selected to use for the game.

Lessons learned for me in this project include problems that can arise with the index function. It will find only the first instance of an element in a list, so when words are split into lists of letters and they have _repeated_ elements, it can cause problems:

Take the word 'Hippo'. If we loop over the letters in the word to find the index of 'p', the index function will only ever locate the index of the _first_ 'p'. As a solution, I iterated over the list of letters following a correct guess and replaced each corresponding letter with a number, to ensure that the same index would not be found (numeric values entered by a user will simply throw an error asking you to input a valid, alphabetic character). Thus, on the first loop, the list would become ['h', 'i', '0', 'p', 'o'], returning the index of 2 for the first instance of 'p'. Then, on the next loop, the index would be 3 as it would ignore the newly-assigned 0, giving a result of ['h', 'i', '0', '0', 'o']. These index values of 2 and 3 then allowed me to slot in two 'p' characters into a list showing correctly guessed characters in a word thus far: [_, _, p, p, _].
