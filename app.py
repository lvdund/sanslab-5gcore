from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from Services import *
from Services.NFDiscovery.discovery import *
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'list api'
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

api.add_resource(Discovery, "/discovery")

if __name__ == "__main__":
    app.run()