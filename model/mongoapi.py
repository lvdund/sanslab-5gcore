import pymongo

client = pymongo.MongoClient("mongdb://localhost:27017/", serverSelectionTimeoutMS=5000)
Client = None
try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")

def SetMongoDB(dbname, url):
    if Client is not None:
        return None
    