import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask import request
import time
from datetime import date


""" 
The class below creates a Resource Class called Item
The Item Resource Class will be used to instantiate item objects
The item object will inherit properties from the Resource Class 
"""
class Item(Resource):
    """ get method for retrieving an item Resource object by name """
    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        
        if row:
            return {'item': 
                {
                    'name': row[0],
                    'cost': row[1],
                    'assignee': row[2],
                    'date_assigned': row[3],
                    'previous_assignees': row[4]
                }
            }
        return {"message": "Item not found"}, 404

        
    """
    post method for storing an item Resource object by name
    The cost value is temporarily hard coded to $1.299.00 for now
    """
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