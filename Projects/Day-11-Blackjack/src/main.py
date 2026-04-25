# HOUSE RULES
# - The deck is unlimited in size.
# - There are no jokers.
# - The Jack/Queen/King all count as 10.
# - The Ace can count as 11 or 1.
# - Use the following list as the deck of cards:
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# - The cards in the list have equal probability of being drawn.
# - Cards are not removed from the deck as they are drawn.
# - The computer is the dealer.

from art import logo
import random
import os
import sys

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

MESSAGES = {
    "user_bust": "You went over. You lose.",
    "dealer_bust": "The dealer went over. You win.",
    "natural": "Congratulations! You win with a natural blackjack.",
    "draw": "It's a draw.",
    "user_win": "Congratulations. You win.",
    "dealer_win": "You lose."
}


def reset_screen():
    """Clear the console screen and display the program logo."""
    if sys.stdout.isatty():  # If running in a real terminal
        os.system('cls' if os.name == 'nt' else 'clear')
    else:  # Fallback for PyCharm console
        print("\n" * 40)

    print(logo)


def get_cards(amount_of_cards: int) -> list:
    """Return a list of randomly drawn cards and adjust Aces if needed."""
    hand = [random.choice(CARDS) for _ in range(amount_of_cards)]
    check_for_ace(hand)
    return hand


def check_for_ace(hand: list):
    """Convert Aces from 11 to 1 if the hand exceeds 21."""
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1


def display_cards(user: list, dealer: list, final_hand: bool = False):
    """Display the user's and dealer's cards depending on the game stage."""
    if final_hand:
        print(f"  Your final hand: {user}, final score: {sum(user)}")
        print(f"  Computer's final hand: {dealer}, final score: {sum(dealer)}")
    else:
        print(f"    Your cards: {user}, current score: {sum(user)}")
        print(f"    Computer's first card: {dealer[0]}")


def determine_winner(user: list, dealer: list) -> str:
    """Return the game outcome code based on user and dealer scores."""
    user_score = sum(user)
    dealer_score = sum(dealer)

    # Busts
    if user_score > 21:
        return "user_bust"
    if dealer_score > 21:
        return "dealer_bust"

    # Naturals
    if len(user) == 2 and user_score == 21 and len(dealer) == 2 and dealer_score == 21:
        return "draw"
    if len(user) == 2 and user_score == 21:
        return "natural"
    if len(dealer) == 2 and dealer_score == 21:
        return "dealer_win"

    # Normal comparison
    if user_score == dealer_score:
        return "draw"
    if user_score > dealer_score:
        return "user_win"
    return "dealer_win"


def run_blackjack():
    """Run the Blackjack game."""
    while True:
        answer = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()
        if answer != "y":
            print("Goodbye!")
            break

        reset_screen()

        # Initial deal: two cards for both player and dealer
        user_cards = get_cards(2)
        dealer_cards = get_cards(2)
        display_cards(user_cards, dealer_cards)

        # User's turn
        while sum(user_cards) < 21:
            another_card = input("Type 'y' to get another card, or type anything else to pass: ").strip().lower()
            if another_card == "y":
                user_cards.extend(get_cards(1))
                display_cards(user_cards, dealer_cards)
            else:
                break

        # Dealer's turn: draw until reaching at least 17
        while sum(dealer_cards) < 17:
            dealer_cards.extend(get_cards(1))

        # Final results
        display_cards(user_cards, dealer_cards, final_hand=True)
        result = determine_winner(user_cards, dealer_cards)
        print(MESSAGES[result])


run_blackjack()
