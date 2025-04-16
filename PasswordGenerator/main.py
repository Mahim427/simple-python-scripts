import string
import secrets


def contains_upper(password: str) -> bool:
    return any(char.isupper() for char in password)


def contains_symbols(password: str) -> bool:
    return any(char in string.punctuation for char in password)


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length: int = len(combination)

    while True:
        new_password: str = "".join(
            combination[secrets.randbelow(combination_length)]
            for _ in range(length)
        )
        if contains_upper(new_password) == uppercase and contains_symbols(new_password) == symbols:
            break

    return new_password


if __name__ == "__main__":
    for i in range(1, 6):
        new_pass: str = generate_password(length=3, symbols=False, uppercase=True)
        specs: str = f"U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}"
        print(f"{i} -> {new_pass} ({specs})")
