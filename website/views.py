from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os, datetime
from . import db
from .models import db_coopersrock, db_greenbrier, db_cabwaylingo, db_calvinPrice
from .models import db_campCreek, db_kanawha, db_kumbrabow, db_panther, db_seneca

views = Blueprint('views', __name__)

UPLOAD = "C://..Coding//.CAC-2022//CAC-2022//website//static//UPLOAD_FOLDER"
# Pages that aren't for a state forest

@views.route("/")
def Home():
     return render_template("Info.html")

@views.route("/my_uploads", methods=['GET', 'POST'])
def Uploads():
     return render_template('MyUploads.html', user=current_user)

@views.route("/state_view")
def StateView():
     return render_template('wvState.html')

@views.route("/")
def Info():
     return "<h3>Change</h3>"

# All of the state park pages

def getImage():
     Description = request.form.get('Description')
     Date = datetime.date.today()
     date = Date.strftime("%m/%d/%y")

     Location = request.form.get('Location')
     IsCaution = request.form.get('Is_Caution')
     IsStar = request.form.get('Is_Star')

     if(IsCaution == "on"):
          IsCaution = True
     else:
          IsCaution = False
     if(IsStar == "on"):
          IsStar = True
     else:
          IsStar = False

     Image = request.files['Image']
     newName = Image.filename.split('.')
     newName[0] = str(datetime.datetime.now())
     Path = newName[0] + '.' + newName[1]

     Path = os.path.join(UPLOAD, secure_filename(Path))
     Image.save(Path)

     return [(newName[0] + '.' + newName[1]), date, Location, Description, IsCaution, IsStar]




@views.route("/coopers_rock", methods=['GET', 'POST'])
def CoopersRock():
     if request.method == 'POST':
          # All data sent from form put into a list
          data = getImage()

          new_image = db_coopersrock(user_id=current_user.id, id=data[0], date=data[1], location=data[2], description=data[3], is_caution=data[4], is_star=data[5])
          db.session.add(new_image)
          db.session.commit()

     # Gets the data from the database to the map
     Images = db_coopersrock.query.all()

     # Sorts the data in a list of lists
     listOfMarkers = []
     for i in range(len(Images)):
          newMarker = []
          newMarker.append(Images[i].id)
          newMarker.append(Images[i].date)
          newMarker.append(Images[i].location)
          newMarker.append(Images[i].description)
          newMarker.append(Images[i].is_caution)
          newMarker.append(Images[i].is_star)
          listOfMarkers.append(newMarker)

          
     return render_template("CoopersRock.html", title="Coopers Rock", markers=listOfMarkers, latitude=39.64390129350228, longitude=-79.81014851593424)

@views.route('/greenbrier', methods=['GET', 'POST'])
def Greenbrier():
     if request.method == 'POST':
          # All data sent from form put into a list
          data = getImage()

          new_image = db_greenbrier(user_id=current_user.id, id=data[0], date=data[1], location=data[2], description=data[3], is_caution=data[4], is_star=data[5])
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

@views.route('/cabwaylingo', methods=['GET', 'POST'])
def Cabwaylingo():
     if request.method == 'POST':
          # All data sent from form put into a list
          data = getImage()

          new_image = db_cabwaylingo(user_id=current_user.id, id=data[0], date=data[1], location=data[2], description=data[3], is_caution=data[4], is_star=data[5])
          db.session.add(new_image)
          db.session.commit()
          
     # Gets the data from the database to the map
     Images = db_cabwaylingo.query.all()

     listOfMarkers = []
     for i in range(len(Images)):
          newMarker = []
          newMarker.append(Images[i].id)
          newMarker.append(Images[i].date)
          newMarker.append(Images[i].location)
          newMarker.append(Images[i].description)
          listOfMarkers.append(newMarker)
         
     return render_template("Cabwaylingo.html", title="Cabwaylingo", markers=listOfMarkers, latitude=37.98630939830299, longitude=-82.37419391981442)

@views.route('/kanawha', methods=['GET', 'POST'])
def Kanawha():
     if request.method == 'POST':
          # All data sent from form put into a list
          data = getImage()

          new_image = db_kanawha(user_id=current_user.id, id=data[0], date=data[1], location=data[2], description=data[3], is_caution=data[4], is_star=data[5])
          db.session.add(new_image)
          db.session.commit()
          
     # Gets the data from the database to the map
     Images = db_kanawha.query.all()

     listOfMarkers = []
     for i in range(len(Images)):
          newMarker = []
          newMarker.append(Images[i].id)
          newMarker.append(Images[i].date)
          newMarker.append(Images[i].location)
          newMarker.append(Images[i].description)
          listOfMarkers.append(newMarker)
         
     return render_template("Kanawha.html", title="Kanawha", markers=listOfMarkers, latitude=38.252479258812265, longitude=-81.6561347664939)

@views.route('/calvin_price', methods=['GET', 'POST'])
def CalvinPrice():
     if request.method == 'POST':
          # All data sent from form put into a list
          data = getImage()

          new_image = db_calvinPrice(user_id=current_user.id, id=data[0], date=data[1], location=data[2], description=data[3], is_caution=data[4], is_star=data[5])
          db.session.add(new_image)
          db.session.commit()

     # Gets the data from the database to the map
     Images = db_calvinPrice.query.all()

     listOfMarkers = []
     for i in range(len(Images)):
          newMarker = []
          newMarker.append(Images[i].id)
          newMarker.append(Images[i].date)
          newMarker.append(Images[i].location)
          newMarker.append(Images[i].description)
          listOfMarkers.append(newMarker)
         
     return render_template("CalvinPrice.html", title="Calvin Price", markers=listOfMarkers, latitude=38.07869624412231, longitude=-80.13671646525201)

@views.route('/camp_creek', methods=['GET', 'POST'])
def CampCreek():
     if request.method == 'POST':
          # All data sent from form put into a list
          data = getImage()

          new_image = db_campCreek(user_id=current_user.id, id=data[0], date=data[1], location=data[2], description=data[3], is_caution=data[4], is_star=data[5])
          db.session.add(new_image)
          db.session.commit()
          

     # Gets the data from the database to the map
     Images = db_campCreek.query.all()

     listOfMarkers = []
     for i in range(len(Images)):
          newMarker = []
          newMarker.append(Images[i].id)
          newMarker.append(Images[i].date)
          newMarker.append(Images[i].location)
          newMarker.append(Images[i].description)
          listOfMarkers.append(newMarker)
         
     return render_template("CampCreek.html", title="Camp Creek", markers=listOfMarkers, latitude=37.52329454326871, longitude=-81.1494609861773)

@views.route('/panther', methods=['GET', 'POST'])
def Panther():
     if request.method == 'POST':
          # All data sent from form put into a list
          data = getImage()

          new_image = db_panther(user_id=current_user.id, id=data[0], date=data[1], location=data[2], description=data[3], is_caution=data[4], is_star=data[5])
          db.session.add(new_image)
          db.session.commit()

     # Gets the data from the database to the map
     Images = db_panther.query.all()

     listOfMarkers = []
     for i in range(len(Images)):
          newMarker = []
          newMarker.append(Images[i].id)
          newMarker.append(Images[i].date)
          newMarker.append(Images[i].location)
          newMarker.append(Images[i].description)
          listOfMarkers.append(newMarker)
         
     return render_template("Panther.html", title="Panther", markers=listOfMarkers, latitude=37.42031776693124, longitude=-81.8827314691821)

@views.route('/seneca', methods=['GET', 'POST'])
def Seneca():
     if request.method == 'POST':
          # All data sent from form put into a list
          data = getImage()

          new_image = db_seneca(user_id=current_user.id, id=data[0], date=data[1], location=data[2], description=data[3], is_caution=data[4], is_star=data[5])
          db.session.add(new_image)
          db.session.commit()

     # Gets the data from the database to the map
     Images = db_seneca.query.all()

     listOfMarkers = []
     for i in range(len(Images)):
          newMarker = []
          newMarker.append(Images[i].id)
          newMarker.append(Images[i].date)
          newMarker.append(Images[i].location)
          newMarker.append(Images[i].description)
          listOfMarkers.append(newMarker)
         
     return render_template("Seneca.html", title="Seneca", markers=listOfMarkers, latitude=38.2846340833706, longitude=-79.99551912339467)

@views.route('/kumbrabow', methods=['GET', 'POST'])
def Kumbrabow():
     if request.method == 'POST':
          # All data sent from form put into a list
          data = getImage()

          new_image = db_kumbrabow(user_id=current_user.id, id=data[0], date=data[1], location=data[2], description=data[3], is_caution=data[4], is_star=data[5])
          db.session.add(new_image)
          db.session.commit()
          

     # Gets the data from the database to the map
     Images = db_kumbrabow.query.all()

     listOfMarkers = []
     for i in range(len(Images)):
          newMarker = []
          newMarker.append(Images[i].id)
          newMarker.append(Images[i].date)
          newMarker.append(Images[i].location)
          newMarker.append(Images[i].description)
          listOfMarkers.append(newMarker)
     
     listOfMarkers = listOfMarkers.reverse()

     return render_template("Kumbrabow.html", title="Kumbrabow", markers=listOfMarkers, latitude=38.636832286036324, longitude=-80.09305460855343)
