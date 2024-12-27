from art import logo

# Program that encode and decode messages by shifting 
# the letters in the message along the alphabet

# List of alphabet letters 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to encode or decode 
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

print(logo) # Program logo
should_continue = True # Variable to control the while loop

# Loop to continuing asking if the user wanna continue 
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction) # Call function to encode and decode
    answer = input("Do you want to start the program again? Type yes or no\n").lower() # Ask if user want to continue
    if answer == "no":
        should_continue = False # Break the loop if user don't wanna continue
        print("Goodbye!!")
