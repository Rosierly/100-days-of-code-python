from art import logo
import os
import sys


def clear_screen():
    """Clear the console screen."""
    if sys.stdout.isatty():  # If running in a real terminal
        os.system('cls' if os.name == 'nt' else 'clear')
    else:  # Fallback for PyCharm console
        print("\n" * 40)


def display_logo(with_welcome: bool = False):
    print(f"{logo}\n")
    if with_welcome:
        print("Welcome to the Secret Auction Program.\n")


def get_bid(bids: dict[str, float]) -> tuple[str, float]:
    """Get a valid name and bid amount from the user and return it."""
    while True:
        name = input("What's your name? ")
        if name not in bids:  # avoid duplicate names
            break
        print("That name has already been used. Please try again.\n")

    while True:
        bid_amount = input("What is your bid? ").strip()
        try:
            bid_amount = float(bid_amount)
            break
        except ValueError:
            print("That's not a valid number. Please try again.\n")

    return name, bid_amount


def should_continue_bidding() -> bool:
    """Ask user if more bidders should be added."""
    while True:
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()

        if more_bidders in ("yes", "y"):
            return True
        elif more_bidders in ("no", "n"):
            return False
        else:
            print("Invalid input. Please try again.\n")


def find_highest_bidders(bids: dict[str, float]) -> tuple[list[str], float]:
    """Find and return the highest bid and the bidder(s) who placed it."""
    # Get the highest bid value
    top_bid = max(bids.values())

    # Collect all bidders who have that highest bid
    top_bidders = []
    for bidder, bid in bids.items():
        if bid == top_bid:
            top_bidders.append(bidder)

    return top_bidders, top_bid


def auction():
    """Run the auction program."""
    display_logo(with_welcome=True)
    all_bids = {}

    continue_bidding = True
    while continue_bidding:
        # Get bidder info and store it
        bidder_name, bid_value = get_bid(all_bids)
        all_bids[bidder_name] = bid_value

        # Check if there are any more bidders and clear screen
        continue_bidding = should_continue_bidding()
        clear_screen()
        display_logo()

    # Determine and display the winner(s)
    winners, winning_amount = find_highest_bidders(all_bids)
    if len(winners) == 1:
        print(f"The winner is {winners[0]} with a bid of ${winning_amount:.2f}.")
    else:
        print(f"The winners are {' and '.join(winners)} with a bid of ${winning_amount:.2f}.")


auction()
