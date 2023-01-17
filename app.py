from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from pymongo import MongoClient

from Services import *
from Services.NFDiscovery.discovery import *
from Services.NFManagement.management import *

app = Flask(__name__)
api = Api(app)

connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
free5gc_db = client.free5gc

# swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint( SWAGGER_URL, API_URL, config={'app_name': 'list api'} )
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

api.add_resource(GetData, "/getdata")

if __name__ == "__main__":
    app.run()