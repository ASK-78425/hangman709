# %%
# Import word variable
from milestone_2 import word
print(word)

# %%
# Check whether guess is in the word

# %%
# Combine into functions
def check_guess(guess):
    guess = guess.lower()
    if guess in word.lower():
      print(f"Good guess! {guess} is in the word.")
    else:
      print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
# Set up loop to continually request input until conditions met
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            break
        print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

# %%
# Test the ask_for_input function:
ask_for_input()
