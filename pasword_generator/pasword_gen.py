import string
import random


def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 for good security."

    # Characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters for the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
