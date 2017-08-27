import os
from flask import Flask, request, render_template, redirect, url_for
from flask_restful import Api

from flask_login import LoginManager, login_user, login_required, logout_user

from supplysergeant.db import db
from supplysergeant.models.user import User
from supplysergeant.models.item import ItemModel
from supplysergeant.models.inventory import InventoryModel

from supplysergeant import app

from supplysergeant.forms import SignupForm, AddItemForm
import uuid


@app.before_first_request
def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()
    
login_manager = LoginManager()
login_manager.init_app(app)

        
""" 
The api object methods below define the endpoints ... 
for the GET methods by name Resource
"""


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'GET':
        return render_template('signup.html', form = form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if User.query.filter_by(email=form.email.data).first():
                return "Email address already exists" 
            else:
                newuser = User(form.email.data, form.password.data)
                db.session.add(newuser)
                db.session.commit()

                login_user(newuser)

                return "User created!!!"        
        else:
            return "Form didn't validate"
            
@login_manager.user_loader
def load_user(email):
    return User.query.filter_by(email = email).first()
    
@app.route('/protected')
@login_required
def protected():
    return "protected area"
    
@app.route('/login', methods=['GET','POST'])
def login():
    form = SignupForm()

    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            user=User.query.filter_by(email=form.email.data).first()
            if user:
                if user.password == form.password.data:
                    login_user(user)
                    return "User logged in"                
                else:
                    return "Wrong password"            
            else:
                return "user doesn't exist"        
    else:
            return "form not validated"
            
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out"
    
@app.route('/item', methods=['GET', 'POST'])
@login_required
def AddItem():
    form = AddItemForm()

    if request.method == 'GET':
        return render_template('item.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if ItemModel.query.filter_by(name=form.name.data).first():
                return "Item already exists"
            else:
                _id = str(uuid.uuid4())
                new_item = ItemModel(form.name.data, form.assignee.data, form.cost.data, _id)
                db.session.add(new_item)
                db.session.commit()

                return "New item added!!!"        
        else:
            return "Form didn't validate"
    
##############

"""
The @app decorated methods below define the endpoints for ... 
the front end of the app 
"""
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')