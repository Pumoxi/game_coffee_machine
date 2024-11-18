from data import coffee,resource,finance
from art import logo

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01
TOPUP = 2.00

def get_input():
    """This is to print the welcome menu"""

    return input("What would you like? (espresso/latte/cappucino): ")

def print_report():
    """This is to print the report of the coffee machine"""

    print(f"Water: {resource['water']}ml")
    print(f"Milk: {resource['milk']}ml")
    print(f"Coffee: {resource['coffee']}g")
    print(f"Cash: ${finance['cash']}")

def check_available_resources(choice_of_coffee):

    for item in resource:
        if resource[item] < coffee[choice_of_coffee]['ingredients'][item]:
            print(f"Sorry there is not enough {item}.")
            return False

    return True

def ask_for_money():
    """This is to ask for money from the user"""

    money_received = {}

    print("Please insert coins.")

    try:
        money_received = {
            "quarters": int(input("How many quarters?: ")),
            "dimes": int(input("How many dimes?: ")),
            "nickles": int(input("How many nickles?: ")),
            "pennies": int(input("How many pennies?: "))
        }
        
    except Exception as e:
        print("Invalid number. Please enter number")

    return money_received

def calculate_money(money_received):
    """This is to calculate the money from the user"""

    total = (money_received['quarters'] * QUARTERS) + (money_received['dimes'] * DIMES) + (money_received['nickles'] * NICKLES) + (money_received['pennies'] * PENNIES)

    return total

def return_change(money_received, cost):
    """This is to return the change to the user"""

    change = money_received - cost

    print(f"Here is ${change} in change.")

def update_income(cost):
    finance['cash'] += cost

def make_coffee(choice_of_coffee):
    """This is to make the coffee"""

    for item in coffee[choice_of_coffee]['ingredients']:
        resource[item] -= coffee[choice_of_coffee]['ingredients'][item]

    print(f"Here is your {choice_of_coffee}. Enjoy!")

def topup():
    """This is to top up the resources of the coffee machine"""

    if finance['cash'] >= TOPUP:

        resource['water'] = 300
        resource['milk'] = 200
        resource['coffee'] = 100
        finance['cash'] -= TOPUP

        print("Resources topped up.")
    
    else:

        print("Not enough money to top up.")

def main():

    print(logo)

    exit_program = False

    while not exit_program:

        try:
            choice_of_coffee = get_input().lower()

            if choice_of_coffee == "report":
                print_report()
            elif choice_of_coffee == "off":
                exit_program = True
            elif choice_of_coffee == "topup":
                topup()
            else:
                if check_available_resources(choice_of_coffee):
                    money_received = calculate_money(ask_for_money())
                    cost = coffee[choice_of_coffee]['cost']

                    if money_received < cost:
                        print("Sorry that's not enough money. Money refunded.")
                    else:
                        if money_received > cost:
                            return_change(money_received, cost)
                        update_income(cost)
                        make_coffee(choice_of_coffee)

        except Exception as e:
            print("Invalid choice. Please enter valid choice.")

if __name__ == "__main__":
    main()

