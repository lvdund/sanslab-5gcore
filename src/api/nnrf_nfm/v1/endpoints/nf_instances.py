from app import app, request
import requests
from quart import jsonify
from src.crud.crud_nf_instance import *
from src.database.database import Subscriptions_collection
from src.schemas.NotificationData import NotificationData, NotificationEventType, Uri, NFProfile
from src.env.config import settings


"""NF Register
Returns:
    NfProfile: if NF registered successful
    None: if cannot register
"""


@app.put("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_register(nfInstanceId):

    nf_pf = await request.get_json()
    if settings.plmnId not in nf_pf["plmnList"] or nfInstanceId != nf_pf["nfInstanceId"]:
        return jsonify(400)

    action = create_nf_instance(nf_profile=await request.get_json(), nfInstanceId=nfInstanceId)

    """NF Status Notify
        This service is used to notify to subscribers when a NF is registed
    """
    if action == 200:
        del nf_pf["_id"]
        for sb in Subscriptions_collection.find():
            notify = NotificationData(
                event=NotificationEventType.NF_REGISTERED,
                nfInstanceUri=Uri(str(request.url)),
                nfProfile=NFProfile(**nf_pf)
            )
            requests.post(
                url=sb["nfStatusNotificationUri"],  # type: ignore
                json={
                    "NotificationData": notify.json()
                }
            )

    return jsonify(nf_pf)


"""NF Deregister
"""


@app.delete("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_deregister(nfInstanceId):
    nf_pf = delete_nf_instance(nfInstanceId=nfInstanceId)

    """NF Status Notify
        This service is used to notify to subscribers when a NF is deregisted
    """
    if nf_pf == 200:
        for sb in Subscriptions_collection.find():
            notify = NotificationData(
                event=NotificationEventType.NF_DEREGISTERED,
                nfInstanceUri=Uri(str(request.url))
            )
            requests.post(
                url=sb["nfStatusNotificationUri"],  # type: ignore
                json={
                    "NotificationData": notify.json()
                }
            )
    return


@app.get("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_read(nfInstanceId):
    nf_prf = get_nf_instance(nfInstanceId=nfInstanceId)
    if nf_prf != None:
        nf_prf["_id"] = str(nf_prf["_id"])
        return nf_prf
    return


"""NF Update 
"""


@app.patch("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_update(nfInstanceId):
    nf_pf = modify_nf_instance(nfInstanceId=nfInstanceId, update_values=await request.get_json())

    """NF Status Notify
        This service is used to notify to subscribers when a NF is update
    """
    if nf_pf == 200:
        _nf = await request.get_json()
        for sb in Subscriptions_collection.find():
            notify = NotificationData(
                event=NotificationEventType.NF_PROFILE_CHANGED,
                nfInstanceUri=Uri(str(request.url)),
                profileChanges=[_nf]
            )
            requests.post(
                url=sb["nfStatusNotificationUri"],  # type: ignore
                json={
                    "NotificationData": notify.json()
                }
            )
    return jsonify(nf_pf)


@app.get("/nnrf-nfm/v1/nf-instances")
async def nf_discovery():
    return jsonify(dc_get_nf_instance(find_value=await request.get_json()))
