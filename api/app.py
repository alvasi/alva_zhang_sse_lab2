from flask import Flask, render_template, request
import random

app = Flask(__name__)

secret_number = None
num_g = 7
range = 100


@app.route("/")
def hello_world():
    new_game()
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
def query(q=None):
    if q is None:
        q = request.args.get("q")
    result = handle_guess(q)
    if "No remaining guesses" in result or "Correct!" in result:
        game_message = new_game()
    else:
        game_message = ""
    template_data = {"result": result, "game_message": game_message}
    return render_template("result.html", **template_data)


def handle_guess(guess):
    global num_g
    if isinstance(guess, int):
        guess = int(guess)
        if guess > secret_number and num_g > 1:
            num_g -= 1
            return "Too high!. Number of remaining guesses is "
            + str(num_g) + "."
        elif guess < secret_number and num_g > 1:
            num_g -= 1
            return "Too low!. Number of remaining guesses is "
            + str(num_g) + "."
        elif guess == secret_number:
            game_message = new_game()
            return game_message
        elif num_g <= 1:
            game_message = new_game()
            return game_message
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
