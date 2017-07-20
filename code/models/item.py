import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    assignee = db.Column(db.String(80))
    cost = db.Column(db.Float(precision=2))
    
    def __init__(self, name, assignee, cost):
        self.name = name
        self.assignee = assignee
        self.cost = cost
        
    def json(self):
        return {'name': self.name, 'assignee': self.assignee, 'cost': self.cost}
        
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row)
            
    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "INSERT INTO items VALUES (?, ?, ?)"
        cursor.execute(query, (self.name, self.assignee, self.cost))
        
        connection.commit()
        connection.close()
        
    def update(self):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "UPDATE items SET assignee=? WHERE name=?"
        changed_item = cursor.execute(query, (self.assignee, self.name))
        
        connection.commit()
        connection.close()
        
        return changed_item