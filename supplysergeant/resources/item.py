from flask_restful import Resource, reqparse
from supplysergeant.models.item import ItemModel


""" 
The class below creates a Resource Class called Item
The Item Resource Class will be used to instantiate item objects
The item object will inherit properties from the Resource Class 
"""
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('assignee',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('cost',
        type=float,
        required=False
    )
    parser.add_argument('inventory_id',
        type=int,
        required=True,
        help="Every item needs an inventory id."
    )
    
    """ get method for retrieving an item Resource object by name """
    def get(self, name):
	    item = ItemModel.find_by_name(name)
	    if item:
	        return item.json()
	    return {'message': 'Item not found'}, 404

        
    """
    post method for storing an item Resource object by name
    The cost value is temporarily hard coded to $1.299.99 for now
    """
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        
        data = Item.parser.parse_args()
        
        item = ItemModel(name, data['assignee'], data['cost'], data['inventory_id'])
#       item = ItemModel(name, **data) 

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred while inserting an item."}, 500

        return item.json(), 201
        
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            
        return {'message': 'Item deleted'}
        
        
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['assignee'], data['cost'], data['inventory_id'])
#           item = ItemModel(name, **data)            
        else:
            item.assignee = data['assignee']
            
        item.save_to_db()
        
        return item.json()


class ItemList(Resource):
    def get(self):
        """ The use of map below is a mapping of funtions to elements """
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}