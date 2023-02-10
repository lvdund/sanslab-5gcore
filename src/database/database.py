from pymongo import MongoClient
from src.env.config import settings

free5gc_db = None
NfProfile = None
urilist = None

def connect_to_database():
    try:
        global free5gc_db
        global NfProfile
        global urilist
        client = MongoClient(settings.connection_string)
        free5gc_db = client.free5gc
        NfProfile = free5gc_db.NfProfile
        urilist = free5gc_db.urilist
        print("successful connection to database")
    except:
        raise Exception("Cannot connect to database")