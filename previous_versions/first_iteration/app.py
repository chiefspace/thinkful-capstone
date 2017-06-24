"""  Packages always start with a lower case letter  """
"""  Classes always start with a capital letter  """
from flask import Flask, jsonify, request
from os import environ


"""  Give the app a name  """
app = Flask(__name__)

inventories = [{
    'name': 'laptops',
    'items': [{'name':'baltieri-lenovo1', 'cost': 1299.99 }]
}]

"""  Tell the app what requests its going to understand  """
# POST /inventory data: (name: )
@app.route('/inventory', methods=['POST'])
def create_inventory():
    request_data = request.get_json()
    new_inventory = {
        'name':request_data['name'],
        'items':[]
    }
    inventories.append(new_inventory)
    return jsonify(new_inventory)

# GET /inventory/<string:name>
@app.route('/inventory/<string:name>')
def get_inventory(name):
    for inventory in inventories:
      if inventory['name'] == name:
          return jsonify(inventory)
    return jsonify ({'message': 'inventory not found'})

# GET /inventory
@app.route('/inventory')
def get_inventories():
    return jsonify({'inventories': inventories})

# POST /store/<string:name>/item (name:, cost: )
@app.route('/inventory/<string:name>/item', methods=['POST'])
def create_item_in_inventory(name):
    request_data = request.get_json()
    for inventory in inventories:
        if inventory['name'] == name:
            new_item = {
                'name': request_data['name'],
                'cost': request_data['cost']
            }
            inventory['items'].append(new_item)
            return jsonify(new_item)
    return jsonify ({'message' :'inventory not found'})

# GET /inventory/<string:name>/items
@app.route('/inventory/<string:name>/items')
def get_item_in_inventory(name):
    for inventory in inventories:
      if inventory['name'] == name:
          return jsonify( {'items':inventory['items'] } )
    return jsonify ({'message':'inventory not found'})

app.run(host=environ['IP'], port=int(environ['PORT']))