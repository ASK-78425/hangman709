# %%
# create list with 5 favourite fruits
word_list = ["Apples", "Grapes", "Bananas", "Strawberries", "Cherries"]

# %%
# choose random word from the list
import random
word = random.choice(word_list)

# %%
# assign user input for game
if __name__ == "__main__":
  guess = input("Please enter a letter: ")

# %%
# validate user input
if __name__ == "__main__":
  if len(guess) == 1 and guess.isalpha() == True:
      print("Good guess!")
  else:
      print("Oops! That is not a valid input.")
