from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'secret'

""" The Api works with Resources and every resource has to be a Class """
api = Api(app) # instantiate an instance of the Api Class

""" Create an instance of the JWT Class using the app object and the ... """
""" ... authenticate and identity methods from security.py """
jwt = JWT(app, authenticate, identity)  # /auth endpoint

""" The items list below will serve as an in memroy database  """
""" The items list will contain a list of item dictionaries """
items = []


""" The class below creates a Resource Class called Item  """
""" The Item Resource Class will be used to instantiate item objects """
""" The item object will inherit properties from the Resource Class """
class Item(Resource):
    """ get method for retrieving an item Resource object by name """
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404
        
    """ post method for storing an item Resource object by name """
    """ The cost value is temporarily hard coded to $1.299.00 for now """
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        
        
        data = request.get_json()
        item = {'name': name, 'cost': data['cost']}
        items.append(item)
        return item, 201
        
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

class ItemList(Resource):
    def get(self):
        return {'items': items}, 200
        
""" The api object method below defines the endpoint for the GET item by name Resource """
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

""" The app.run method below starts the Flask app and binds it to port 5000 """
app.run(host='0.0.0.0', port=8080, debug=True)