import os
import random
from hangman_words import word_list
from hangman_art import stages, logo

# List of words that will be sampled for Hangman game
game_over = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
guessed_letters = []
lives = 6
current_hangman = stages[lives]

# Chooses a random word from the #word_list and creates an array duplicate
chosen_word = random.choice(word_list)
chosen_word_as_array = []

for letter in chosen_word:
  chosen_word_as_array += letter

for blank in range(len(chosen_word)):
  display.append('_')

def already_guessed(guess):
    if not guess in guessed_letters:
      guessed_letters.append(guess)

def still_playing():
  if lives > 0 and display != chosen_word_as_array:
    return True
  else:
    return False

while still_playing():
  os.system('clear')
  print(logo)
  print(f"Lives remaining: {lives}")
  print(current_hangman)
  print(display)
  print('\n')
  print(f"You've guessed --> {guessed_letters}\n")
  guess = input("Guess a letter: \n> ").lower()
  already_guessed(guess)
  if not guess in chosen_word_as_array:
    lives -= 1
    current_hangman = stages[lives]
  for index in range(len(display)):
    if chosen_word[index] == guess:
      display[index] = guess

os.system('clear')
print(logo)
print(current_hangman)
print(display)
print('\n')
if display == chosen_word_as_array:
  print(f'Congrats! You win, the word was {chosen_word}')
else:
  print(f"Oh no, I'm sorry but you lose. The word was '{chosen_word}'")
