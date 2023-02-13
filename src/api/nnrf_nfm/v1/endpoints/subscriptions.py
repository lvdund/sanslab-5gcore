from app import app, request, jsonify
from src.crud.crud_subscriptions import *

@app.post("/nnrf-nfm/v1/subscriptions")
async def nf_status_subscribe():
    return jsonify(create_subscription(subscription_profile=await request.get_json()))

@app.patch("/nnrf-nfm/v1/subscriptions/<subscriptionId>")
async def nf_status_update_subscribe(subscriptionId):
    return jsonify(update_subscription(subscriptionId=subscriptionId, update_values=await request.get_json()))

@app.delete("/nnrf-nfm/v1/subscriptions/<subscriptionId>")
async def nf_status_unsubscribe(subscriptionId):
    return jsonify(delete_subscription(subscriptionId=subscriptionId))