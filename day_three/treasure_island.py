print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
name = input("Please enter your name\n> ")
print("Welcome to Death Island.")
print("Many seek to leave here with their pockets filled with gold. Few leave here at all.")

choice_one = input(f"The path ahead splits into two, which way do you go?\n - Left\n - Right\n{name}> ").lower()
if choice_one == "left":
  choice_two = input(f"You arrive at a door, what do you do?\n - Knock\n - Open\n{name}> ").lower()
  if choice_two == "open":
    choice_three = input(f"You reach the treasure room and see three chests, which do you open?\n - Left\n - Middle\n - Right\n{name}> ").lower()
    if choice_three == "left":
      print("The left chest opens and you see a glow of gold! Congrats, you're rich!!!")
    elif choice_three == "middle":
      print("You open the middle chest and hear a 'click'. The room quickly fills with sands and the walls close in. Game over.")
    elif choice_three == "right":
      print("You open the right chest, only to discover it was the wrong chest. You spontaneously combust into flames... Game over")
    else:
      print("The decision is too much to bear, you sit there pondering which chest to open until you finally die before making a decision. Game Over :(")
  else:
    print("The knocking disturbs nearby creatures, they swarm you within moments. Game Over :(")
else:
  print("You get lost for hours and never make it home. Game Over :(")