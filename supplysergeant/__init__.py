import os
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "supplysergeant.config.DevelopmentConfig")
app.config.from_object(config_path)

""" The Api works with Resources and every resource has to be a Class """
api = Api(app) # instantiate an instance of the Api Class

from supplysergeant import views
from supplysergeant import forms
from .util import validators