from flask import Flask, request, session, render_template
from flask import redirect, url_for
import random


app = Flask(__name__)
app.secret_key = 'some_secret_key'  # set a secret key for the session


@app.route('/')
def index():
    session['num'] = random.randint(1, 100)
    session['chances'] = 7
    result = session.pop('result', None)
    return render_template('index.html', result=result)


@app.route('/guess', methods=['GET', 'POST'])
def guess_game():
    if request.method == 'POST':
        guess = int(request.form.get('guess'))
    else:
        guess = int(request.args.get('guess'))

    num = session['num']
    chances = session['chances']

    if num is None or chances is None:
        session['num'] = random.randint(1, 100)
        session['chances'] = 7
        return redirect(url_for('index'))

    if guess == num:
        result = 'Hurray! You got it in {} steps!'.format(7 - chances)
        session['result'] = result
        return redirect(url_for('index'))

    elif guess < num:
        result = 'Your number is less than the random number'
    else:
        result = 'Your number is greater than the random number'

    chances -= 1
    session['chances'] = chances

    if chances == 0:
        result = 'Phew! You lost the game. You are out of chances'
        session['result'] = result
        return redirect(url_for('index'))

    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.template_folder = 'templates'
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
