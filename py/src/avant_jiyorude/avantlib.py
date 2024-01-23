import time
import sys
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://user:welcome123@avant.kp8vmpd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['avant']
map_data = db['map_data']

def iterate(bdel: int, tdel: float, *str: any):
    time.sleep(bdel)
    for char in str:
        print(char, end='', flush=True)
        time.sleep(tdel)
    print()

def progress(int: int):
    print(f"{int}%", end='\r')

def terminate(int: int):
    print(f"Avant cannot connect to the database. Terminating in {int} seconds", end='\r')

def getTime():
    now = datetime.now()
    formatted = now.strftime("%A %d %B %Y - %H:%M")
    return f"Algorithm initiated at: {formatted}\n\n"

def find(que, col):
    fail = "No results. Please try again."
    succ = f"Your search for {que} returned {len(col_find)} results:"
    col_find = col.find(que)
    if not col_find:
        iterate(1, 0.025, *fail)
    else:
        iterate(1, 0.025, *succ)
        for data in col_find:
            iterate(0.5, 0.025, data)
        
def init():
    i1 = "\n\nAVANT\n"
    i2 = "Random-data generating algorithm for experimental, Quake III machinima (post-) production" 
    i3 = "Created by Jordy Veenstra / A Pixelated Point of View"
    i4 = "\nVersion 0.0.2\n\n"
    iterate(1, 0.025, *i1), iterate(0.4, 0.025, *i2), iterate(0.4, 0.025, *i3), iterate(0.6, 0.025, *i4), iterate(1.5, 0.025, *getTime())

def connect():
    sc = "Succesfully connected to avant database\n"
    e = "Could not connect to avant database"
    try:
        client.admin.command('ping')
        for x in range(0, 101, 1):
            progress(x)
            time.sleep(0.025)
        iterate(0.8, 0.025, *sc)
    except Exception as err:
        iterate(0.8, 0.025, *e)
        time.sleep(0.5)
        print(f"{err}\n")
        time.sleep(0.5)
        for x in range(4, -1, -1):
            terminate(x)
            time.sleep(1)
        print()
        sys.exit()
