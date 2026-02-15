import random

def game():
    number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        guess = int(input("Make a guess: "))
        
        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        else:
            print("You got it!")
            return
        
        attempts -= 1
        print(f"Attempts left: {attempts}")
    
    print("You ran out of attempts. The number was:", number)

game()
