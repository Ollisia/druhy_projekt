"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Olga Portešová
email: olikportesova@seznam.cz
"""
import random

length = 4
separator = "-" * 47


def generate_secret_number():
    """
    generating a secret number
    the first number must not start with a zero
    converting to string
    subsequent concatenation of numbers into one string
    """
    numbers = list(range(10))
    first_numbers = list(range(1, 10))

    first_number = random.choice(first_numbers)
    numbers.remove(first_number)

    other_numbers = random.sample(numbers, length - 1)

    secret_numbers = [first_number] + other_numbers

    secret_number = [str(cislo) for cislo in secret_numbers]
    secret_number = "".join(secret_number)
    return secret_number


def validate_tip(user_tip):
    """
    list of conditions
    exact description of the entered number
    """
    if not user_tip.isdigit():
        print("Enter numbers only.")
        return False
    elif len(user_tip) != length:
        print("Enter a four-digit number.")
        return False
    elif user_tip[0] == "0":
        print("The entered number must not start with a zero.")
        return False
    elif len(set(user_tip)) != len(user_tip):
        print("Enter unique numbers.")
        return False
    return True


def evaluate_guess(guess, secret):
    """
    if the guessed number is in the same place as the secret number, a bull is added
    if the guessed number is in the secret number, but in a different place, a cow is added
    """
    bulls = 0
    cows = 0
    for x in range(length):
        if guess[x] == secret[x]:
            bulls += 1
        if guess[x] in secret and guess[x] != secret[x]:
            cows += 1
    return (bulls, cows)


def main():
    """
    main function to run bulls and cows game
    """

    # greeting the user
    print("Hi there!")
    print(separator)

    # writing the introductory text
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(separator)

    # generating a secret number
    secret = generate_secret_number()

    # pre-arrangement of variables
    attempts = 0
    bulls = 0

    print("Enter a number:")
    print(separator)

    # main game loop
    while bulls != length:
        user_tip = input(">>> ")
        if not validate_tip(user_tip):
            print(separator)
            continue
        attempts += 1
        bulls, cows = evaluate_guess(user_tip, secret)
        print(f"{bulls} bull{"s" if bulls != 1 else ""}, {cows} cow{"s" if cows != 1 else ""}")
        print(separator)
        if bulls == length:
            print(f"Correct, you've guessed the right number in")
            print(f"{attempts} guesses!")
            print(separator)
            print("That's amazing!")


if __name__ == "__main__":
    main()