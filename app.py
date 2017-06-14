"""  Packages always start with a lower case letter  """
"""  Classes always start with a capital letter  """
from flask import Flask
from os import environ


"""  Give the app a name  """
app = Flask(__name__)

"""  Tell the app what requests its going to understand  """
@app.route('/')
def home():
    return "Hello, World!"

app.run(host=environ['IP'], port=int(environ['PORT']))