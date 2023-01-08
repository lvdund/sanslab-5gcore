from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from Services import *
from Services.NFDiscovery.discovery import *

app = Flask(__name__)
api = Api(app)

class ALL(Resource):
    def post(self):        
        return 'true'

# api.resource(Discovery, "/discovery")
api.resource(ALL, "/all")

if __name__ == "__main__":
    app.run()