import MemoryGame
import GuessGame
import CurrencyRouletteGame
import Score


def welcome(name):
    return print(f"\nHello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n")


def load_game():
    print(f"Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer.\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS.")
    print(f"Please enter your choice:", end=" ")
    playerChoice = input()

    while playerChoice not in ["1", "2", "3"]:
        print(f"\n*** Wrong input, please enter a number between 1 - 3 ***\n\nPlease enter your choice:", end=" ")
        playerChoice = input()

    print(f"\nPlease choose game difficulty from 1 to 5:\nPlease enter your choice:", end=" ")
    levelOfDifficulty = input()

    while levelOfDifficulty not in ["1", "2", "3", "4", "5"]:
        print(f"\n*** Wrong input, please enter a number between 1 - 5*** \n\nEnter your choice:", end=" ")
        levelOfDifficulty = input()

    levelOfDifficulty = int(levelOfDifficulty)

    if playerChoice == "1":
        gameResult = MemoryGame.play(levelOfDifficulty)
        if gameResult == True:
            Score.add_score(levelOfDifficulty)
            print(f"\nYou have won the game! 🎉🎉🎉")
        else:
            print(f"\nYou have lost the game! 😭😭")
    elif playerChoice == "2":
        gameResult = GuessGame.play(levelOfDifficulty)
        if gameResult == True:
            Score.add_score(levelOfDifficulty)
            print(f"\nYou have won the game! 🎉🎉🎉")
        else:
            print(f"\nYou have lost the game! 😭😭")
    else:
        gameResult = CurrencyRouletteGame.play(levelOfDifficulty)
        if gameResult == True:
            Score.add_score(levelOfDifficulty)
            print(f"\nYou have won the game! 🎉🎉🎉")
        else:
            print(f"\nYou have lost the game! 😭😭")
