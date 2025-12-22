def print_grid():
    """
    Description:
    Renders the current state of the 3x3 Tic-Tac-Toe board to the console,
    framed by decorative dashes and vertical bars.
    """
    print("---------")
    print(f"| {cells[0]} {cells[1]} {cells[2]} |")
    print(f"| {cells[3]} {cells[4]} {cells[5]} |")
    print(f"| {cells[6]} {cells[7]} {cells[8]} |")
    print("---------")


def check_game_state():
    """
    Description:
    Evaluates the board to determine if there is a winner (X or O),
    if the game is a draw, or if it should continue.

    Returns:
    str: 'X wins', 'O wins', 'Draw', or None if the game is ongoing.
    """
    win_indices = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]


    x_wins = any(cells[i] == cells[j] == cells[k] == 'X' for i, j, k in win_indices)
    o_wins = any(cells[i] == cells[j] == cells[k] == 'O' for i, j, k in win_indices)

    if x_wins:
        return "X wins"
    if o_wins:
        return "O wins"
    if "_" not in cells and " " not in cells:
        return "Draw"
    return None



cells = [" "] * 9
print_grid()


current_player = "X"


while True:
    user_input = input("Enter the coordinates: ").split()


    if not all(char.isdigit() or (char.startswith('-') and char[1:].isdigit()) for char in user_input):
        print("You should enter numbers!")
        continue


    if len(user_input) != 2:
        continue


    col, row = map(int, user_input)


    if not (1 <= col <= 3 and 1 <= row <= 3):
        print("Coordinates should be from 1 to 3!")
        continue


    index = (row - 1) * 3 + (col - 1)


    if cells[index] != " ":
        print("This cell is occupied! Choose another one!")
        continue


    cells[index] = current_player
    print_grid()


    result = check_game_state()
    if result:
        print(result)
        break


    current_player = "O" if current_player == "X" else "X"