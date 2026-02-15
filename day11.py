import random

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, dealer has Blackjack"
    elif user_score == 0:
        return "Win with Blackjack"
    elif user_score > 21:
        return "You went over"
    elif computer_score > 21:
        return "Dealer went over"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or_
