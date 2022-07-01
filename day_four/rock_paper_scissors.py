import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
player_choice = input("Rock, Paper or Scissors?\n> ").lower()

if player_choice == computer_choice:
  if player_choice == "rock":
    print(f"{rock}\nIt's a draw! You both chose rock!")
  elif player_choice == "paper":
    print(f"{paper}\nIt's a draw! You both chose paper!")
  else:
    print(f"{scissors}\nIt's a draw! You both chose scissors!")
elif player_choice == "rock":
  if computer_choice == "scissors":
    print(f"{rock}VS{scissors}\nRock beats scissors, you win!!!")
  else:
    print(f"{rock}VS{paper}\nPaper beats rock, you lose...")
elif player_choice == "scissors":
  if computer_choice == "paper":
    print(f"{scissors}VS{paper}\nScissors beats paper, you win!!!")
  else:
    print(f"{scissors}VS{rock}\nRock beats scissors, you lose...")
elif player_choice == "paper":
  if computer_choice == "rock":
    print(f"{paper}VS{rock}\nPaper beats rock, you win!!!")
  else:
    print(f"{paper}VS{scissors}\nScissors beats paper, you lose...")
else:
  print("Sorry, your choice was invalid. Maybe you've never played rock paper scissors before? Please try again.")
