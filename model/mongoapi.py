import pymongo

# client = pymongo.MongoClient("mongdb://localhost:27017/", serverSelectionTimeoutMS=5000)
# Client = None
# try:
#     print(client.server_info())
# except Exception:
#     print("Unable to connect to the server.")

Client = None
dbName = ''

def SetMongoDB(dbname, url):
    global Client
    global dbName
    if Client is not None:
        return None
    client = pymongo.MongoClient("mongdb://localhost:27017/", serverSelectionTimeoutMS=5000)
    try :
        print(client.server_info())
    except Exception:
        print("Unable to connect to the server.")
        return False
    Client = client
    dbName = dbname
    return None
