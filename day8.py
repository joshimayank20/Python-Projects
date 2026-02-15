import string

alphabet = list(string.ascii_lowercase)

def caesar(text, shift, direction):
    result = ""
    
    if direction == "decode":
        shift *= -1
    
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            result += alphabet[new_position]
        else:
            result += letter  # keeps spaces/symbols unchanged
    
    print(f"The {direction}d text is: {result}")


print("Welcome to Caesar Cipher!")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift % 26  # handles large numbers
    
    caesar(text, shift, direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        print("Goodbye!")
        break

