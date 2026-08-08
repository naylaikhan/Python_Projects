from auction_art import logo

def find_highest_bidder(building_dictionary):
    winner=""
    highest_bid =0
    for bidder in building_dictionary:
        bid_amount=building_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder


    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids={}

continue_bidding = True

while continue_bidding:
    name=input("What is you name : ")
    price=int(input("What is your bid? : $ "))
    bids[name] = price
    should_continue=input("Are there any other bidders ? Type 'Yes' or 'no'. \n ")

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)



