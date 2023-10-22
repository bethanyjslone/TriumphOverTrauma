from flask import Flask, render_template, request

app = Flask(__name__)


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
