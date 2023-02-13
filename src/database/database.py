from pymongo import MongoClient
from src.env.config import settings

free5gc_db = None
NfProfile_collection = None
urilist_collection = None
Subscriptions_collection =None

def connect_to_database():
    try:
        global free5gc_db
        global NfProfile_collection
        global urilist_collection
        global Subscriptions_collection
        client = MongoClient(settings.connection_string)
        free5gc_db = client.free5gc
        NfProfile_collection = free5gc_db.NfProfile
        urilist_collection = free5gc_db.urilist
        Subscriptions_collection =free5gc_db.Subscriptions
        print("successful connection to database")
    except:
        raise Exception("Cannot connect to database")