from art import logo

def add(n1, n2):
    """Take two inputs and return the sum of them"""
    return n1 + n2

def subtract(n1, n2):
    """Take two inputs and return their difference"""
    return n1 - n2

def multiply(n1, n2):
    """Take two inputs and return their product"""
    return n1 * n2

def division(n1, n2):
    """Take two inputs and divide them"""
    return n1 / n2

def power(n1, n2):
    """Take the first input and elevate it to the power of the second input"""
    return n1 ** n2

def calculate(n1, op, n2):
    """Calculate based on the inputs of the user"""
    return operations[op](n1, n2)

def calculator():
    print(logo)  # Logo
    continue_answer = True
    num1 = float(input("Type the first number:\n"))
    while continue_answer:
        # Ask for inputs
        operator = input("+\n-\n*\n/\n**\nType the operator:\n")
        num2 = float(input("Type the second number\n"))
        # Show outputs
        result = calculate(num1, operator, num2)
        print(f"{num1} {operator} {num2} = {result}")
        answer = input(f"Type 'y' to continue calculating with {result} or type 'n' to restart\n").lower()
        if answer == "y":
            num1 = result
        else:
            continue_answer = False
            print("\n" * 100)
            calculator()

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
    "**": power,
}

calculator()
