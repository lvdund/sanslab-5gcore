from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from Services.NFDiscovery import *
from Services import *

app = Flask(__name__)
api = Api(app)

class Discovery(Resource):
    def get(self):
        getData = request.get_json()
        getNfProfile = schemas.NFProfile
        getNfProfile.nfType = getData["nfType"]
        
        return 'true'

