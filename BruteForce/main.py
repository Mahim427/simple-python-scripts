import itertools
import string
import time
from typing import List


def common_guess(word: str) -> str | None:
    with open('words.txt', 'r') as words:
        word_list: List[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f"Common match: {match} (#{i})"


def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    chars: str = string.ascii_lowercase
    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    # itertools.product return every combination of given string
    # product(range(2), repeat=3) → 000 001 010 011 100 101 110 111 -> returns List
    for attempts, guess in enumerate(itertools.product(chars, repeat=length), start=1):
        guess: str = "".join(guess)

        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses'

        # print(guess, attempts)


def main():
    print("Searching...")
    password: str = 'lmnop'

    start_time: float = time.perf_counter()

    if common_match := common_guess(password):
        print(common_match)
    elif cracked := brute_force(password, length=len(password)):
        print(cracked)
    else:
        print("There was no match.")

    end_time = time.perf_counter()
    print(round(end_time - start_time, 2), 'seconds')


if __name__ == '__main__':
    main()
