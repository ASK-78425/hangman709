
# %%
import random

class Hangman:
   def __init__(self, word_list, numlives = 5):
      self.word_list = word_list
      self.numlives = numlives
      self.word = random.choice(self.word_list) # select word
      self.list_of_guesses = [] # empty list for letter guesses
      self.word_guessed = []
      for letter in self.word:
         self.word_guessed.append("_") # appends _ for each letter in word
      self.letters_list = []
      self.unique_vals = []
      for letter in self.word.lower():
         self.letters_list.append(letter) # splits word into list of its letters
      for letter in list(set(self.letters_list)):
        if letter not in self.list_of_guesses:
         self.unique_vals.append(letter) # checks unique values against guesses
      self.num_letters = len(self.unique_vals) # gives number of letters left to guess

   def check_guess(self, guess):
      guess = guess.lower()
      if guess in self.word.lower(): # checks word for guessed letter
            print(f"Good guess! {guess} is in the word.")
            for letter in self.letters_list:
               if letter == guess:
                  self.index = self.letters_list.index(guess)
                  self.word_guessed[self.index] = guess
                  self.letters_list[self.index] = 0
            self.num_letters -= 1
      else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.numlives -= 1
            print(f"You have {self.numlives} lives left.")

         
   def ask_for_input(self):
       while True:
          guess = input("Guess a letter: ")
          if not guess.isalpha() and len(guess) != 1:
             print("Invalid letter. Please, enter a single alphabetical character.")
          elif guess in self.list_of_guesses:
             print("You already tried that letter!")
          else:
             self.check_guess(guess)
             self.list_of_guesses.append(guess)
             break



# %%
def play_game(word_list):
   numlives = 5
   game = Hangman(word_list, numlives)
   while True:
      if game.numlives == 0:
         print("You lost!")
         break
      elif game.num_letters > 0:
         game.ask_for_input()
         print(game.word_guessed)
      else:
         print("Congratulations! You won the game!")
         break
