class CoffeeMachine:
    """
    Description:
    A state-machine simulation of a coffee maker. It tracks resource
    inventory, handles purchasing of different coffee types, manages
    refilling procedures, and processes cash withdrawals.

    Parameters:
    (No parameters for initialization)

    Returns:
    None: Interactions are managed are printed to the console.
    """


    recipe = {
        '1': {'name': 'espresso', 'water': 30, 'milk': 0, 'coffee': 9, 'price': 4},
        '2': {'name': 'latte', 'water': 30, 'milk': 120, 'coffee': 9, 'price': 7},
        '3': {'name': 'cappuccino', 'water': 30, 'milk': 60, 'coffee': 9, 'price': 6}
    }

    def __init__(self):
        self.res = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}
        self.state = "action"
        self.fill_steps = ['water', 'milk', 'beans', 'cups']
        self.current_fill = 0

    def print_state(self):
        """Displays the current inventory of resources and cash."""
        print(f"\nThe coffee machine has:\n{self.res['water']} of water\n{self.res['milk']} of milk\n"
              f"{self.res['beans']} of coffee beans\n{self.res['cups']} of disposable cups\n"
              f"{self.res['money']} of money")

    def process_inp(self, inp):
        """
        Description:
        Processes the user's input based on the current machine state.

        Parameters:
        inp (str): The command or numeric value entered by the user.

        Returns:
        bool: True if the machine should continue running, False if 'exit' was called.
        """
        if self.state == "action":
            if inp == "buy":
                self.state = "coffee"
                print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back:")
            elif inp == "fill":
                self.state = "fill"
                self.current_fill = 0
                print("\nWrite how many ml of water do you want to add:")
            elif inp == "take":
                print(f"\nI gave you {self.res['money']}")
                self.res['money'] = 0
            elif inp == "remaining":
                self.print_state()
            elif inp == "exit":
                return False


        elif self.state == "coffee":
            if inp != "back" and inp in self.recipe:
                r = self.recipe[inp]
                err = ("water" if self.res['water'] < r['water'] else
                       "milk" if self.res['milk'] < r['milk'] else
                       "coffee beans" if self.res['beans'] < r['coffee'] else
                       "cups" if self.res['cups'] < 1 else None)

                if err:
                    print(f"Sorry, not enough {err}!")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.res['water'] -= r['water']
                    self.res['milk'] -= r['milk']
                    self.res['beans'] -= r['coffee']
                    self.res['cups'] -= 1
                    self.res['money'] += r['price']
            self.state = "action"


        elif self.state == "fill":
            try:
                key = self.fill_steps[self.current_fill]
                self.res[key] += int(inp)
                self.current_fill += 1


                if self.current_fill < len(self.fill_steps):
                    next_step = self.fill_steps[self.current_fill]
                    print(f"Write how many {next_step} to add:")
                else:
                    self.state = "action"
            except ValueError:
                print("Enter a valid number")


        if self.state == "action":
            print("\nWrite action (buy, fill, take, remaining, exit):")
        return True


def main():
    """Main execution loop for the coffee machine."""
    machine = CoffeeMachine()
    print("Write action (buy, fill, take, remaining, exit):")
    while machine.process_inp(input("> ").strip().lower()):
        pass


if __name__ == "__main__":
    main()