from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # turns off Flask's SQLAlchemy mod tracker
app.secret_key = 'secret'

""" The Api works with Resources and every resource has to be a Class """
api = Api(app) # instantiate an instance of the Api Class


""" 
Create an instance of the JWT Class using the app object and the ...
authenticate and identity methods from security.py 
"""
jwt = JWT(app, authenticate, identity)  # /auth endpoint

        
""" 
The api object method below defines the endpoint ... 
for the GET item by name Resource
"""
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


""" The app.run method below starts the Flask app and binds it to port 5000 """
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=8080, debug=True)