import time
import sys
import requests
import os
import inquirer
import avantxt
import avantutils
import platformdirs
import webbrowser
from pathlib import Path
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

global projectname
global framerate
global algselect
global algbool

now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# Algorithm Functions
def projname():
    global projectname
    avantutils.iterate(0.5, 0.025, *avantxt.setup_1)
    projectname = input()
    while len(projectname) > 30:
        avantutils.iterate(0.5, 0.025, *avantxt.setup_2)
        projectname = input()
    avantutils.double_print()

def fps():
    global framerate
    avantutils.iterate(0.5, 0.025, *avantxt.setup_3)
    while True:
        try:
            framerate = float(input())
            if framerate.is_integer():
                framerate = int(framerate)
            break
        except ValueError:
            pass
        avantutils.iterate(0.5, 0.025, *avantxt.setup_4)
    avantutils.double_print()

def algomode():
    global algselect
    avantutils.iterate(0.5, 0.025, *avantxt.setup_5)
    almo = [inquirer.List('algchoice',
        choices=[
            avantxt.mode_one,
            avantxt.mode_two,
            avantxt.mode_three,
        ])]
    almo_ch = inquirer.prompt(almo)
    if almo_ch is None:
        return None
    selected_mode = almo_ch['algchoice']
    match(selected_mode):
        case "Production Mode (Production data and capturing files)":
            algselect = "Production Mode"
            avantutils.wait_and_clear(0.5)
            confirm()
        case "Post Mode (Editing data only)":
            algselect = "Post Mode"
            avantutils.wait_and_clear(0.5)
            confirm()
        case "Full Service mode (Production- and Post Mode combined)":
            algselect = "Full Service Mode"
            avantutils.wait_and_clear(0.5)
            confirm()
            
def confirm():
    global algbool
    algbool = False
    avantutils.wait(0.5)
    avantutils.iterate(0.8, 0.025, *avantxt.confirm_one)
    avantutils.iterate(0.8, 0.025, *f"Project name: {projectname}")
    avantutils.iterate(0.8, 0.025, *f"Framerate: {framerate} frames per second")
    avantutils.iterate(0.8, 0.025, *f"Selected algorithm mode: {algselect}")
    avantutils.iterate(0.8, 0.025, *avantxt.confirm_two)
    while True:
        choice = input().casefold()
        if choice == "y" or choice == "n" or choice == "yes" or choice == "no":
            if choice == "y" or choice == "yes":
                algbool = True
                break
            elif choice == "n" or choice == "no":
                algbool = False
                break
        print("Please answer with 'y' for Yes, or 'n' for No.")

def prod_mode():
    print("production mode started")

def post_mode():
    avantutils.clear()
    avantutils.wait(1)
    now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    doc_path = platformdirs.user_documents_dir()
    project_dir = os.path.join(doc_path, "Avant", f"POST | {projectname} | ({framerate} fps) | {now}")
    try:
        os.makedirs(project_dir, exist_ok=True)
        for subdir in ["Footage", "Image Sequences", "XML", "EDL", "PDF", "Readme"]:
            subdir_path = os.path.join(project_dir, subdir)
            os.makedirs(subdir_path, exist_ok=True)
        avantutils.iterate(0.8, 0.025, *avantxt.post_one)
        avantutils.iterate(0.8, 0.025, *avantxt.post_two)
        avantutils.wait(2)
        if os.path.isdir(doc_path):
            webbrowser.open(f"file://{doc_path}")
        avantutils.wait(1)
        input("Press the ENTER/RETURN key on your keyboard whenever you are ready to analyze your footage.")
    except OSError as e:
        print(f"Error: {e}")
        sys.exit(0)

def full_mode():
    print("full service mode has started")

# Main Functions
def init():
    return avantutils.print_ascii(), print(), avantutils.iterate(0.4, 0.025, *avantxt.i2), avantutils.iterate(0.4, 0.025, *avantxt.i3), avantutils.iterate(0.6, 0.025, *avantxt.i4), avantutils.iterate(1.5, 0.025, *avantutils.getTime())

def connect():
    avantutils.iterate(0.8, 0.025, *avantxt.sd)
    local_filename = './database.json'
    try:
        if os.path.isfile(local_filename):
            for x in range(0, 101, 1):
                avantutils.progress(x)
                avantutils.wait(0.025)
            avantutils.iterate(0.8, 0.025, *avantxt.sc)
            avantutils.wait_and_clear(2)
        else:
            avantutils.iterate(0.8, 0.025, *avantxt.nf)
            url = "http://example.com/path/to/your/file.json" # CHANGE URL HERE WHEN DB IS READY
            try:
                with requests.get(url) as response:
                    avantutils.iterate(0.8, 0.025, *avantxt.ad)
                    response.raise_for_status()
                    with open(local_filename, 'wb') as file:
                        file.write(response.content)
                    avantutils.iterate(0.8, 0.025, *avantxt.sdd)
            except Exception as err:
                print(f"{err}\n")
                avantutils.clear()
                sys.exit(0)
    except Exception as err:
        avantutils.iterate(0.8, 0.025, *avantxt.se)
        avantutils.wait(0.5)
        print(f"{err}\n")
        avantutils.wait(0.5)
        for x in range(4, -1, -1):
            avantutils.terminate(x)
            avantutils.wait(1)
        print()
        avantutils.clear()
        sys.exit(0)
        
def mame():
    try:
        avantutils.wait(0.7)
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
        ch = 1 if sel_mame == "Start Algorithm" else 2 if sel_mame == "Documentation" else 3 if sel_mame == "Credits" else 4
        return ch
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

def cre():
    avantutils.wait_and_clear(0.7)
    print()
    avantutils.iterate(0.5, 0.025, *avantxt.cred)
    avantutils.iterate(0.7, 0.025, *avantxt.cred_2)
    avantutils.iterate(0.7, 0.025, *avantxt.cred_3)
    avantutils.wait(0.4)
    input(avantxt.any)
    avantutils.wait_and_clear(0.5)
    return True

def htu():
    avantutils.wait_and_clear(0.7)
    print()
    avantutils.iterate(0.5, 0.025, *avantxt.help_1)
    print()
    avantutils.iterate(0.5, 0.025, *avantxt.help_2)
    print()
    avantutils.wait(0.4)
    input(avantxt.any)
    avantutils.clear()
    avantutils.wait(0.5)
    return True

def start():
    global algbool
    avantutils.wait_and_clear(0.5)
    print()
    projname()
    avantutils.wait(1)
    fps()
    avantutils.wait(1)
    algomode()
    if algbool:
        match(algselect):
            case "Production Mode":
                prod_mode()
            case "Post Mode":
                post_mode()
            case "Full Service Mode":
                full_mode()
            case _:
                pass
    if not algbool:
        cach = [inquirer.List('cancelchoice',
        message= 'RETURN TO MAIN MENU, START OVER, OR RECONFIRM CHOICES?',
        choices=[
            avantxt.cancel_one,
            avantxt.cancel_two,
            avantxt.cancel_three
        ])]
        cancel_choice = inquirer.prompt(cach)
        selected_choice = cancel_choice['cancelchoice']
        if selected_choice is None:
            return None
        selected_choice = 1 if cancel_choice['cancelchoice'] == avantxt.cancel_one else 2 if cancel_choice['cancelchoice'] == avantxt.cancel_two else 3
        match (selected_choice):
            case 1:
                pass
            case 2:
                avantutils.clear()
                avantutils.wait(1)
                projname()
                fps()
                algomode()
            case 3:
                algbool = True
                if algbool:
                    match(algselect):
                        case "Production Mode":
                            prod_mode()
                        case "Post Mode":
                            post_mode()
                        case "Full Service Mode":
                            full_mode()
                        case _:
                            pass
    avantutils.wait_and_clear(1)
    return True