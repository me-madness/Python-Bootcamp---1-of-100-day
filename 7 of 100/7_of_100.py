# For & While loop, if / else, Lists, Strings, Range, Modules



# How to break a Complex problem down into a Flow chart


## Challenge 1 - Picking a Random word and checking answers 

# Step 1 and Solution
word_list = ["ardvark", "baboon", "camel"]

# Todo-1 - """Randomly choose a word from the word_list and assign it to a variable called chosen_word."""
import random

chosen_word = random.choice(word_list)

# Todo-2 - """Ask the use to guess a letter and assign their answer to a variable called guess. Make guess lowercase"""
guess = input("Guess a letter: ").lower()

# Todo-3 - """Check if the letter the user guessed (guess) is one of the letter in the chosen_word"""
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


## Challenge 2 - Replacing Blanks with Guesses

import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# Testing code
print(f"Pssst, the solution is {chosen_word}.")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)    

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_word(position)
    if letter == guess:
        display[position] = letter

print(display)


## Challenge 3 - Checking if the Player has Won


import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# Testing code
print(f"Pssst, the solution is {chosen_word}.")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display) 

end_of_game = False   
while not end_of_game: 
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word(position)
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You win.")


## Challenge 4 - Keeping Track of the Player_s Lives

import random

stages = ['''
          
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  0   |
  |    |
      |
      |
=========
''', '''
  +---+
  |   |
  0   |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# Testing code
print(f"Pssst, the solution is {chosen_word}.")

display = []
word_length = len(chosen_word)

lives = 6

for _ in range(word_length):
    display += "_"
print(display) 

end_of_game = False   
while not end_of_game: 
    guess = input("Guess a letter: ").lower()

    # Check guesses position
    for position in range(word_length):
        letter = chosen_word(position)
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            
    # Check the lives        
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    print(stages[lives])    
    
    
## Challenge 5 -




## Hangman Project
# 7_of_100_project_hangman.py