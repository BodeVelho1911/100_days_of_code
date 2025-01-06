from art import logo
import random as rd

# Functions
def deal_card():
    """Return a random card from the list of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return rd.choice(cards)

def calculate_score(card_deck):
    """Calculate the player score, check for blackjacks and
    check if in case of a bust (going over 21) there is an ace
    in the player deck"""
    score = sum(card_deck)
    if score == 21 and len(card_deck) == 2:
        return 0
    if 11 in card_deck and score > 21:
        card_deck.remove(11)
        card_deck.append(1)
    else:
        return score

def compare(player1_score, player2_score):
    """Compare the players scores and decide who wins and who loses"""
    if player1_score == player2_score:
        return "It's a draw! 😑"
    elif player2_score == 0:
        player2_score = 21
        return "Dealer hit BlackJack. You lose!! 😖"
    elif player1_score == 0:
        player1_score = 21
        return "BlackJack!! You win!!! 😎"
    elif player1_score > 21:
        return "Over 21. You lose!!! 😢"
    elif player2_score > 21:
        return "Dealer has gone over 21, you win!!! 😘"
    elif player1_score > player2_score:
        return "You win!!! 😎"
    else:
        return "You lose!!! 😢"


def play_blackjack():
    # Initialization
    user_cards = []
    dealer_cards = []
    user_score = -1
    dealer_score = -1
    is_game_over = False
    print(logo) # Logo for the game

    # Deal two cards at the beginning
    for _ in range(2):
        """Returns a random card from the deck"""
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Player's cards: {user_cards}, current value: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")
        if user_score == 0 or dealer_score == 0 or user_score> 21:
            is_game_over = True
        else:
            hit_or_stand = input("Type 'Y' to hit another card or 'N' to stand: ").lower()
            if hit_or_stand == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
    print(compare(user_score, dealer_score))
    print(f"Your hand: {user_cards}, your score: {user_score}")
    print(f"Dealer hand: {dealer_cards}, dealer score: {dealer_score}")

while input("Do you want to play a game of blackjack? Type 'Y' or 'N': ").lower() == "y":
    print("\n" * 100)
    play_blackjack()
