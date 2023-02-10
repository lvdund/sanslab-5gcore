from app import app, request
from src.env.config import settings
from quart import jsonify
from src.crud.crud_nf_instance import *
from src.schemas.HeartBeatTimer import listNF_heartBeatTimer
from src.schemas.NFStatus import NFStatus
import time

@app.put("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_register(nfInstanceId):
    return jsonify(create_nf_instance(nf_profile=await request.get_json(), nfInstanceId=nfInstanceId))

@app.delete("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_deregister(nfInstanceId):
    return jsonify(delete_nf_instance(nfInstanceId=nfInstanceId))

@app.get("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_read(nfInstanceId):
    nf_prf = get_nf_instance(nfInstanceId= nfInstanceId)
    if nf_prf != None:
        nf_prf["_id"] = str(nf_prf["_id"])
        return nf_prf
    return None

@app.patch("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_update(nfInstanceId):
    return jsonify(modify_nf_instance(nfInstanceId=nfInstanceId, update_values=await request.get_json()))

# NF Heart-Beat
def nf_heart_beat():
    while True:
        time.sleep(settings.hear_beat_timer)
        current_time = time.time()
        for nf in listNF_heartBeatTimer:
            if (current_time-nf.updateTime)>5.5:
                nf.nfStatus = NFStatus.SUSPENDED
                modify_nf_instance(nfInstanceId=nf.nfInstanceId, update_values={"nfStatus": "SUSPENDED"})

@app.get("/nnrf-nfm/v1/nf-instances")
async def nf_discovery():
    return jsonify(dc_get_nf_instance(find_value=await request.get_json()))


