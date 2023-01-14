from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from Services.NFDiscovery.model_discovery import *
from Services.model import *

app = Flask(__name__)
api = Api(app)


        
