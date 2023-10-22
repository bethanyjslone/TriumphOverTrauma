from flask import Flask, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash
import pandas as pd
import numpy as np
import sqlite3
import os

app = Flask(__name__)
EXCEL_DATA = "excel_data.xlsx"
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/results")
def results():
    return render_template("results.html")


@app.route("/resources")
def resources():
    return render_template("resources.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    # elif request.method == "POST":
    #     email = request.form["email"]
    #     password = request.form["password"]

    #     if not email:
    #         error = "- Please Enter an Email -"
    #         return render_template("register.html", error=error)

    #     elif not password:
    #         error = "- Please Enter a Password -"
    #         return render_template("register.html", error=error)

    #     connection = sqlite3.connect(CURRENT_DIRECTORY + "\TriumphOverTrauma-logs.db")
    #     cursor = connection.cursor()
    #     hashed_password = generate_password_hash(password)
    #     query = "INSERT INTO User (Email, Password) VALUES ('{e}', {p})".format(
    #         e=email, p=hashed_password
    #     )
    #     cursor.execute(query)
    #     connection.commit()


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        ...


@app.route("/logger", methods=["GET", "POST"])
def logger():
    if request.method == "GET":
        return render_template("results.html")

    elif request.method == "POST":
        if not request.form["heartrate"]:
            return render_template("results.html")
        heartrate = int(request.form["heartrate"])
        if heartrate > 100:
            video = "https://youtu.be/Vdce8ulDKFs?feature=shared"
            image = "../static/Sleep-Infographic.png"
        elif heartrate > 70:
            video = "https://youtu.be/lkORzatrCqY?feature=shared"
            image = "../static/Anxiety-Infographic.png"
        else:
            video = "https://youtu.be/g_HFX6fRjIM?feature=shared"
            image = "../static/Anxiety-Infographic-1.png"

        return render_template("results.html", video=video, image=image)


if __name__ == "__main__":
    app.run()
