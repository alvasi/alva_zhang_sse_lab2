from flask import Flask, request, session
import random


app = Flask(_name_)
app.secret_key = 'some_secret_key'  # set a secret key for the session


@app.route('/guess', methods=['GET'])
def guess_game():
    if 'num' not in session:
        session['num'] = random.randint(1, 100)
    if 'chances' not in session:
        session['chances'] = 7


    guess = request.args.get('guess', type=int)
    if guess == session['num']:
        result = 'Hurray! You got it in {} steps!'.format(7 - session['chances'])
        session.pop('num', None)  # remove the number from the session
        session.pop('chances', None)  # remove the chances from the session
    elif guess < session['num']:
        result = 'Your number is less than the random number'
        session['chances'] -= 1  # decrease the chances
    elif guess > session['num']:
        result = 'Your number is greater than the random number'
        session['chances'] -= 1  # decrease the chances
    if session['chances'] == 0:
        result = 'Phew! You lost the game. You are out of chances'
        session.pop('num', None)  # remove the number from the session
        session.pop('chances', None)  # remove the chances from the session

    return result

if _name_ == '_main_':
    app.run()


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
