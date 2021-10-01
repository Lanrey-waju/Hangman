# Step 2

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# hanging_man = stages.reverse()
end_of_game = False
wrong_guesses = 0
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
letters_list = list(chosen_word)

# create a "lives" variable
lives = len(stages)

# Testing code
print(f"Pssst, the solution is {chosen_word}.")


# TODO-1: - Create an empty List called display.
display = []
# For each letter in the chosen_word, add a "_" to 'display'.
blanks = "_" * len(chosen_word)
for space in blanks:
    display.append(space)

print(display)
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

while wrong_guesses < lives - 1:
    print("\n")
    guess = input("Guess a letter: ").lower()
    if guess in letters_list:
        letter_index = letters_list.index(guess)
        display[letter_index] = guess
        letters_list[letter_index] = "$"

#TODO-2: - If guess is not a letter in the chosen_word,
# Increase wrong guesses by 1. Print the ASCII art from 'stages' that corresponds to the current number of wrong guesses the user has made. 
    else:
      print("\n".join(stages[-1:wrong_guesses + 1]))
      wrong_guesses += 1
  #If lives goes down to 0 then the game should stop and it should print "You lose."
    if wrong_guesses == lives:
      print("You lose")
      break

  #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        print("Word completed. Well done!")
        end_of_game = True
        print("You win.")
        break
