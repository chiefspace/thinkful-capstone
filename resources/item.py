import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import time
from datetime import date


""" 
The class below creates a Resource Class called Item
The Item Resource Class will be used to instantiate item objects
The item object will inherit properties from the Resource Class 
"""
class Item(Resource):
    TABLE_NAME = 'items'

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
    
    """ get method for retrieving an item Resource object by name """
    @jwt_required()
    def get(self, name):
	    item = Item.find_by_name(name)
	    if item:
	        return item
	    return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'assignee': row[1], 'cost': row[2]}}

        
    """
    post method for storing an item Resource object by name
    The cost value is temporarily hard coded to $1.299.99 for now
    """
    def post(self, name):
        if Item.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        
        data = Item.parser.parse_args()
        item = {'name': name, 'assignee': data['assignee'], 'cost': data['cost']}

        try:
            Item.insert(item)
        except:
            return {"message": "An error occurred while inserting an item."}, 500

        return item, 201
        
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "INSERT INTO items VALUES (?, ?, ?)"
        cursor.execute(query, (item['name'], item['assignee'], item['cost']))
        
        connection.commit()
        connection.close()
        
    def delete(self, name):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))
        
        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}
        
    def put(self, name):
        data = Item.parser.parse_args()
        item = Item.find_by_name(name)
        updated_item = {'name': name, 'assignee': data['assignee'], 'cost': item['cost']}
        if item is None:
            try:
                Item.insert(updated_item)
            except:
                return {"message": "An error occurred inserting the item."}
        else:
            try:
                Item.update(updated_item)
            except:
                return {"message": "An error occurred updating the item."}
        return updated_item

        
    
    @classmethod
    def update(cls, item):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "UPDATE items SET assignee=? WHERE name=?"
        changed_item = cursor.execute(query, (item['assignee'], item['name']))
        
        connection.commit()
        connection.close()
        
        return changed_item

class ItemList(Resource):
    TABLE_NAME = 'items'

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'assignee': row[1], 'cost': row[2]})
        connection.close()

        return {'items': items}