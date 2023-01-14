from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource
from Services import *
from Services.NFDiscovery.discovery import *
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

# swagger
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

# add route example
@app.route("/")
def index():
    # return "hello master"
    return render_template('index.html')

# add api example
def checkPost(postedData, funcName):
    if funcName in ["add", "sub"]:
        if "x" not in postedData or "y" not in postedData:
            return 301
        return 200
    
class Tinh_tong_2_so(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPost(postedData, "add")
        if status_code == 301:
            return jsonify({
                "message": "ERROR",
                'status code': status_code
            })
        x = int(postedData["x"])
        y = int(postedData["y"])
        result = {
            'message': x + y,
            'status code': status_code
        }
        return jsonify(result)

api.add_resource(Tinh_tong_2_so, "/sum")

if __name__ == "__main__":
    app.run()