# %%
# create list with 5 fav fruits
word_list = ["Apples", "Grapes", "Bananas", "Strawberries", "Cherries"]
print(word_list)

# %%
# choose random word from the list
import random
word = random.choice(word_list)
print(word)
# %%
# assign user input for game
guess = input("Please enter a letter: ")
print(guess)
# %%
# validate user input
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
     print("Oops! That is not a valid input.")