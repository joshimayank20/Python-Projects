import random

word_list = ["apple", "banana", "tiger", "mountain", "python"]
chosen_word = random.choice(word_list)

display = []
for _ in chosen_word:
    display.append("_")

lives = 6

print("Welcome to Hangman!")

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print("You already guessed that letter.")
    
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. Lives left: {lives}")
    
    print(" ".join(display))

if "_" not in display:
    print("You win! 🎉")
else:
    print("You lose. The word was:", chosen_word)
