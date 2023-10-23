from flask import Flask, render_template, request

app = Flask(__name__)


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
    else:
        return "Unknown"
