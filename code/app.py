from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

""" The Api works with Resources and every resource has to be a Class """
api = Api(app) # instantiate an instance of the Api Class