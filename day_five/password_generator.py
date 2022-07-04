import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the world's not best nor worst password generator!!!")
amount_of_letters= int(input("How many letters would you like in your brand new secure password?\n> ")) 
amount_of_symbols = int(input(f"Got it, and how many symbols?\n> "))
amount_of_numbers = int(input(f"Lastly, how many numbers would you like?\n> "))

password = []
secure_password = ''

# Could've also used append for these.
for letter in range(0, amount_of_letters):
  password += random.choice(letters)

for symbol in range(0, amount_of_symbols):
  password += random.choice(symbols)

for number in range(0, amount_of_numbers):
  password += random.choice(numbers)

random.shuffle(password)

for char in password:
  secure_password += char

print(f"Congrats, here is your shiny new password ;)")
print(f"---> {secure_password} <---")
