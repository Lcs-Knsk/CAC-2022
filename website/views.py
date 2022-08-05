from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os, datetime
from . import db
from .models import db_coopersrock, db_greenbrier
import mysql.connector


views = Blueprint('views', __name__)

UPLOAD = 'C:\\Users\\lucas\\.Coding\\..CAC-2022\\CAC-2022\\website\\static\\UPLOAD_FOLDER'


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
          Date = datetime.date.today()
          date = Date.strftime("%m/%d/%y")

          Location = request.form.get('Location')

          Image = request.files['Image']
          newName = Image.filename.split('.')
          newName[0] = str(datetime.datetime.now())
          Path = newName[0] + '.' + newName[1]
          Path = os.path.join(UPLOAD, secure_filename(Path))
          Image.save(Path)

          new_image = db_coopersrock(date=date, location=Location, description=Description, id=(newName[0] + '.' + newName[1]))
          db.session.add(new_image)
          db.session.commit()

     # Gets the data from the database to the map
     Images = db_coopersrock.query.all()

     listOfMarkers = []
     for i in range(len(Images)):
          newMarker = []
          newMarker.append(Images[i].id)
          newMarker.append(Images[i].date)
          newMarker.append(Images[i].location)
          newMarker.append(Images[i].description)
          listOfMarkers.append(newMarker)
          
     return render_template("CoopersRock.html", title="Coopers Rock", markers=listOfMarkers, latitude=39.64390129350228, longitude=-79.81014851593424)

@views.route('/greenbrier', methods=['GET', 'POST'])
def Greenbrier():
     if request.method == 'POST':
          Description = request.form.get('Description')
          Date = datetime.date.today()
          date = Date.strftime("%m/%d/%y")

          Location = request.form.get('Location')

          Image = request.files['Image']
          newName = Image.filename.split('.')
          newName[0] = str(datetime.datetime.now())
          Path = newName[0] + '.' + newName[1]
          Path = os.path.join(UPLOAD, secure_filename(Path))
          Image.save(Path)

          new_image = db_greenbrier(date=date, location=Location, description=Description, id=(newName[0] + '.' + newName[1]))
          db.session.add(new_image)
          db.session.commit()

     # Gets the data from the database to the map
     Images = db_greenbrier.query.all()

     listOfMarkers = []
     for i in range(len(Images)):
          newMarker = []
          newMarker.append(Images[i].id)
          newMarker.append(Images[i].date)
          newMarker.append(Images[i].location)
          newMarker.append(Images[i].description)
          listOfMarkers.append(newMarker)
         
     return render_template("Greenbrier.html", title="Greenbrier", markers=listOfMarkers, latitude=37.73212355678927, longitude=-80.35293828677094)
