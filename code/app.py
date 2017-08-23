from flask import Flask, request, render_template, redirect, url_for
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.inventory import Inventory, InventoryList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # turns off Flask's SQLAlchemy mod tracker
app.secret_key = 'secret'

""" The Api works with Resources and every resource has to be a Class """
api = Api(app) # instantiate an instance of the Api Class

@app.before_first_request
def create_tables():
    db.create_all()

""" 
Create an instance of the JWT Class using the app object and the
authenticate and identity methods from security.py 
"""
jwt = JWT(app, authenticate, identity)  # /auth endpoint

        
""" 
The api object methods below define the endpoints ... 
for the GET methods by name Resource
"""
api.add_resource(Inventory, '/inventory/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(InventoryList, '/inventories')
api.add_resource(UserRegister, '/register')


"""
The @app decorated methods below define the endpoints for ... 
the front end of the app 
"""
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
    
# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

    
@app.route('/registration')
def register_template():
    return render_template('register.html')


""" The app.run method below starts the Flask app and binds it to port 5000 """
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=8080, debug=True)