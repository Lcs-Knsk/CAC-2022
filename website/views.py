from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route("/")
def Home():
     return render_template("testing.html")


@views.route("/about")
def about():
     return "<h1>About<h1>"


@views.route("/coopers_rock")
@login_required
def CoopersRock():
     return render_template("CoopersRock.html")
