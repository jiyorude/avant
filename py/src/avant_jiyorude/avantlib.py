import time
import sys
import os
import inquirer
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

uri = "mongodb+srv://user:wPrU3lO40KCN3YWN@avant.kp8vmpd.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['avant']
map_data = db['map_data']

def wait(int: int):
    time.sleep(int)

def iterate(bdel: int, tdel: float, *str: any):
    wait(bdel)
    for char in str:
        print(char, end='', flush=True)
        wait(tdel)
    print()

def progress(int: int):
    print(f"{int}%", end='\r')

def terminate(int: int):
    print(f"Avant cannot connect to the database. Terminating in {int} seconds", end='\r')

def terminateAlt(int: int):
    print(f"An error occurred. Avant will shut down in {int} seconds", end="\r")

def terAlt():
    for x in range(4, -1, -1):
        terminateAlt(x)
        wait(1)

def getTime():
    now = datetime.now()
    formatted = now.strftime("%A %d %B %Y - %H:%M")
    return f"Algorithm initiated at: {formatted}\n\n"

def find(que: str, col: str):
    fail = "No results. Please try again."
    succ = f"Your search for {que} returned {int(len(col_find))} results:"
    col_find = col.find(que)
    if not col_find:
        iterate(1, 0.025, *fail)
    else:
        iterate(1, 0.025, *succ)
        for data in col_find:
            iterate(0.5, 0.025, data)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ex():
    clear()
    line = "\n\nExiting...\n"
    iterate(1, 0.025, *line)
    wait(1.5)
    sys.exit()

def double_print():
    print()
    print()
        
def init():
    i1 = "\n\nAVANT\n"
    i2 = "Random-data generating algorithm for experimental, Quake III machinima (post-) production" 
    i3 = "Created by Jordy Veenstra / A Pixelated Point of View"
    i4 = "\nVersion 0.0.2\n"
    iterate(1, 0.025, *i1), iterate(0.4, 0.025, *i2), iterate(0.4, 0.025, *i3), iterate(0.6, 0.025, *i4), iterate(1.5, 0.025, *getTime())

def connect():
    sc = "Succesfully connected to avant database\n"
    e = "Could not connect to avant database"
    try:
        client.admin.command('ping')
        for x in range(0, 101, 1):
            progress(x)
            wait(0.025)
        iterate(0.8, 0.025, *sc)
        wait(2)
        clear()
    except Exception as err:
        iterate(0.8, 0.025, *e)
        wait(0.5)
        print(f"{err}\n")
        wait(0.5)
        for x in range(4, -1, -1):
            terminate(x)
            wait(1)
        print()
        sys.exit()

def mame():
    wait(0.4)
    double_print()
    mame = [inquirer.List('choice',
    message='MAIN MENU',
    choices=[
        "Start Algorithm",
        "Help",
        "Credits",
        "Exit"
    ])]
    ini_mame = inquirer.prompt(mame)
    sel_mame = ini_mame['choice']
    ch = 1 if sel_mame == "Start Algorithm" else 2 if sel_mame == "Help" else 3 if sel_mame == "Credits" else 4 if sel_mame == "Exit" else 5
    return ch

def cre():
    clear()
    double_print()
    cred = "AVANT\nRandom-data generating algorithm for experimental, Quake III machinima (post-) production\nCreated by Jordy Veenstra / A Pixelated Point of View\n\n"
    cred_2 = "GitHub: https://github.com/jiyorude/avant\nIssues: https://github.com/jiyorude/avant/issues\nBitBucket: https://bitbucket.org/appov/avant/src/main/\n\nPyPi: T.B.A\nNPM: T.B.A\nFront-End: T.B.A.\n"
    cred_3 = "Acknowledgements:\nPython 3.11 (Python Software Foundation)\nPyMongo (MongoDB Python Team)\nInquirer (Miguel Ángel García)\nMatplotlib (John D. Hunter, Michael Droettboom)\nReportlab (Andy Robinson, Robin Becker)\nAvantlib (Jordy Veenstra)\n\n"
    iterate(1.5, 0.025, *cred)
    iterate(1, 0.025, *cred_2)
    iterate(1, 0.025, *cred_3)
    wait(0.4)
    ret_mame = inquirer.prompt([
        inquirer.Confirm('return_to_menu', message='Return to main menu?', default=True)
    ])
    if ret_mame['return_to_menu']:
        clear()
        wait(0.5)
        return True
    return False






# These serve for destructuring purposes later in the setup function
sc = None #software choice (mme or wolfcam)
mc = None #map choice (freemap, map assist or custom map or custom assist)
pc = None #production choice (production, post, workflow)
cc = None #custom choice (true false)
dc = None #depth choice (true or false)
pc = None #print choice (full or minimal)