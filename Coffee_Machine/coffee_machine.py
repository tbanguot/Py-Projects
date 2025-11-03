

class CoffeeMachine:

    def __init__(self):
        # Available resources
        self.resources = {
            'water': 300,
            'coffee': 100,
            'milk': 200,
        }
        # Available menu
        self.menu = {
            'espresso': {
                'ingredients': {
                    'water': 50,
                    'coffee': 18,
                    'milk': 0
                },
                'cost': 1.50
            },
            'latte': {
                'ingredients': {
                    'water': 200,
                    'coffee': 24,
                    'milk': 150,
                },
                'cost': 2.50
            },
            'cappuccino': {
                'ingredients': {
                    'water': 250,
                    'coffee': 24,
                    'milk': 100,
                },
                'cost': 3.0
            }
        }

        self.money = 0  # total amount

    def print_report(self):
        """
        Display the coffee machine report
        :return:
        """
        print(f'Water: {self.resources["water"]}ml')
        print(f'Milk: {self.resources["milk"]}ml')
        print(f'Coffee: {self.resources["coffee"]}g')
        print(f'Money: ${self.money}')

    def is_sufficient_resources(self, order):
        return self.menu[order]['ingredients']['water'] <= self.resources['water'] and \
            self.menu[order]['ingredients']['coffee'] <= self.resources['coffee'] and \
            self.menu[order]['ingredients']['milk'] <= self.resources['milk']


    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

        return total

    def make_order(self):
        return input("What would you like? (espresso/latte/cappuccino): ")

    def make_coffee(self, order):
        self.resources['water'] -= self.menu[order]['ingredients']['water']
        self.resources['coffee'] -= self.menu[order]['ingredients']['coffee']
        self.resources['milk'] -= self.menu[order]['ingredients']['milk']

    def process_order(self, order):

        while order.lower() != "off":
            if order == "report":
                self.print_report()
            else:
                # Checks available resources
                if self.is_sufficient_resources(order):
                    amount = self.process_coins()  # Process payment

                    if amount >= self.menu[order]['cost']:
                        self.money += self.menu[order]['cost']
                        self.make_coffee(order)  # Make the transaction
                        print(f"Here is ${(amount - self.menu[order]['cost']):.2f} in change")
                        print(f"Here is your {order}. Enjoy!")
                    else:
                        print("Sorry, that's not enough money. Money refunded.")

                # Insufficient resources
                else:
                    print("Sorry there is not enough ", end="")
                    if self.menu[order]['ingredients']['water'] > self.resources['water']:
                        print("water")
                    elif self.menu[order]['ingredients']['coffee'] > self.resources['coffee']:
                        print("water")
                    elif self.menu[order]['ingredients']['milk'] > self.resources['milk']:
                        print("milk")

            # Prompt another order
            order = self.make_order()

        else:
            print("Machine is off for maintenance")


if __name__ == '__main__':
    machine = CoffeeMachine()
    user_order = machine.make_order()
    machine.process_order(user_order)
