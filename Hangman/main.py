from random import choice

word_list: list[str] = ["apple", "orange", "banana", "cherry", "blueberry", "strawberry", "peach", "pear", "berry"]


def run_game():
    word: str = choice(word_list)

    username: str = input("Please enter your username? -> ")
    print(f"Welcome to hangman, {username}!")

    guessed: str = ''
    tries: int = 4

    while tries > 0:
        blanks: int = 0

        print("Word: ", end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print("_", end='')
                blanks += 1

        print()  # Adds a blank line

        if blanks == 0:
            print("You guessed the word!")
            break

        guess: str = input("Guess a letter? -> ").lower()

        if len(guess) > 1:  # Picks the first char of the input
            guess = guess[0]

        if guess in guessed:
            print(f"You already guessed {guess}!")
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f"Sorry, that was wrong... {tries} tries left.")

            if tries == 0:
                print("No more tries remaining... You Lose.")


if __name__ == "__main__":
    run_game()
