from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os, datetime
from . import db
from .models import db_coopersrock


views = Blueprint('views', __name__)

UPLOAD = 'C:\\Users\\lucas\\.Coding\\..CAC-2022\\CAC-2022\\website\\UPLOAD_FOLDER'


@views.route("/")
def Home():
     return render_template("Home.html")


@views.route("/about")
def about():
     return "<h1>About<h1>"


@views.route("/coopers_rock", methods=['GET', 'POST'])
def CoopersRock():
     if request.method == 'POST':
          Description = request.form.get('Description')
          Date = request.form.get('Date')
          Location = request.form.get('Location')

          Image = request.files['Image']
          print(datetime.datetime.now())
          newName = Image.filename.split('.')
          newName[0] = str(datetime.datetime.now())
          Path = newName[0] + '.' + newName[1]
          Path = os.path.join(UPLOAD, secure_filename(Path))
          Image.save(Path)

          new_image = db_coopersrock(date=Date, location=Location, description=Description, id=Path)
          db.session.add(new_image)
          db.session.commit()

     return render_template("CoopersRock.html")
