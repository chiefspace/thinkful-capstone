import sqlite3
from flask_restful import Resource

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    """ Find user by username in the database """
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))  #  Single value tuple
        
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            User = None
            
        connection.close()  # No need to commit because no data added
        return user
        
    """ Find user by id in the database """
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))  #  Single value tuple
        
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            User = None
            
        connection.close()  # No need to commit because no data added
        return user
        
class UserRegister(Resource):
    def post(self):
        pass