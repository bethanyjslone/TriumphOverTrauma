from flask import Flask, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash
import pandas as pd
import numpy as np

app = Flask(__name__)
EXCEL_DATA = "excel_data.xlsx"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results")
def results():
    return render_template("results.html")


@app.route("/resources")
def resources():
    return render_template("resources.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if not email:
            error = "- Please Enter an Email -"
            return render_template("register.html", error=error)

        elif not password:
            error = "- Please Enter a Password -"
            return render_template("register.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        ...


@app.route("/logger", methods=["GET"])
def logger():
    if request.method == "GET":
        df = pd.read_excel(
            io=EXCEL_DATA,
            sheet_name="Data In",
            usecols=[1],
            skiprows=lambda x: x not in range(8, 52),
            keep_default_na=False,
        )
        values = df.values
        data = list(values)
        new_data = []
        for i in range(len(data)):
            new_data.append(int(data[i][0]))
            print(type(data[i][0]))
        return render_template("results.html", data=new_data)


if __name__ == "__main__":
    app.run()
