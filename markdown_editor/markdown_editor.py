class MarkdownEditor:
    """
    An interactive command-line tool for creating Markdown files.

    Maintains a running string of formatted text and provides
    methods to append headers, links, lists, and standard text styles.
    """

    def __init__(self):
        """Initialize the editor with an empty document and available formatters."""
        self.document = ""
        self.formatters = [
            "plain", "bold", "italic", "header", "link",
            "inline-code", "ordered-list", "unordered-list", "new-line"
        ]

    def show_help(self):
        """Print the available commands and formatters."""
        print(f"Available formatters: {' '.join(self.formatters)}")
        print("Special commands: !help !done")

    def add_header(self):
        """Prompts for a header level (1-6) and text, then appends it."""
        while True:
            try:
                level = int(input("Level: > "))
                if 1 <= level <= 6:
                    break
                print("The level should be within the range of 1 to 6.")
            except ValueError:
                print("The level should be within the range of 1 to 6.")

        text = input("Text: > ")
        self.document += f"{'#' * level} {text}\n"

    def add_link(self):
        """Prompts for a label and URL to create a Markdown link [label](url)."""
        label = input("Label: > ")
        url = input("URL: > ")
        self.document += f"[{label}]({url})"

    def add_list(self, is_ordered: bool):
        """Prompts for the number of rows and populates an ordered or unordered list."""
        while True:
            try:
                rows = int(input("Number of rows: > "))
                if rows > 0:
                    break
                print("The number of rows should be greater than zero")
            except ValueError:
                print("The number of rows should be greater than zero")

        for i in range(1, rows + 1):
            row_text = input(f"Row #{i}: > ")
            prefix = f"{i}." if is_ordered else "*"
            self.document += f"{prefix} {row_text}\n"

    def apply_formatter(self, choice: str):
        """Routes the user's choice to the specific formatting logic."""
        if choice == "new-line":
            self.document += "\n"
        elif choice == "header":
            self.add_header()
        elif choice == "link":
            self.add_link()
        elif choice == "ordered-list":
            self.add_list(is_ordered=True)
        elif choice == "unordered-list":
            self.add_list(is_ordered=False)
        else:
            text = input("Text: > ")
            if choice == "plain":
                self.document += text
            elif choice == "bold":
                self.document += f"**{text}**"
            elif choice == "italic":
                self.document += f"*{text}*"
            elif choice == "inline-code":
                self.document += f"`{text}`"

    def save_and_exit(self):
        """Writes the accumulated document string to a file."""
        try:
            with open("output.md", "w", encoding="utf-8") as file:
                file.write(self.document)
        except OSError as e:
            print(f"Error saving file: {e}")

    def run(self):
        """The main execution loop for the editor."""
        while True:
            choice = input("Choose a formatter: > ").strip()

            if choice == "!help":
                self.show_help()
            elif choice == "!done":
                self.save_and_exit()
                break
            elif choice not in self.formatters:
                print("Unknown formatting type or command")
            else:
                self.apply_formatter(choice)

                if self.document:
                    print(self.document)


if __name__ == "__main__":
    editor = MarkdownEditor()
    editor.run()