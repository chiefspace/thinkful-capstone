from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

""" The Api works with Resources and every resource has to be a Class """
api = Api(app) # instantiate an instance of the Api Class

""" The items list below will serve as an in memroy database  """
""" The items list will contain a list of item dictionaries """
items = []


""" The class below creates a Resource Class called Item  """
""" The Item Resource Class will be used to instantiate item objects """
""" The item object will inherit properties from the Resource Class """
class Item(Resource):
    def get(self, name):
        return {'item': name}
        
""" The api object below defines the endpoint for the GET item by name Resource """
api.add_resource(Item, '/item/<string:name>')        

""" The app.run method below starts the Flask app and binds it to port 5000 """
app.run(port=5000)