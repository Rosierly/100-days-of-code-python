from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

menu_display = (
    "\n=== Coffee Machine Menu ===\n"
    "  order  - place an order\n"
    "  report - view resources\n"
    "  help   - show menu options\n"
    "  off    - turn off machine"
)

print(menu_display)


def coffee_machine():
    """Run the main coffee machine command loop."""
    while True:
        command = input("\nEnter command or type 'help' for options: ").strip().lower()

        if command == "order":
            user_input = input(f"What would you like ({menu.get_items()}): ").strip().lower()
            drink = menu.find_drink(user_input)

            if not drink:
                continue  # Invalid drink, skip and ask again

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

        elif command == "report":
            coffee_maker.report()
            money_machine.report()

        elif command == "help":
            print(menu_display)

        elif command == "off":
            break

        else:
            print("Invalid command. Please try again.")


coffee_machine()
