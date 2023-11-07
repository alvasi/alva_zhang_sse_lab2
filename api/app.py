from flask import Flask, request, session, render_template
from flask import redirect, url_for
from datetime import datetime
import random
import re
import requests


app = Flask(__name__)
app.secret_key = "some_secret_key"  # set a secret key for the session


@app.route("/")
def index():
    session["num"] = random.randint(1, 100)
    session["chances"] = 7
    result = session.pop("result", None)
    return render_template("index.html", result=result)


@app.route("/guess", methods=["GET", "POST"])
def guess_game():
    if request.method == "POST":
        guess = int(request.form.get("guess"))
    else:
        guess = int(request.args.get("guess"))

    num = session["num"]
    chances = session["chances"]

    if num is None or chances is None:
        session["num"] = random.randint(1, 100)
        session["chances"] = 7
        return redirect(url_for("index"))

    if guess == num:
        result = "Hurray! You got it in {} steps!".format(7 - chances)
        session["result"] = result
        return redirect(url_for("index"))

    elif guess < num:
        result = "Your number is less than the random number"
    else:
        result = "Your number is greater than the random number"

    chances -= 1
    session["chances"] = chances

    if chances == 0:
        result = "Phew! You lost the game. You are out of chances"
        session["result"] = result
        return redirect(url_for("index"))

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.template_folder = "templates"
    app.run()


@app.route("/")
def hello_world():
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
    result = process_query(query_param)
    return result


def process_query(q):
    if q == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif q == "asteroids":
        return "Unknown"
    elif q == "What is your name?":
        return "AZ"
    elif "plus" in q:
        return add(q)
    elif "minus" in q:
        return minus(q)
    elif "Which of the following numbers is the largest: " in q:
        return find_largest_number(q)
    elif "multiplied by " in q:
        return multiply(q)
    elif "Which of the following numbers is both a square and a cube: " in q:
        return find_square_and_cube_numbers(q)
    else:
        return "Unknown"


def add(text):
    numbers = re.findall(r"\d+", text)

    if len(numbers) == 2:
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        return str(num1 + num2)
    else:
        return "Invalid Numbers"


def minus(text):
    numbers = re.findall(r"\d+", text)

    if len(numbers) == 2:
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        return str(num1 - num2)
    else:
        return "Invalid Numbers"


def find_largest_number(question):
    if "Which of the following numbers is the largest: " in question:
        numbers_str = question.split(": ")[1]
        numbers = numbers_str.split(",")
        numbers = [int(num.strip("?").strip()) for num in numbers]
        return str(max(numbers))
    return None


def multiply(text):
    # Use regular expressions to find the two integers in the sentence.
    numbers = re.findall(r"\d+", text)

    if len(numbers) == 2:
        # Convert the found numbers to integers and calculate their product.
        number1 = int(numbers[0])
        number2 = int(numbers[1])
        product = number1 * number2
        return str(product)
    else:
        # Handle the case where two numbers are not found in the input.
        return "Unable to extract and multiply the numbers."


def find_square_and_cube_numbers(text):
    # Use regular expressions to find integers in the sentence.
    numbers = re.findall(r"\d+", text)
    square_and_cube_numbers = []

    for number_str in numbers:
        number = int(number_str)
        if is_square_and_cube(number):
            square_and_cube_numbers.append(number)

    return sorted(square_and_cube_numbers)


def is_square_and_cube(number):
    # Check if a number is both a square and a cube.
    square_root = number**0.5
    cube_root = number ** (1 / 3)
    return square_root.is_integer() and cube_root.is_integer()


@app.template_filter("datetimeformat")
def datetimeformat(value, format="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").strftime(format)


@app.route("/gitquery", methods=["GET"])
def gitquery():
    input_username = request.args.get("gitquery")
    user_response = requests.get(
        f"https://api.github.com/users/{input_username}"
    )
    repos_response = requests.get(
        f"https://api.github.com/users/{input_username}/repos"
    )
    followers_response = requests.get(
        f"https://api.github.com/users/{input_username}/followers"
    )
    following_response = requests.get(
        f"https://api.github.com/users/{input_username}/following"
    )
    if (
        user_response.status_code == 200
        and repos_response.status_code == 200
        and followers_response.status_code == 200
        and following_response.status_code == 200
    ):
        user_data = user_response.json()
        repos = repos_response.json()
        followers = followers_response.json()
        following = following_response.json()

        language_distribution = {}
        for repo in repos:
            commit_response = requests.get(
                f"https://api.github.com/repos/{repo['full_name']}/commits"
            )
            languages_response = requests.get(
                f"https://api.github.com/repos/{repo['full_name']}/languages"
            )
            if commit_response.status_code == 200:
                commits = commit_response.json()[:1]
                repo["latest_commits"] = commits
                for commit in commits:
                    commit["commit"]["author"]["date"] = (
                        commit["commit"]["author"]["date"]
                    )
            if languages_response.status_code == 200:
                repo['language_distribution'] = languages_response.json()
                lang_dist_items = repo['language_distribution'].items()
                for language, bytes_ in lang_dist_items:
                    if language not in language_distribution:
                        language_distribution[language] = 0
                    language_distribution[language] += bytes_

        return render_template(
            "gitquery.html",
            gitquery=input_username,
            user=user_data,
            repos=repos,
            followers=followers,
            following=following,
            language_distribution=language_distribution,
        )
    else:
        print(f"User response status: {user_response.status_code},
              response: {user_response.text}")
        print(f"Repos response status: {repos_response.status_code},
              response: {repos_response.text}")
        print(f"Followers response status: {followers_response.status_code},
              response: {followers_response.text}")
        print(f"Following response status: {following_response.status_code},
              response: {following_response.text}")
        return render_template("error.html")
