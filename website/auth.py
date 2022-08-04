from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route("/sign_up", methods=['GET', 'POST'])
def SignUp():
     if request.method == 'POST':

          if "signUpForm" in request.form:
               UserName = request.form.get('Username')
               password1 = request.form.get('Password')
               password2 = request.form.get('Password2')

               user = User.query.filter_by(username=UserName).first()
               if user:
                    flash('Username already exists.', category='error')
               elif len(UserName) < 4:
                    flash('First name must be greater than 3 characters.', category='error')
               elif password1 != password2:
                    flash('Passwords don\'t match.', category='error')
               elif len(password1) < 7:
                    flash('Password must be at least 7 characters.', category='error')
               else:
                    new_user = User(username=UserName, password=generate_password_hash(password1, method='sha256'))
                    db.session.add(new_user)
                    db.session.commit()
                    flash('Account created!', category='success')
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
                         flash('Incorrect password.', category='error')
               else:
                    flash('Username does not exist.', category='error')


     return render_template("SignUp.html", test="Hello Flask", testCase=True)


@auth.route('/logout')
@login_required
def logout():
     logout_user()
     return redirect(url_for('views.Home'))
