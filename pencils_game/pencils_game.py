import random

def pencils_game():
    """
    Description:
    Manages the logic for a pencil-taking game (Nim variation).
    Validates initial pencil count, handles turn-taking between a human
    and an AI with a winning strategy, and determines the winner.

    Parameters:
    (No parameters)

    Returns:
    None: The game state and winner are printed to the console.
    """
    while True:
        n_input = input("How many pencils would you like to use:\n")
        # Validate that the input is a number
        if not n_input.isdigit():
            print("The number of pencils should be numeric")
        elif int(n_input) <= 0:
            print("The number of pencils should be positive")
        else:
            num_pencils = int(n_input)
            break


    p1, bot = "John", "Jack"
    while True:
        current_player = input(f"Who will be the first ({p1}, {bot}):\n")
        if current_player in [p1, bot]:
            break
        print(f"Choose between '{p1}' and '{bot}'")


    while num_pencils > 0:

        print("|" * num_pencils)
        print(f"{current_player}'s turn!")


        if current_player == bot:
            if num_pencils == 1:
                taken = 1
            elif num_pencils % 4 == 0:
                taken = 3
            elif num_pencils % 4 == 3:
                taken = 2
            elif num_pencils % 4 == 2:
                taken = 1
            else:
                taken = random.randint(1, min(3, num_pencils))


            print(taken)
        else:
            while True:
                taken_input = input()
                if taken_input not in ['1', '2', '3']:
                    print("Possible values: '1', '2' or '3'")
                elif int(taken_input) > num_pencils:
                    print("Too many pencils were taken")
                else:
                    taken = int(taken_input)
                    break


        num_pencils -= taken


        if num_pencils == 0:
            winner = bot if current_player == p1 else p1
            print(f"{winner} won!")
            break


        current_player = bot if current_player == p1 else p1


if __name__ == "__main__":
    pencils_game()