import matplotlib as plt
from avantlib import init, connect, mame, terAlt, cre, ex
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://user:wPrU3lO40KCN3YWN@avant.kp8vmpd.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['avant']
map_data = db['map_data']

init()
connect()

while True:
    ch = mame()
    if ch == 1:
        start()
    elif ch == 2:
        htu()
    elif ch == 3:
        if cre():
            continue
        else:
            break
    elif ch == 4:
        ex()
    else:
        terAlt()
        break