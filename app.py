"""  Packages always start with a lower case letter  """
"""  Classes always start with a capital letter  """
from flask import Flask
from os import environ


"""  Give the app a name  """
app = Flask(__name__)

inventories = [{
    'name': 'Laptop Computers',
    'items': [{'name':'baltieri-lenovo1', 'cost': 1299.99 }]
}]

"""  Tell the app what requests its going to understand  """
# POST /inventory data: (name: )
@app.route('/inventory', methods=['POST'])
def create_inventory():
    pass

# GET /inventory/<string:name>
@app.route('/inventory/<string:name>')
def get_inventory(name):
    pass

# GET /inventory
@app.route('/inventory')
def get_inventories():
    pass

# POST /store/<string:name>/item (name:, cost: )
@app.route('/inventory/<string:name>/item', methods=['POST'])
def create_item_in_inventory(name):
    pass

# GET /inventory/<string:name>/item
@app.route('/inventory/<string:name>/item')
def get_item_in_inventory(name):
    pass

app.run(host=environ['IP'], port=int(environ['PORT']))