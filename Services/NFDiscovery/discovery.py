from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from Services.NFDiscovery.schemas import *
from Services.schemas import *

app = Flask(__name__)
api = Api(app)

def Check(nfservice_post):
    for i in range(nfslist):
        if jsonify(nfservice_post) == jsonify(nfslist[i]):
            return 200
    return 404

class Discovery(Resource):
    def get(self):
        getData = request.get_json()
        # plmnCheck1 = PlmnId('208', '93')
        # plmnCheck2 = PlmnId('20', '9')
        # nfservice_post.plmnList.append(plmnCheck1)
        # nfservice_post.plmnList.append(plmnCheck2)
        
        try:
            for i in range(0,3):
                if getData["nfType"] == nfslist[i].nfType:
                    return 200
        except:
            return 404
        return 400
        
