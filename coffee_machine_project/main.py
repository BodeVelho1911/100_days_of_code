import menu
import art

# Functions
def make_espresso():
    """Function to subtract the amount needed to make an espresso from the resources dict"""
    menu.resources['water'] -= 50
    menu.resources['coffee'] -= 18
    print("Here's your espresso. Enjoy!! ☕")

def make_latte():
    """Function to subtract the amount needed to make a latte from the resources dict"""
    menu.resources['water'] -= 200
    menu.resources['coffee'] -= 24
    menu.resources['milk'] -= 150
    print("Here's your latte. Enjoy!! ☕")

def make_cappuccino():
    """Function to subtract the amount needed to make a cappuccino from the resources dict"""
    menu.resources['water'] -= 250
    menu.resources['coffee'] -= 24
    menu.resources['milk'] -= 100
    print("Here's your cappuccino. Enjoy!! ☕")

def needed_amount(beverage, ingredient):
    """Takes the wanted beverage and the ingredient and returns the amount of ingredient needed to make the beverage"""
    amount_needed = menu.menu[beverage]["ingredients"][ingredient]
    return amount_needed

def price(beverage):
    """Takes the beverage (As a string) and returns its price"""
    beverage_price = menu.menu[beverage]["cost"]
    return beverage_price

def calculate_change(pennies, nickels, dimes, quarters):
    """Takes the amount of money the user has put in and calculate if its needed change and returns it.
    If the payment is not enough, returns -1"""
    total_paid = pennies * 0.01 + nickels * 0.05 + dimes * 0.10 + quarters * 0.25
    if total_paid >= price(answer):
        return total_paid - price(answer)
    else:
        return -1

def take_payment_and_make(beverage):
    """Take the beverage the user wants, asks the payment and make the beverage"""
    print(f"Please insert ${price(answer):.2f} in the coin port")

    # Ask how many of which coin
    penny_amount = int(input("How many pennies did you put in? "))
    nickel_amount = int(input("How many nickels did you put in? "))
    dime_amount = int(input("How many dimes did you put in? "))
    quarter_amount = int(input("How many quarters did you put? "))

    # Check if user has made an enough amount of payment
    change_amount = calculate_change(penny_amount, nickel_amount, dime_amount, quarter_amount)
    if change_amount == -1:
        print("That's not enough money. Refunded!")
    else:
        if beverage == "espresso":
            make_espresso()
        elif beverage == "latte":
            make_latte()
        elif beverage == "cappuccino":
            make_cappuccino()
        if change_amount > 0:
            print(f"Your change is ${change_amount:.2f}")

# Is the machine turned on?
state = True

# Display the initial screen
print(art.logo)
print(art.cup)
profit = 0
# Loop to keep machine on
while state:
    # Ask the user which beverage it wants (espresso, latte or capuccino)
    answer = input("What would you want? Type 'help' to see commands: ")

    # Resources left in the machine
    water_left = menu.resources["water"]
    coffee_left = menu.resources["coffee"]
    milk_left = menu.resources["milk"]

    # Check the answer to decide what to do and
    # check if there are enough resources in the machine to make the user's coffee
    ## Checking for espresso ingredients
    if answer == 'espresso':
        water_needed_espresso = needed_amount("espresso", "water")
        coffee_needed_espresso = needed_amount("espresso", "coffee")
        if water_left >= water_needed_espresso and coffee_left >= coffee_needed_espresso:
            take_payment_and_make("espresso")
            profit += price("espresso")
        elif water_left < water_needed_espresso:
            print("Sorry, not enough water. Please refill the machine.")
        elif coffee_left < coffee_needed_espresso:
            print("Sorry, not enough coffee. Please refill the machine.")
        else:
            print("Sorry, not enough water and coffee. Please refill the machine.")

    ## Checking for latte ingredients
    if answer == 'latte':
        water_needed_latte = needed_amount("latte", "water")
        coffee_needed_latte = needed_amount("latte", "coffee")
        milk_needed_latte = needed_amount("latte", "milk")
        if water_left >= water_needed_latte and coffee_left >= coffee_needed_latte and milk_left >= milk_needed_latte:
            take_payment_and_make("latte")
            profit += price("latte")
        elif water_left < water_needed_latte:
            print("Sorry, not enough water. Please refill the machine.")
        elif coffee_left < coffee_needed_latte:
            print("Sorry, not enough coffee. Please refill the machine.")
        elif milk_left < milk_needed_latte:
            print("Sorry, not enough milk. Please refill the machine.")
        else:
            print("Sorry, not enough water, milk and coffee. Please refill the machine.")

    ## Checking for cappuccino ingredients
    if answer == 'cappuccino':
        water_needed_cappuccino = needed_amount("cappuccino", "water")
        coffee_needed_cappuccino = needed_amount("cappuccino", "coffee")
        milk_needed_cappuccino = needed_amount("cappuccino", "milk")
        if water_left >= water_needed_cappuccino and coffee_left >= coffee_needed_cappuccino and milk_left >= milk_needed_cappuccino:
            take_payment_and_make("cappuccino")
            profit += price("cappuccino")
        elif water_left < water_needed_cappuccino:
            print("Sorry, not enough water. Please refill the machine.")
        elif coffee_left < coffee_needed_cappuccino:
            print("Sorry, not enough coffee. Please refill the machine.")
        elif milk_left < milk_needed_cappuccino:
            print("Sorry, not enough milk. Please refill the machine.")
        else:
            print("Sorry, not enough water, milk and coffee. Please refill the machine.")

    # Refill the machine
    if answer == "refill":
        menu.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0,
        }
        print("Machine refilled!!")

    # Turn the coffee machine off when the user type 'off'
    if answer == 'off':
        state = False
        print("Machine turned off. Good bye!")
    # Print a list of the ingredients remaining in the machine when user types 'report'
    if answer == 'report':
        print(f"Water: {water_left} ml\nMilk: {milk_left} ml\nCoffee: {coffee_left} g\nMoney: ${profit}")

    if answer == "help":
        print("""off -> Turn off the coffee machine\nreport -> See remaining ingredients\nrefill -> Refill the ingredients\nespresso -> Make an espresso\nlatte -> Make a latte\ncappuccino -> Make a cappuccino""")
