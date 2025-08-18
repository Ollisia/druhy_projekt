"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Olga Portešová
email: olikportesova@seznam.cz
"""
import random

# function to create a secret 4-digit number
def generate_secret_number():
    """
    generation of non-repeating numbers
    the first number must not start with a zero
    converting to string
    subsequent concatenation of numbers into one string
    """
    numbers = list(range(10))
    first_numbers = list(range(1, 10))

    first_number = random.choice(first_numbers)
    numbers.remove(first_number)

    other_numbers = random.sample(numbers, 3)

    secret_numbers = ([first_number] + other_numbers)

    secret_number = [str(cislo) for cislo in secret_numbers]
    secret_number = "".join(secret_number)
    return secret_number

# condition check function
def validate_tip(user_tip):
    """
    list of conditions
    exact description of the entered number
    """
    if not user_tip.isdigit():
        print("Enter numbers only.")
        return False
    elif len(user_tip) != 4:
        print("Enter a four-digit number.")
        return False
    elif user_tip[0] == "0":
        print("The entered number must not start with a zero.")
        return False
    elif len(set(user_tip)) != len(user_tip):
        print("Enter unique numbers.")
        return False
    return True

# cow and bull counting function
def evaluate_guess(guess, secret):
    """
    if the guessed number is in the same place as the secret number, a bull is added
    if the guessed number is in the secret number, but in a different place, a cow is added
    """
    bulls = 0
    cows = 0
    for x in range(4):
        if guess[x] == secret[x]:
            bulls += 1
        if guess[x] in secret:
            cows += 1
    return (bulls, cows)


# greeting the user
print("Hi there!")
print("-" * 47)


# writing the introductory text
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-" * 47)


# generating a secret number
secret = generate_secret_number()

# pre-arrangement of variables
attempts = 0
bulls = 0
first_quest = True

# main game loop
# entering the guessed number
# deciding whether it is a bull or a cow
# the game ends when there are four bulls
while bulls != 4:
    if first_quest:
        print("Enter a number:")
        print("-" * 47)
        first_quest = False
    user_tip = input(">>> ")
    while not validate_tip(user_tip):
        print("-" * 47)
        user_tip = input(">>> ")
    attempts += 1
    bulls, cows = evaluate_guess(user_tip, secret)
    print(f"{bulls} bull{"s" if bulls != 1 else ""}, {cows} cow{"s" if cows != 1 else ""}")
    print("-" * 47)
    if bulls == 4:
        print(f"Correct, you've guessed the right number in")
        print(f"{attempts} guesses!")
        print("-" *47)
        print("That's amazing!")