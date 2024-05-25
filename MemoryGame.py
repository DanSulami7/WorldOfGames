import random
import time
import os


def generate_sequence(levelOfDifficulty):
    randomNumbersList = random.sample(range(1, 101), levelOfDifficulty)
    print(f"now you will see {
          levelOfDifficulty} numbers. try to remember them all!\n")
    print(randomNumbersList)
    delete_list()
    return randomNumbersList


def get_list_from_user(levelOfDifficulty):
    print(f"please enter {
          levelOfDifficulty} numbers that you remember from the list you saw before:")
    playerList = []
    for i in range(levelOfDifficulty):
        playerList.append(int(input()))
    print(f"your list is: {playerList}")
    return playerList


def is_list_equal(randomNumbersList, playerList):
    for i in range(len(randomNumbersList)):
        if randomNumbersList[i] != playerList[i]:
            return False
    return True


def delete_list():
    time.sleep(3)
    print('Deleting list...')
    os.system('cls')
    print('List deleted!')


def play(levelOfDifficulty):
    print(f"\nYou have chosen Memory Game, and level of difficulty {
          levelOfDifficulty}. you will now enter the game.\n")
    randomNumbersList = generate_sequence(levelOfDifficulty)
    playerList = get_list_from_user(levelOfDifficulty)
    answer = is_list_equal(randomNumbersList, playerList)
    return answer
