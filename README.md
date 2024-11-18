[Link to my blogpost](https://pumoxi.com/2024/11/18/python-coffee-machine-game-simulating-a-real-life-experience/)

# Coffee Machine Simulator

A Python-based coffee machine simulator that allows users to:

- Order espresso, latte, or cappuccino.
- Insert virtual coins to pay for coffee.
- Manage coffee machine resources (water, milk, coffee).
- Print resource reports.
- Top up the machine resources when needed.
- Turn off the machine.

This project is perfect for learning fundamental Python concepts such as functions, loops, conditionals, and exception handling.

---

## Features

1. **Order Coffee**  
   Choose from espresso, latte, or cappuccino. The machine checks if enough resources are available before making the coffee.

2. **Insert Coins**  
   The machine accepts quarters, dimes, nickels, and pennies, calculating the total and returning any change.

3. **Resource Management**  
   View the current resource levels with the `report` command and refill the machine when required.

4. **Cost Calculation**  
   The machine ensures the user pays the correct amount before dispensing the coffee.

5. **Admin Controls**  
   - `report`: Displays the current machine resources and income.
   - `topup`: Refills the machine resources (if enough money is collected).
   - `off`: Turns off the machine.

---

## Installation

1. Clone this repository:
   ```bash
   git clone git@github.com:Pumoxi/game_coffee_machine.git
   ```

2.	Navigate to the project directory:

    ```bash
    cd game_coffee_machine
    ```

3.	Run the script:

    ```bash
    python main.py
    ```

## How to Use

1. **Start the machine**
Run the script and follow the on-screen prompts.

2.	**Commands**:
    - Enter `espresso, latte, or cappuccino` to order a coffee.
    - Enter `report` to view the current resource levels.
	- Enter `topup` to refill machine resources (requires sufficient income).
	- Enter `off` to shut down the machine.

3.	**Insert coins**
When prompted, input the number of quarters, dimes, nickels, and pennies to pay for your coffee.

## Example

```plaintext
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 12
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.50 in change.
Here is your latte. Enjoy!
```

## Project Structure

- `main.py`: The main script containing the coffee machine functionality.
- `data.py`: Contains pre-defined coffee recipes, resources, and initial income.
- `art.py`: Contains the logo for this application.

## Data Structure Overview

**Coffee Recipes (coffee)**

```python
coffee = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}
```

**Resources (resource)**

```python
resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
```

**Income (income)**

```python
income = 0.0
```

## Acknowledgments

- The development of this project was inspired by course “Master Python by building 100 projects in 100 days”, Dr. Angela Yu.