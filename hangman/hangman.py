import random
import string
def play_game():
    """
        Description:
        Manages the core logic of the Hangman game, including word selection,
        user input validation, life tracking, and win/loss conditions.

        Parameters:
        (No parameters)

        Returns:
        None: Results are printed to the console.
        """


    words = ['python', 'java', 'javascript', 'php']
    secret_word = random.choice(words)
    word_display = list("-" * len(secret_word))


    lives = 8
    all_guessed = set()


    while lives > 0:
        print("\n" + "".join(word_display))
        user_input = input("Input a letter: > ")


        if len(user_input) != 1:
            print("You should input a single letter")
            continue


        if user_input not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
            continue


        if user_input in all_guessed:
            print("You've already guessed this letter")
            continue


        all_guessed.add(user_input)


        if user_input in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == user_input:
                    word_display[i] = user_input
        else:
            print("That letter doesn't appear in the word")
            lives -= 1


        if "-" not in word_display:
            print("\n" + "".join(word_display))
            print(f"You guessed the word {secret_word}!")
            print("You survived!")
            return


    print("You lost!")


def main():
    print("HANGMAN")


    while True:
        choice = input('Type "play" to play the game, "exit" to quit: > ').lower()

        if choice == "play":
            play_game()
        elif choice == "exit":
            break
        else:
            continue


if __name__ == "__main__":
    main()