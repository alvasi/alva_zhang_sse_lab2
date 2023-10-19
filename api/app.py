from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
    
@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_fav_colour = request.form.get("colour")
    return render_template("hello.html", name=input_name, age=input_age)   