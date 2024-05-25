import os
# I found on the network that you can call the "os" to clear the screen

SCORE_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = 1


def screen_cleaner():
    os.system('cls')
