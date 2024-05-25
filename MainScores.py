from flask import Flask
from flask import render_template
# from e2e import main_function

app = Flask("game")


@app.route('/Game', methods=['GET'])
def score_server():
    try:
        f = open("Scores.txt", "r")
        lastScore = f.read()
        f.close()
        print(f'the score is: {lastScore}')
        return render_template('success.html', SCORE=lastScore)

    except FileNotFoundError as ve:
        return render_template('error.html', ERROR=ve)


app.run(host="0.0.0.0", port=5001, debug=True)

# main_function()
