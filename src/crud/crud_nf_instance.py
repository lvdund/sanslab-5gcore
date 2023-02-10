from src.database.database import NfProfile, urilist
from src.schemas.HeartBeatTimer import listNF_heartBeatTimer, Nf_heartBeat
from src.schemas.common.NfInstanceId import NfInstanceId
from src.schemas.NFStatus import NFStatus
import time
# from bson.objectid import ObjectId

# from Services import environment

def get_nf_instance(nfInstanceId):
    try:
        nf_profile = NfProfile.find_one({"nfInstanceId": nfInstanceId})
        return nf_profile
    except:
        return None
    
def dc_get_nf_instance(find_value):
    try:
        a = []
        list_nf_profile = NfProfile.find(find_value)
        for i in list_nf_profile:
            a.append(i["nfType"])
        return a
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
        NfProfile.insert_one(nf_profile)
        print("Register NF")
        listNF_heartBeatTimer.append(Nf_heartBeat(nfInstanceId=NfInstanceId(nfInstanceId), nfStatus=NFStatus.REGISTERED, updateTime=time.time()))
        return 200
    except:
        print("Cannot insert to nfProfile collection")
        return 400

def delete_nf_instance(nfInstanceId):
    if get_nf_instance(nfInstanceId= nfInstanceId) == None:
        print("NF does not exist")
        return 400
    try:
        NfProfile.delete_one({"nfInstanceId": nfInstanceId})
        for i in range(len(listNF_heartBeatTimer)):
            if listNF_heartBeatTimer[i].nfInstanceId == nfInstanceId:
                del listNF_heartBeatTimer[i]
        
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
        update_values.update({"nfStatus": "REGISTERED"})
        new_values = { "$set": update_values}
        NfProfile.update_one({"nfInstanceId": nfInstanceId}, new_values)
        for i in range(len(listNF_heartBeatTimer)):
            if listNF_heartBeatTimer[i].nfInstanceId == nfInstanceId:
                listNF_heartBeatTimer[i].updateTime = time.time()
        
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