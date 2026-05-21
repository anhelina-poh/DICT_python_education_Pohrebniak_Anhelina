import random
from typing import Dict, List, Set


class RockPaperScissors:
    """
    Description:
    A flexible Rock-Paper-Scissors game engine. It supports custom options,
    tracks user ratings via a local file, and implements a circular logic
    algorithm to determine winners in extended versions of the game.

    Parameters:
    (No parameters for initialization)

    Returns:
    None: The game runs in a command-line loop.
    """

    def __init__(self) -> None:
        self.name: str = ""
        self.score: int = 0
        self.options: List[str] = []
        self.beats: Dict[str, Set[str]] = {}

    def get_starting_score(self) -> int:
        """Reads the initial player rating from rating.txt if available."""
        try:
            with open("rating.txt", "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 2 and parts[0] == self.name:
                        return int(parts[1])
        except FileNotFoundError:
            pass
        return 0

    def compute_beats(self) -> None:
        """
        Calculates the game rules dynamically.
        For any option in a list, the options that come after it (circularly)
        are split into two halves. The second half contains the options
        that the current option beats.
        """
        self.beats.clear()
        for i, opt in enumerate(self.options):
            ordered = self.options[i + 1:] + self.options[:i]
            half = len(ordered) // 2

            self.beats[opt] = set(ordered[half:])

    def setup_game(self) -> None:
        """Handles the initial game configuration and player greeting."""
        self.name = input("Enter your name: > ").strip()
        print(f"Hello, {self.name}")
        self.score = self.get_starting_score()

        opts_input = input("> ").strip().lower()
        if opts_input:
            self.options = [opt.strip() for opt in opts_input.split(",")]
        else:
            self.options = ["rock", "paper", "scissors"]

        self.compute_beats()
        print("Okay, let's start")

    def determine_winner(self, user_choice: str, comp_choice: str) -> str:
        """Uses the pre-calculated beats dictionary to find the result."""
        if user_choice == comp_choice:
            return "draw"
        if comp_choice in self.beats[user_choice]:
            return "win"

        return "lose"

    def play(self) -> None:
        """The main game loop handling inputs and score updates."""
        self.setup_game()

        while True:
            user_input = input("> ").strip().lower()

            if user_input == "!exit":
                print("Bye!")
                break
            elif user_input == "!rating":
                print(f"Your rating: {self.score}")
            elif user_input in self.options:
                comp_choice = random.choice(self.options)
                result = self.determine_winner(user_input, comp_choice)

                if result == "draw":
                    print(f"There is a draw ({comp_choice})")
                    self.score += 50
                elif result == "win":
                    print(f"Well done. The computer chose {comp_choice} and failed")
                    self.score += 100
                else:
                    print(f"Sorry, but the computer chose {comp_choice}")
            else:
                print("Invalid input")


if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()