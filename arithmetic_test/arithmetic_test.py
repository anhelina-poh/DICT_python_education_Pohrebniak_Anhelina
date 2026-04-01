import random

class InvalidInputError(Exception):
    """Custom exception raised when user input is not a valid integer."""
    pass

class ArithmeticTestApp:
    """
    A math testing application for generating and scoring arithmetic problems.

    Maintains a history of test results and supports different difficulty levels
    with the ability to save progress to a file.
    """

    def __init__(self) -> None:
        """Initialize the application with empty results and level definitions."""
        self.results: list[tuple[int, int]] = []
        self.level_descriptions: dict[int, str] = {
            1: "simple operations with numbers 2-9",
            2: "integral squares of 11-29"
        }

    @staticmethod
    def _get_integer_input() -> int:
        """
        Helper method to ensure input is an integer.

        Returns:
            int: The integer value entered by the user.

        Raises:
            InvalidInputError: If the input is not a valid integer.
        """
        user_input = input("> ").strip()
        try:
            return int(user_input)
        except ValueError:
            raise InvalidInputError("Incorrect format.") from None

    def choose_level(self) -> int:
        """
        Prompt the user to select a difficulty level with input validation.

        Returns:
            int: The selected level (1 or 2).
        """
        while True:
            print("Which level do you want? Enter a number:")
            print("1 - simple operations with numbers 2-9")
            print("2 - integral squares of 11-29")
            try:
                level = self._get_integer_input()
                if level in (1, 2):
                    return level
                print("Incorrect format.")
            except InvalidInputError:
                print("Incorrect format.")

    @staticmethod
    def generate_task(level: int) -> tuple[str, int]:
        """
        Generate a math problem based on the chosen level.

        Args:
            level (int): The difficulty level (1 for arithmetic, 2 for squares).

        Returns:
            tuple[str, int]: A tuple containing the question string and the integer answer.
        """
        if level == 1:
            num1 = random.randint(2, 9)
            num2 = random.randint(2, 9)
            op = random.choice(['+', '-', '*'])
            question = f"{num1} {op} {num2}"

            if op == '+':
                answer = num1 + num2
            elif op == '-':
                answer = num1 - num2
            else:
                answer = num1 * num2

            return question, answer

        num = random.randint(11, 29)
        return str(num), num ** 2

    def play_level(self, level: int) -> int:
        """
        Execute a round of 5 questions for the specified level.

        Args:
            level (int): The level to play.

        Returns:
            int: The number of correct answers (0 to 5).
        """
        correct_count = 0
        total_questions = 5

        for _ in range(total_questions):
            question, correct_answer = self.generate_task(level)
            print(question)

            while True:
                try:
                    user_ans = self._get_integer_input()
                    break
                except InvalidInputError:
                    print("Incorrect format.")

            if user_ans == correct_answer:
                print("Right!")
                correct_count += 1
            else:
                print("Wrong!")

        self.results.append((correct_count, level))
        return correct_count

    def save_results(self) -> None:
        """Append the test results and user's name to 'results.txt'."""
        if not self.results:
            return

        choice = input("Would you like to save the result? Enter yes or no.\n> ").strip().lower()
        if choice in ['yes', 'y']:
            name = input("What is your name?\n> ").strip()
            try:
                with open("results.txt", "a", encoding="utf-8") as file:
                    for score, lvl in self.results:
                        desc = self.level_descriptions[lvl]
                        file.write(f"{name}: {score}/5 in level {lvl} ({desc}).\n")
                print('The results are saved in "results.txt".')
            except OSError as e:
                print(f"Error saving file: {e}")

    def run(self) -> None:
        """Start the main control flow of the application."""
        current_level = self.choose_level()
        score = self.play_level(current_level)
        print(f"Your mark is {score}/5.")

        if current_level == 1:
            choice = input("Would you like to try level 2? Enter yes or no.\n> ").strip().lower()
            if choice in ['yes', 'y']:
                score2 = self.play_level(2)
                print(f"Your mark is {score2}/5.")

        self.save_results()


if __name__ == "__main__":
    app = ArithmeticTestApp()
    app.run()