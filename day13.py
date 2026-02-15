import random

data = [
    {"name": "Instagram", "followers": 600},
    {"name": "Cristiano Ronaldo", "followers": 550},
    {"name": "Ariana Grande", "followers": 380},
    {"name": "YouTube", "followers": 500},
]

def get_random():
    return random.choice(data)

def play():
    score = 0
    a = get_random()
    b = get_random()

    while True:
        print(f"A: {a['name']}")
        print(f"B: {b['name']}")

        guess = input("Who has more followers? A or B: ").upper()
        
        if (a["followers"] > b["followers"] and guess == "A") or \
           (b["followers"] > a["followers"] and guess == "B"):
            score += 1
            print(f"Correct! Score: {score}")
            a = b
            b = get_random()
        else:
            print("Wrong! Final score:", score)
            break

play()
