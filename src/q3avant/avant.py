from avantlib import init, connect, exception, mame, cre, ex, htu, start
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://user:wPrU3lO40KCN3YWN@avant.kp8vmpd.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['avant']
map_data = db['map_data']

try:
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
            ex()
            break
except KeyboardInterrupt:
    ex()
except Exception as err:
    exception(err, 5)