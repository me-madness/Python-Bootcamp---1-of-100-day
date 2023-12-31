# Auction Program Project

from replit import clear
#Hints use function clear() to clear the inputs


from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    #highest_bid = max(bidding_record.values()) if bidding_record else None
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")        
        
        
        
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are the any other bidder? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()    