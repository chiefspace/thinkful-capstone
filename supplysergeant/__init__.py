import os
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "supplysergeant.config.DevelopmentConfig")
app.config.from_object(config_path)

from supplysergeant import views
from supplysergeant import forms
from .util import validators