from art import logo

# Function to find the highest bidder
def find_highest(bids_dict):
    highest_bid = 0
    winner = ''
    for bidder in bids_dict:
        bid_amount = bids_dict[bidder]
        if  bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print(logo) # Print the program logo
print("Welcome to the blind auction program!".upper()) # Welcome
add_new = True # Variable to control the while loop
bids = {} # Empty dict to add the bidder's names and bids

# While loop to add new bidders until user type "no"
while add_new:
    name = input("What's your name?\n") # Ask bidder name
    bid = float(input("How much is your bid?\n$")) # Ask bid
    bids[name] = bid # Add to the dict
    answer = input("Is there more bidders? Type yes or no\n").lower()
    if answer == "no": # Check if there is more bidders
        add_new = False
    print("\n" * 100)  # "Clear" the console

find_highest(bids) # Comparing bids values to get the biggest
