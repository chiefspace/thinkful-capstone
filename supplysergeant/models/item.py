from supplysergeant.db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    assignee = db.Column(db.String(80))
    cost = db.Column(db.Float(precision=2))
    
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventories.id'))
    inventory = db.relationship('InventoryModel')
    
    def __init__(self, name, assignee, cost, inventory_id):
        self.name = name
        self.assignee = assignee
        self.cost = cost
        self.inventory_id = inventory_id
        
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
            
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()