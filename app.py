from quart import Quart, request, jsonify
from crud import nf_instance

app = Quart(__name__)

# NF Management

# NF Instance ID (Document): register, deregister, read, update

@app.put("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_register(nfInstanceId):
    return jsonify(nf_instance.create_nf_instance(nf_profile=await request.get_json(), nfInstanceId=nfInstanceId))

@app.delete("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_deregister(nfInstanceId):
    return jsonify(nf_instance.delete_nf_instance(nfInstanceId=nfInstanceId))

@app.get("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_read(nfInstanceId):
    nf_prf = nf_instance.get_nf_instance(nfInstanceId= nfInstanceId)
    if nf_prf != None:
        nf_prf["_id"] = str(nf_prf["_id"])
        return nf_prf
    return None

@app.patch("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_update(nfInstanceId):
    return jsonify(nf_instance.modify_nf_instance(nfInstanceId=nfInstanceId, update_values=await request.get_json()))


if __name__ == "__main__":
    app.run()