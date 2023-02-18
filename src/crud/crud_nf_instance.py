from src.database.database import NfProfile_collection, urilist_collection

def get_nf_instance(nfInstanceId):
    try:
        nf_profile = NfProfile_collection.find_one({"nfInstanceId": nfInstanceId})
        return nf_profile
    except:
        return None
    
def dc_get_nf_instance(find_value):
    try:
        a = []
        list_nf_profile = NfProfile_collection.find(find_value)
        for i in list_nf_profile:
            a.append(i["nfType"])
        return a
    except:
        return None

def create_nf_instance(nfInstanceId, nf_profile):
    if get_nf_instance(nfInstanceId= nfInstanceId) != None:
        print("NF has already registered")
        return 400
    try:
        if "nfInstanceId" not in nf_profile:
            nf_profile["nfInstanceId"] = nfInstanceId
        if nf_profile["nfInstanceId"] != nfInstanceId:
            return 400
        _link = "http://127.0.0.10:8000/nnrf-nfm/v1/nf-instances/" + nf_profile["nfInstanceId"]
        uri_dict = {
            "nfType": nf_profile["nfType"],
            "_link": _link
        }
        NfProfile_collection.insert_one(nf_profile)
        urilist_collection.insert_one(uri_dict)
        print("Register NF")
        return 200
    except:
        print("Cannot insert to NfProfile_collection collection")
        return 400

def delete_nf_instance(nfInstanceId):
    if get_nf_instance(nfInstanceId= nfInstanceId) == None:
        print("NF does not exist")
        return 400
    try:
        NfProfile_collection.delete_one({"nfInstanceId": nfInstanceId})
        
        print("Deleted: " + str(nfInstanceId))
        return 200
    except:
        print("Cannot delete: " + str(nfInstanceId))
        return 400

def modify_nf_instance(nfInstanceId, update_values, status = None):
    if get_nf_instance(nfInstanceId= nfInstanceId) == None:
        print("NF does not exist")
        return 400
    if status is not None:
        try:
            suspended_status = {"nfStatus": "SUSPENDED"}
            new_values = { "$set": suspended_status}
            NfProfile_collection.update_one({"nfInstanceId": nfInstanceId}, new_values)
            print("suspended_status")
            return 200
        except:
            print("error")
            return 400
    try:
        new_values = { 
                      "$set": update_values
                      }
        NfProfile_collection.update_one({"nfInstanceId": nfInstanceId}, new_values)
        return 200
    except:
        print("Cannot update")
        return 400