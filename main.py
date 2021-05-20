from art import logo
import os

print(logo)

def bid_calc():
    bid_names = {}
    max_bidder = []
    bid_names[name] = bid

    for bidder in bid_names:
      score = 0
      if bid_names[bidder] > score:
        score = bid_names[bidder]
        max_bidder.append(bidder)
        max_bidder.append(score)
    print(f"The max bidder is: {max_bidder[0]} with a bid of {max_bidder[1]}")


repeat = False
while repeat != True:
  bid = int(input("What is your bid?: "))
  name = input("What is your name?: ")

  game_over = input(
      "Are there more bidders? Enter in 'Y' to bid or 'n' to end the game: \n").lower()
  if game_over == "y":
      os.system('clear')
  elif game_over == "n":
    os.system('clear')
    bid_calc()
    repeat = True
