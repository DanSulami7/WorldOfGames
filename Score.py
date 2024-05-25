

def add_score(levelOfDifficulty):
    print(f'The level of difficulty is: {levelOfDifficulty}')
    int_POINTS_OF_WINNING = ((levelOfDifficulty*3)+5)
    str_POINTS_OF_WINNING = str(int_POINTS_OF_WINNING)
    print(f'The point of this win equal to: {str_POINTS_OF_WINNING})')

    try:
        f = open("Scores.txt", "r")
        lastScore = f.read()
        int_lastScore = int(lastScore)
        print(f'The old score was: {lastScore}')
        f.close()

        int_totalScore = int_lastScore + int_POINTS_OF_WINNING
        print(int_totalScore)

        f = open("Scores.txt", "w")
        str_totalScore = str(int_totalScore)
        f.write(str_totalScore)
        f.close()

    except:
        print("the file you want to read does not exist. it will be create now")
        f = open("Scores.txt", "a")
        f.write(str_POINTS_OF_WINNING)
        print(f'The total sum in the file is: {str_POINTS_OF_WINNING}')
        f.close()
