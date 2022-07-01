# final_amount = (total / amount_of_people) * tip_percentage
total = 140
tip = 1.12

print("Hi there, here is your bill. Your total is $140\n")
print(f"With tax, that comes up to ${total * tip}\n")

print("Will that be 1 bill or..?\n")
amount_of_people = int(input("You say: No actually, please split it in "))
final_amount = round((total / amount_of_people) * tip, 2)

print("No problem at all, here is your total.")
print(f"Each of you will have to pay {final_amount}")