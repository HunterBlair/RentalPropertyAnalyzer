from flask import Flask, render_template, request, redirect
from Models.Users import *
from anaylzer_class import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rentalyzer.db'
# initialize database
db = SQLAlchemy(app)


# Model for Users

db.create_all()
db.session.commit()


@app.route("/")
def home():
    # re route a get started button that takes to login or create an account page
    return render_template("homepage.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        first_name = request.form.get("fname")
        password = request.form.get("password")
        user = Users(name=first_name, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect("/rentalyzer")
    # after login or sign up. re route to the actual anaylzer.
    return render_template("login.html")


@app.route("/rentalyzer", methods=["POST", "GET"])
def main_tool():

    if request.method == "POST":

        new_analyzer = Analyzer()
    return render_template("anaylzerform.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
