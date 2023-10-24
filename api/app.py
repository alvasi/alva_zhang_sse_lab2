from flask import Flask, render_template, request
import random

app = Flask(__name__)

secret_number = None
num_g = 7
range = 100


@app.route("/")
def hello_world():
    game_message = new_game()
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_reason = request.form.get("reason")
    return render_template(
        "hello.html", name=input_name, age=input_age, reason=input_reason
    )


@app.route("/query", methods=["GET"])
def query():
    query_param = request.args.get("q")
    result = handle_guess(query_param)
    game_message = (
        new_game() if "No remaining guesses" in result or "Correct!" in result else ""
    )
    return render_template("result.html", result=result, game_message=game_message)


def handle_guess(guess):
    global num_g
    if guess.isdigit():
        guess = int(guess)
        if guess < secret_number and num_g > 1:
            num_g -= 1
            return "Higher. Number of remaining guesses is " + str(num_g) + "."
        elif guess > secret_number and num_g > 1:
            num_g -= 1
            return "Lower. Number of remaining guesses is " + str(num_g) + "."
        elif guess == secret_number:
            new_game()
            return "Correct!"
        elif num_g <= 1:
            new_game()
            return "Unlucky! No remaining guesses."
    else:
        return "Invalid query. Please enter a number."


def new_game():
    global secret_number, num_g, range
    num_g = 7
    secret_number = random.randrange(0, range)
    return (
        "New game! Range is [0, "
        + str(range)
        + "). Number of remaining guesses is "
        + str(num_g)
        + "."
    )


new_game()
