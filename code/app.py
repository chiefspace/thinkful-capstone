from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
import time
from datetime import date

from security import authenticate, identity
from user import UserRegister

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
        item = {
            'name': name,
            'cost': data['cost'],
            'assignee': data['assignee'],
            'date_assigned': str(date.today()),
            'previous_assignees': [(data['assignee'],str(date.today())),]
        }
        items.append(item)
        return item, 201
        
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}
        
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('assignee',
            type=str,
            required=True,
            help="This field cannot be blank!"
        )
        data = parser.parse_args()
        
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'assignee': data['assignee']}
            items.append(item)
        elif data['assignee'] != item['assignee']:
            item.update(data)
            item['previous_assignees'].append((item['assignee'],item['date_assigned']),)
            item['date_assigned'] = str(date.today())
        else:
            return {'message': 'New assignee cannot be equal to previous assignee'}
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}, 200
        
""" The api object method below defines the endpoint for the GET item by name Resource """
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

""" The app.run method below starts the Flask app and binds it to port 5000 """
app.run(host='0.0.0.0', port=8080, debug=True)