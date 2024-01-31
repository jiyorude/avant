import time
import sys
import os
import inquirer
import avantxt
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

def ex():
    clear()
    iterate(0.5, 0.025, *avantxt.exit_two)
    wait(1.5)
    clear()
    wait(0.5)
    sys.exit(0)

def exception(err: any, x: int):
    clear()
    print()
    iterate(0.4, 0.025, f"An error occurred: {err}.\n")
    for y in range(x, -1, -1):
        terminateAlt(y)
        wait(1)
    clear()
    sys.exit(0)

def print_ascii():
    for line in avantxt.ascii.splitlines():
        iterate(0.1, 0.010, *line)

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
    tma = f"Avant will shut down in {int} seconds"
    print("\033[K", end="")
    print(f"{tma:<30}", end="\r")

def terAlt():
    for x in range(4, -1, -1):
        terminateAlt(x)
        wait(1)

def getTime():
    now = datetime.now()
    formatted = now.strftime("%A %d %B %Y - %H:%M")
    return f"Algorithm initiated at: {formatted}\n\n"

def find(que: str, col: str):
    succ = f"Your search for {que} returned {int(len(col_find))} results:"
    col_find = col.find(que)
    if not col_find:
        iterate(1, 0.025, *avantxt.search_fail)
    else:
        iterate(1, 0.025, *succ)
        for data in col_find:
            iterate(0.1, 0.025, data)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def double_print():
    return print(), print()
        
def init():
    return print_ascii(), print(), iterate(0.4, 0.025, *avantxt.i2), iterate(0.4, 0.025, *avantxt.i3), iterate(0.6, 0.025, *avantxt.i4), iterate(1.5, 0.025, *getTime())

def connect():
    try:
        client.admin.command('ping')
        for x in range(0, 101, 1):
            progress(x)
            wait(0.025)
        iterate(0.8, 0.025, *avantxt.sc)
        wait(2)
        clear()
    except Exception as err:
        iterate(0.8, 0.025, *avantxt.se)
        wait(0.5)
        print(f"{err}\n")
        wait(0.5)
        for x in range(4, -1, -1):
            terminate(x)
            wait(1)
        print()
        clear()
        sys.exit(0)

def mame():
    try:
        wait(0.7)
        print(avantxt.ascii)
        print()
        mame = [inquirer.List('choice',
        message='MAIN MENU',
        choices=[
            avantxt.start_algorithm,
            avantxt.help,
            avantxt.credits,
            avantxt.exit
        ])]
        ini_mame = inquirer.prompt(mame)
        if ini_mame is None:
            return None
        sel_mame = ini_mame['choice']
        ch = 1 if sel_mame == "Start Algorithm" else 2 if sel_mame == "Help" else 3 if sel_mame == "Credits" else 4 if sel_mame == "Exit" else 5
        return ch
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

def cre():
    clear()
    wait(0.7)
    print()
    print(avantxt.ascii_credits)
    iterate(0.5, 0.025, *avantxt.cred)
    iterate(0.7, 0.025, *avantxt.cred_2)
    iterate(0.7, 0.025, *avantxt.cred_3)
    iterate(0.7, 0.025, *avantxt.cred_4)
    wait(0.4)
    input(avantxt.any)
    clear()
    wait(0.5)
    return True

def show_bg():
    print(avantxt.bg_t + avantxt.bg + avantxt.bg_2 + avantxt.bg_3 + avantxt.bg_4 + avantxt.bg_5 + avantxt.bg_6 + avantxt.bg_7 + avantxt.bg_8 +
          avantxt.bg_9 + avantxt.bg_10 + avantxt.bg_11 + avantxt.bg_12 + avantxt.bg_13 + avantxt.bg_14 + avantxt.bg_15 + avantxt.bg_16)
    wait(5)
    print()
    input(avantxt.any2)
    clear()
    wait(0.7)
    print(avantxt.ascii_help)

def show_modes():
    return sys.exit(0)

def show_htu():
    return sys.exit(0)

def show_intpr():
    return sys.exit(0)

def show_trbs():
    return sys.exit(0)

def show_log():
    return sys.exit(0)

def show_lcn():
    return sys.exit(0)

def htu():
    clear()
    wait(0.7)
    print()
    print(avantxt.ascii_help)
    opt = [avantxt.h1, avantxt.h2, avantxt.h3, avantxt.h4, avantxt.h5, avantxt.h6, avantxt.h7, avantxt.h8]
    while True:
        iterate(0.5, 0.025, *"Select a topic for more information\n")
        wait(0.5)
        selected_option = inquirer.prompt([
            inquirer.List('topic', choices=opt)
        ])['topic']
        if selected_option == avantxt.h1:
            clear()
            wait(0.7)
            show_bg()
        elif selected_option == avantxt.h2:
            clear()
            wait(0.7)
            show_modes()
        elif selected_option == avantxt.h3:
            clear()
            wait(0.7)
            show_htu()
        elif selected_option == avantxt.h4:
            clear()
            wait(0.7)        
            show_intpr()
        elif selected_option == avantxt.h5:
            clear()
            wait(0.7)
            show_trbs()
        elif selected_option == avantxt.h6:
            clear()
            wait(0.7)
            show_log()
        elif selected_option == avantxt.h7:
            clear()
            wait(0.7)
            show_lcn()
        elif selected_option == avantxt.h8:
            clear()
            wait(0.7)
            break