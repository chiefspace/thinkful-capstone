from flask import Flask, request, render_template
from flask_restful import Api

from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.inventory import Inventory, InventoryList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///supplysergeant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # turns off Flask's SQLAlchemy mod tracker
app.SUPPLY_SERGEANT_SECRET_KEY="your_secret_key_here"

""" The Api works with Resources and every resource has to be a Class """
api = Api(app) # instantiate an instance of the Api Class

        
""" 
The api object method below defines the endpoint ... 
for the GET item by name Resource
"""
api.add_resource(Inventory, '/inventory/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(InventoryList, '/inventories')
api.add_resource(UserRegister, '/register')


@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html")