# from flask import request, jsonify
# from flask_restful import Resource
# from crud import nf_instance

# class NFInstance_Document(Resource):
#     # register
#     def put(self, nfInstanceId):
#         return nf_instance.create_nf_instance(nf_profile=request.get_json(), nfInstanceId= nfInstanceId)
#     # read
#     def get(self, nfInstanceId):
#         nf_prf = nf_instance.get_nf_instance(nfInstanceId= nfInstanceId)
#         if nf_prf != None:
#             nf_prf["_id"] = str(nf_prf["_id"])
#             return nf_prf
#         return None
#     # deregister
#     def delete(self, nfInstanceId):
#         return nf_instance.delete_nf_instance(nfInstanceId= nfInstanceId)
#     # modify
#     def patch(self, nfInstanceId):
#         return nf_instance.modify_nf_instance(nfInstanceId= nfInstanceId, update_values= request.get_json())