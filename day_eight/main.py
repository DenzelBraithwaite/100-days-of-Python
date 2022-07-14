import os
import math
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encrypting = True

def caesar(text, shift, directon):
  text_split = list(text)
  final_text = ""
  if direction == "decode".lower():
    shift = -shift
  for character in text_split:
    if character in alphabet:
      index = alphabet.index(character)
      new_index = index + shift
      if new_index < 0:
        shift = shift % -26
      elif new_index > 26:
        shift = shift % 26

      new_index = index + shift
      new_letter = alphabet[new_index]
      final_text += new_letter
    elif not character in alphabet:
      final_text += character

  print(f"The final text is {final_text}")

while encrypting:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n> ")
  text = input("Type your message:\n> ").lower()
  shift = int(input("Type the shift number:\n> "))

  caesar(text, shift, direction)
  print("\nWould you like to play again?")
  choice = input("Type yes or no\n> ").lower()

  if choice == 'yes':
    os.system('clear')
  else:
    encrypting = False
    print("Ok no problem, see you next time hacker!")
