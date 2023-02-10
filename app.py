from quart import Quart, request
app = Quart(__name__)

from src.database.database import connect_to_database
connect_to_database()

from src.api.nnrf_nfm.v1.endpoints.nf_instances import *

if __name__ == "__main__":
    app.run() # type: ignore