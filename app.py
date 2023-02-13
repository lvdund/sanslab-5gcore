from threading import Thread

from quart import Quart, request
app = Quart(__name__)

from src.database.database import connect_to_database
connect_to_database()

from src.api.nnrf_nfm.v1.endpoints.nf_instances import *
from src.api.nnrf_nfm.v1.endpoints.subscriptions import *
# nf_heart_beat_timer.start()    

quart_app = Thread(target=app) # type: ignore
if __name__ == "__main__":
    # quart_app.start()
    app.run() # type: ignore 