from msilib.schema import Error
from flask import Flask, render_template, Blueprint, request, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route("/sign_up", methods=['GET', 'POST'])
def SignUp():
     # Will tell user if there was an error getting into the account
     ErrorMessage = ""
     # Tells if user left off on sign in or sign up, False=Login True=Sign Up
     SaveState = False
     
     if request.method == 'POST':

          if "signUpForm" in request.form:
               SaveState = True
               UserName = request.form.get('Username')
               password1 = request.form.get('Password')
               password2 = request.form.get('Password2')

               user = User.query.filter_by(username=UserName).first()
               if user:
                    ErrorMessage="Username already exists."
               elif len(UserName) < 4:
                    ErrorMessage = "Username must be at least 4 characters."
               elif password1 != password2:
                    ErrorMessage = "Passwords do not match."
               elif len(password1) < 5:
                    ErrorMessage = "Password must be at least 5 characters."
               else:
                    new_user = User(username=UserName, password=generate_password_hash(password1, method='sha256'))
                    print("Added new user")
                    db.session.add(new_user)
                    db.session.commit()
                    login_user(new_user, remember=True)
                    return redirect(url_for('views.Home'))
         
          elif "loginForm" in request.form:
               username = request.form.get('Username')
               password = request.form.get('Password')

               user = User.query.filter_by(username=username).first()
               if user: 
                    if check_password_hash(user.password, password): 
                         login_user(user, remember=True)
                         return redirect(url_for('views.Home'))
                    else:
                         ErrorMessage = "Incorect password."
               else:
                    ErrorMessage = "Username does not exists."

     if not len(ErrorMessage) == 0:
          return render_template("SignUp.html", test="Hello Flask", testCase=True, ErrorMessage="*" + ErrorMessage, SaveState=SaveState)
     else:
          return render_template("SignUp.html", test="Hello Flask", testCase=True, SaveState=SaveState)

          


@auth.route('/logout')
def logout():
     logout_user()
     return redirect(url_for('views.Home'))
