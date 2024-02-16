from avantlib import init, connect, exception, mame, cre, ex, htu, start
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://user:wPrU3lO40KCN3YWN@avant.kp8vmpd.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['avant']
map_data = db['map_data']

def exec():
    try:
        init()
        connect()
        while True:
            ch = mame()
            if ch == 1:
                if start():
                    continue
            elif ch == 2:
                if htu():
                    continue
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

exec()