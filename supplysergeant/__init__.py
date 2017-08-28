import os
from flask import Flask

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "supplysergeant.config.DevelopmentConfig")
app.config.from_object(config_path)

from . import views
from . import forms
from . import filters
from .util import validators