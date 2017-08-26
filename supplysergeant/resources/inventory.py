from flask_restful import Resource
from supplysergeant.models.inventory import InventoryModel

class Inventory(Resource):
    def get(self, name):
        inventory = InventoryModel.find_by_name(name)
        if inventory:
            return inventory.json()
        return {'message': 'Inventory not found.'}, 404
    
    def post(self, name):
        if InventoryModel.find_by_name(name):
            return {'message': "An inventory with name '{}' already exists!".format(name)}, 400
            
        inventory = InventoryModel(name)
        try:
            inventory.save_to_db()
        except:
            return {'message': 'An error occured while creating the inventory.'}, 500
            
        return inventory.json(), 201
    
    def delete(self, name):
        inventory = InventoryModel.find_by_name(name)
        if inventory:
            inventory.delete_from_db()
        
        return {'message': 'Inventory deleted.'}
            
    
    
class InventoryList(Resource):
    def get(self):
        return {'inventories': [inventory.json() for inventory in InventoryModel.query.all()]}
#       return {'inventories': list(map(lambda x: x.json(), InventoryModel.query.all()))