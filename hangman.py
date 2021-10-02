import random
from hangman_words import word_list

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


end_of_game = False
wrong_guesses = 0
chosen_word = random.choice(word_list)
letters_list = list(chosen_word)
word_length = len(letters_list)

# create a "lives" variable. This variable will be used to print the status of the hanging man.
lives = len(stages) - 1


# TODO-1: - Create an empty List called display.
display = []
# For each letter in the chosen_word, add a "_" to 'display'.
for _ in range(word_length):
  display += "_"

print(display)
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


while not end_of_game:
    print("\n")
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
      letter = chosen_word[position]
      if letter in guess:
          display[position] = guess
        # letters_list[letter_index] = "$"

#TODO-2: - If guess is not a letter in the chosen_word,
# Increase wrong guesses by 1. Print the ASCII art from 'stages' that corresponds to the current number of wrong guesses the user has made. 
    if guess not in chosen_word:
      lives -= 1
  #If lives goes down to 0 then the game should stop and it should print "You lose."
      if lives == 0:
        end_of_game = True
        print("You lose")
        

  #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        print("Word completed. Well done!")
        end_of_game = True
        print("You win.")

    print(stages[lives])