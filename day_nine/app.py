import os
from art import logo

bids = {}
num_of_bidders = 1


def take_bid(bidders):
    name = input("Hello next bidder, what is your awesome bidding alias?\n >")
    # Bid can only be a full int, not a float
    bid = int(input("\nGreat, and how much money will you be bidding?\n > $"))
    bidders[name] = bid
    # Currently, if the same user enters a higher bid, it will treat them like a new person.
    print(
        f"\nAwesome, {len(bidders)} bidders so far! Before we close the bid, will there be anyone else bidding today?"
    )


print(logo)
print("Welcome to the world's most ghetto auction program.\n")
name = input("\nWhat is your awesome bidding alias?\n >")
bid = int(
    input(
        "\nGreat, since you're here I assume you have money. How much of that loot will you be bidding today?\n > $"
    ))
bids[name] = bid
print(
    "\nIt wouldn't be much of an auction if you bid alone... is there anyone else who'd like to spend some cash?"
)
other_bidders = input("\nType Yes or No.\n >").lower()

while other_bidders == "yes":
    os.system("clear")
    print(logo)
    take_bid(bids)
    other_bidders = input("Type Yes or No.\n >").lower()

winner = (max(bids, key=bids.get))
winning_bid = bids[winner]
print(
    f"Winner winner chicken dinner! The winner of this auction is {winner}! With an astounding bid of ${winning_bid}!"
)
