import os
from flask.ext.script import Manager

from supplysergeant import app, views

manager = Manager(app)

@manager.command
def run():
    app.run(host='0.0.0.0', port=8080)
    

if __name__ == "__main__":
    from supplysergeant.db import db
    views.init_db()
    manager.run()