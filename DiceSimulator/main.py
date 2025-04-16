from random import randint


def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = [randint(1, 6) for _ in range(amount)]
    return rolls


def main():
    while True:
        try:
            user_input = input("How many dice would you like to roll? (type e to exit): ")

            if user_input.lower() == "e":
                print("Thanks for playing.")
                break

            rolls = roll_dice(int(user_input))
            print(*rolls, sep=", ", end="")
            print(f" (sum: {sum(rolls)})")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
