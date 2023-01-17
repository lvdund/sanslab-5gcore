from flask import request, jsonify
from flask_restful import Resource
import json

import app

class GetData(Resource):
    def put(self):
        putData = request.get_json()
        # with open("static/getdata.json", "w") as outfile:
        #     json.dump(putData, outfile)
        collection = app.free5gc_db.nfprofile
        collection.insert_one(putData)
        return 200
    def get(self):
        getData = []
        nfprofile_collection = app.free5gc_db.nfprofile
        nfpfs = nfprofile_collection.find()
        for nfpf in nfpfs:
            with open("static/getdata.json", "w") as outfile:
                json.dump(nfpf["nfServices"][0]["ipEndPoints"][0]["ipv4Address"], outfile)
            break
        return 200