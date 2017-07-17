import sqlite3

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
            user = cls(row[0], row[1], row[2])
        else:
            User = None
            
        connection.close()  # No need to commit because no data added
        return user
        
        