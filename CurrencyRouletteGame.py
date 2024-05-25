import requests
from forex_python.converter import CurrencyRates
import random


def get_money_interval(levelOfDifficulty):

    CurrencyRatesResult = CurrencyRates()
    CurrencyRatesResult = CurrencyRatesResult.get_rate('ILS', 'USD')

    randomNumberResult = random.randint(1, 100)
    print(f'{randomNumberResult} is the amount USD, what do you think will be the value of current currency rate from USD to ILS?')
    lowRange = (randomNumberResult-(5-levelOfDifficulty))/CurrencyRatesResult
    HighRange = (randomNumberResult+(5-levelOfDifficulty))/CurrencyRatesResult
    return lowRange, HighRange


def get_guess_from_user(lowRange, HighRange):
    print(f'What do you think will be the value of current currency rate from USD to ILS of t?')
    number_from_user = input()
    number_from_user = int(number_from_user)

    if number_from_user <= lowRange or number_from_user > HighRange:
        return False
    else:
        return True


def play(levelOfDifficulty):
    print(f"\nYou have chosen Currency Roulette, and level of difficulty {
          levelOfDifficulty}. you will now enter the game.\n")
    lowRange, HighRange = get_money_interval(levelOfDifficulty)
    answer = get_guess_from_user(lowRange, HighRange)
    print(f'the low range is {lowRange} and the high range is {HighRange}')
    return answer
