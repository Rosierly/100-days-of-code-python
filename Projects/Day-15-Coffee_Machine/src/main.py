# 1.Makes 3 hot flavors
#  Espresso
#  Latte
#  Cappuccino

# 2.Coin Operated
#  Penny = 1 cent
#  Nickel = 5 cents
#  Dime = 10 cents
#  Quarter = 25 cents

# TODO :Program Requirements
#  1.Print report (show remaining resources in the machine)
#  2.Check if the resources are sufficient
#  3.Process coins
#  4.Check if the transaction is successful
#  5.Make coffee (update resources accordingly)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Current available resources in the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Maps each resource to its unit of measurement
unit_by_resource = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}

# Coin values used for calculating total inserted money
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

# Total money collected by the machine
money = 0


# -------------------- LOGIC --------------------
def check_resources(selected_coffee):
    """Check if enough resources are available for the selected coffee."""
    for resource, amount_needed in MENU[selected_coffee]["ingredients"].items():
        if resources[resource] < amount_needed:
            return False, resource
    return True, None


def process_transaction(machine_balance, money_inserted, cost_of_coffee):
    """Validate payment and return updated balance with change or refund."""
    # Check if the inserted money is sufficient
    if money_inserted < cost_of_coffee:
        return False, machine_balance, money_inserted  # refund

    # Update machine balance and calculate change
    machine_balance += cost_of_coffee
    change = round(money_inserted - cost_of_coffee, 2)
    return True, machine_balance, change


def update_resources(available_resources, selected_coffee):
    """Deduct required ingredients from available resources."""
    for resource, amount_needed in MENU[selected_coffee]["ingredients"].items():
        available_resources[resource] -= amount_needed


# -------------------- UI --------------------
def get_coffee():
    """Prompt user to select a valid coffee option."""
    while True:
        coffee_choice = input(f"What would you like? ({'/'.join(MENU)}): ").strip().lower()
        if coffee_choice in MENU:
            return coffee_choice
        print("That's not a valid choice. Please try again.")


def get_coin_input():
    """Collect coin input from user and return the total amount of the inserted money."""
    money_inserted = 0
    for coin_type, value in coins.items():
        while True:
            amount_of_coins = input(f"How many {coin_type}? ")
            if amount_of_coins.isdigit():
                money_inserted += int(amount_of_coins) * value
                break
            print("That's not a valid amount of coins. Please try again.")

    return round(money_inserted, 2)


def display_report():
    """Display available resources and total money."""
    for resource, amount in resources.items():
        print(f"{resource.title()}: {amount}{unit_by_resource[resource]}")
    print(f"Money: ${money:.2f}")


def add_resources():
    """Allow user to restock machine resources."""
    global resources
    while True:
        user_input = input(f"Select a resource to add [{', '.join(resources)}], or 'q' to quit: ").strip().lower()

        if user_input == "q":
            return

        if user_input not in resources:
            print("Invalid input. Please try again.")
            continue

        while True:
            amount = input(f"How much {user_input} would you like to add? ")
            if amount.isdigit():
                resources[user_input] += int(amount)
                print(f"{user_input.title()} has been added. "
                      f"Total amount: {resources[user_input]}{unit_by_resource[user_input]}")
                break
            print("Invalid amount. Please try again.")


# -------------------- MAIN FLOW --------------------
def process_order():
    """Handle a complete coffee order."""
    global money, resources

    coffee = get_coffee()

    # Ensure enough resources are available before taking payment
    is_resources_sufficient, missing_resource = check_resources(coffee)
    if not is_resources_sufficient:
        print(f"Sorry, there is not enough {missing_resource}.")
        return

    cost = MENU[coffee]["cost"]
    print(f"Your coffee costs ${cost:.2f}\nPlease insert coins.")
    money_received = get_coin_input()

    # Process payment
    is_money_sufficient, money, change_or_refund = process_transaction(money, money_received, cost)
    if not is_money_sufficient:
        print(f"Sorry that's not enough money. Your ${change_or_refund:.2f} has been refunded.")
        return
    if change_or_refund > 0:
        print(f"Here is ${change_or_refund:.2f} in change.")

    # Make coffee and update resources
    update_resources(resources, coffee)
    print(f"Here is your {coffee} ☕️. Enjoy!")


def coffee_machine():
    """Run the main coffee machine command loop."""
    menu_display = (
        "\n=== Coffee Machine Menu ===\n"
        "  order  - place an order\n"
        "  report - view resources\n"
        "  add    - restock resources\n"
        "  help   - show menu options\n"
        "  off    - turn off machine"
    )

    print(menu_display)

    while True:
        command = input("\nEnter command or type 'help' for options: ").strip().lower()

        if command == "order":
            process_order()
        elif command == "report":
            display_report()
        elif command == "add":
            add_resources()
        elif command == "help":
            print(menu_display)
        elif command == "off":
            break
        else:
            print("\nInvalid command. Please try again.")


coffee_machine()
