# from bson.objectid import ObjectId
from .database import free5gc_db
from Services import environment

# collections
nfprofile_collection = free5gc_db.NfProfile

def get_nf_instance(nfInstanceId):
    try:
        nf_profile = nfprofile_collection.find_one({"nfInstanceId": nfInstanceId})
        return nf_profile
    except:
        return None

def create_nf_instance(nfInstanceId, nf_profile):
    if get_nf_instance(nfInstanceId= nfInstanceId) != None:
        print("NF has already registered")
        return 400
    # if not check_plmnId(nf_profile["plmnList"]):
    #     print("NF is not in same plmnId")
    #     return 400
    try:
        if "nfInstanceId" not in nf_profile:
            nf_profile["nfInstanceId"] = nfInstanceId
        nfprofile_collection.insert_one(nf_profile)
        print("Register NF")
        return 200
    except:
        print("Cannot insert to nfProfile collection")
        return 400

def delete_nf_instance(nfInstanceId):
    if get_nf_instance(nfInstanceId= nfInstanceId) == None:
        print("NF does not exist")
        return 400
    try:
        nfprofile_collection.delete_one({"nfInstanceId": nfInstanceId})
        print("Deleted: " + str(nfInstanceId))
        return 200
    except:
        print("Cannot delete: " + str(nfInstanceId))
        return 400

def modify_nf_instance(nfInstanceId, update_values):
    if get_nf_instance(nfInstanceId= nfInstanceId) == None:
        print("NF does not exist")
        return 400
    try:
        new_values = { "$set": update_values}
        nfprofile_collection.update_one({"nfInstanceId": nfInstanceId}, new_values)
        return 200
    except:
        print("Cannot update")
        return 400

# def check_plmnId(plmn_lists):
#     for x in plmn_lists:
#         for y in environment.plmnId:
#             if x["mcc"] == y.mcc and x["mnc"] == y.mnc:
#                 return True
#     return False