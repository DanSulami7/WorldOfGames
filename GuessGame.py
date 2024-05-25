import random


def generate_number(levelOfDifficulty):
    secret_number = random.randint(1, levelOfDifficulty)
    return secret_number


def get_guess_from_user(levelOfDifficulty):
    print(f"Please enter a number between 1 and {levelOfDifficulty}: ")
    number_from_user = input()
    number_from_user = int(number_from_user)
    return number_from_user


def compare_results(num1, num2):
    if num1 == num2:
        return True
    else:
        return False


def play(levelOfDifficulty):
    print(f"\nYou have chosen Guess Game, and level of difficulty {
          levelOfDifficulty}. you will now enter the game.\n")
    secret_number = generate_number(levelOfDifficulty)
    numberFromUser = get_guess_from_user(levelOfDifficulty)
    number_from_user = int(numberFromUser)
    compareTheResults = compare_results(secret_number, numberFromUser)
    print(f'The secret number is {
          secret_number} and the number from user is {number_from_user}')
    return compareTheResults
