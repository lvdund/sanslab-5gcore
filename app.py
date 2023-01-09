from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from Services import *
from Services.NFDiscovery.discovery import *

app = Flask(__name__)
api = Api(app)

# class All(Resource):
#     def post(self):
#         postData = request.get_json()
#         return postData
    

api.add_resource(Discovery, "/discovery")
# api.add_resource(All, "/all")

if __name__ == "__main__":
    app.run()