from src.database.database import Subscriptions_collection
import uuid

def get_subscription(subscriptionId):
    try:
        subscription_profile = Subscriptions_collection.find_one({"subscriptionId": subscriptionId})
        return subscription_profile
    except:
        return None

def create_subscription(subscription_profile):
    try:
        subscription_profile["subscriptionId"] = str(uuid.uuid4())
        Subscriptions_collection.insert_one(subscription_profile)
        print("Created Subscription")
        return 200
    except:
        print("Cannot insert to Subscriptions collection")
        return 400

def delete_subscription(subscriptionId):
    if get_subscription(subscriptionId=subscriptionId) == None:
        print("Subscriptions does not exist")
        return 400
    try:
        Subscriptions_collection.delete_one({"subscriptionId": subscriptionId})
        print(f"Subscriptions deleted: {subscriptionId}")
    except:
        print("Cannot delete Subscription")
        return 400
    
def update_subscription(subscriptionId, update_values):
    if get_subscription(subscriptionId=subscriptionId) == None:
        print("Subcription does not exist")
        return 400
    try:
        new_values = { "$set": update_values}
        Subscriptions_collection.update_one({"subscriptionId": subscriptionId}, new_values)
        return 200
    except:
        print("Subscriptions cannot update")
        return 400