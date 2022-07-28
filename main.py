from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
     return render_template("testing.html")


@app.route("/about")
def about():
     return "<h1>About<h1>"


@app.route("/CoopersRock")
def CoopersRock():
     return render_template("CoopersRock.html")


if __name__ == "__main__":
     app.run(host="127.0.0.1", port=8080,debug=True)