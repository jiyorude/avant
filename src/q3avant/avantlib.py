import time
import sys
import requests
import os
import glob
import inquirer
import avantxt
import avantutils
import platformdirs
import webbrowser
import ffmpeg
import random
from moviepy.editor import VideoFileClip
from pathlib import Path
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Globals for algorithm
global projectname # Projectname
global framerate # Selected framerate for the project
global algselect # Selected algorithm mode
global algbool # Checker to verify projectdata

# Globals for filedata
global containers # Source material container, such as mp4, mpeg, mov.
global filenames # File name
global codecs # Source material codec, such as h264, hevc, apr4444xq
global framerates # Source material frames per second 
global widths # Width resolution
global heights # Height resolution
global durations # Original length of clip
global newlength # New length of clip after being conformed to the right fps
global frames # Total length of CLIP in frames

# Globals for final project
global projwidth # Project width in pixels, based on the largest found file
global projheight # Project height in pixels, based on the largest found file
global projframes # Total length of PROJECT in frames

# Algorithm Functions
def get_codec_name(video_file):
    try:
        probe = ffmpeg.probe(video_file, v='error', show_entries='stream=codec_name', format='json')
        for stream in probe['streams']:
            codec_name = stream.get('codec_name')
            if codec_name:
                return codec_name
        return "UNKNOWN CODEC"
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode()}")
        return []

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

def count_items(vr: int, va: int, ir: int, ia: int):
    match(va, vr):
        case (0, 0):
            avantutils.iterate(0.8, 0.025, *f"VIDEO: No (usable) videofiles found in Video folder. Skipped.")
        case (va, vr) if va == vr:
            avantutils.iterate(0.8, 0.025, *f"VIDEO: All {va} videofiles in the Video folder can be analyzed.")
        case _:
            avantutils.iterate(0.8, 0.025, *f"VIDEO: Out of the {va} videofiles found, {vr} files can be analyzed.")
    match(ia, ir):
        case (0, 0):
            avantutils.iterate(0.8, 0.025, *f"IMG SEQUENCES: No (usable) image sequences found in Image Sequence folder. Skipped.")
        case (ia, ir) if ia == ir:
            avantutils.iterate(0.8, 0.025, *f"IMG SEQUENCES: All {va} image sequences in the Image Sequence folder can be analyzed.")
        case _:
            avantutils.iterate(0.8, 0.025, *f"IMG SEQUENCES: Out of the {va} image sequences found, {vr} sequences can be analyzed.")
    if all(x == 0 for x in [vr, va, ia, ir]):
        avantutils.iterate(0.8, 0.925, *avantxt.no_files)
        avantutils.wait_and_clear(1)
        avantutils.ex()

# WORK IN PROGRESS: NEED TO FIND WAYS TO ANALYZE IMAGE SEQUENCES AS WELL!
# VIDEO WORKS RN
def analyze_footage(vpa: str, ipa: str): # video path, image path
    global containers
    global filenames
    global codecs
    global framerates
    global widths
    global heights
    global durations
    global newlength
    global frames
    global projwidth
    global projheight
    v_r_count = 0
    v_a_count = 0 
    i_r_count = 0 
    i_a_count = 0 
    projwidth = 0
    projheight = 0
    containers = []
    filenames = []
    codecs = []
    framerates = []
    widths = []
    heights = []
    durations = []
    newlength = []
    frames = []
    v_items = os.listdir(vpa) # video items
    i_items = os.listdir(ipa) # image items
    v_a_count = sum(1 for item in v_items if os.path.isfile(os.path.join(vpa, item)))
    video_extensions = ['*.mp4', '*.avi', '*.mxf', '*.mov', '*.m4v', '*.m2v', '*.flv', '*.mkv', '*.wmv', '*.webm', '*.mpg']
    for extension in video_extensions:
        for video_file in glob.glob(os.path.join(vpa, extension)):
            try:
                clip = VideoFileClip(video_file)
                containers.append(video_file.split('.')[-1])
                filenames.append(os.path.basename(video_file))
                codecs.append(get_codec_name(video_file))
                framerates.append(clip.fps)
                widths.append(clip.size[0])
                heights.append(clip.size[1])
                durations.append(clip.duration)
                v_r_count += 1
                if clip.size[0] > projwidth:
                    projwidth = clip.size[0]
                if clip.size[1] > projheight:
                    projheight = clip.size[1]
            except Exception as e:
                print(f"ERROR while processing {video_file}: {e}")
    count_items(v_r_count, v_a_count, i_r_count, i_a_count)
    avantutils.iterate(0.8, 0.025, *"Converting obtained data to fit project's framerate...")
    for clip, x in enumerate(containers, filenames, codecs, framerates, widths, heights, durations):
        if (float(framerates[x]) == framerate):
            newlength.append("Same Framerate as project")
            frames.append(int(framerates[x] * durations[x]))
        if (float(framerates[x]) != framerate):
            orig = int(framerates[x] * durations[x])
            new_dur = float(orig / framerate)
            newlength.append(new_dur)
            frames.append(int(new_dur * framerate))
    avantutils.iterate(0.8, 0.025, *"Conversion completed.")
    avantutils.iterate(0.8, 0.025, *f"Avant will assume videoproject dimensions based on the videofile with the highest resolution found.")
    avantutils.iterate(0.8, 0.025, *f"In this case, your project will be using a resolution of {projwidth} x {projheight} pixels. You can manually change this later inside your NLE.")

def lengthselector():
    global projframes
    projframes = 0
    avantutils.wait_and_clear(1)
    avantutils.iterate(0.8, 0.025, *"Please input your preferred length of your video in full minutes. (f.e. 2.30, 3.01, 0.45, 4.00 or 110.45)")
    avantutils.iterate(0.8, 0.025, *f'If you are fine with Avant randomizing the length of your film, type "r", followed by your preferred MAXIMUM amount of minutes, f.e. r45, r110, r1, r25')
    while True:
        user_input = input("")
        # If user input cannot be converted to float
        if user_input is not float(user_input):
            print()
            avantutils.iterate(0.8, 0.025, *"Your input cannot convert to a float. Please try again.")
            continue
        # If user input is incorrectly formatted
        if "," in user_input:
            print()
            avantutils.iterate(0.8, 0.025, *"You did not define a proper length. (Did you use a comma instead of a period?)")
            continue
        # If user specifies 'R' mode.
        if str(user_input[0].upper()) is "R":
            if "," in user_input or "." in user_input:
                print()
                avantutils.iterate(0.8, 0.025, *"Since you are using the randomizer, you can only define FULL minutes, such as 'r23' or 'R2. Float entries such as R2.34 or R11.44 are not supported.")
                continue
            if int(user_input[1]) == 0:
                print()
                avantutils.iterate(0.8, 0.025, *"You did not properly declare the randomized max length. You cannot use '0' as the first integer.")
                continue
            if len(user_input.upper().split("R")) > 3:
                print()
                avantutils.iterate(0.8, 0.25, *"You tried to declare a length longer than 999 minutes. Please try again")
                continue
            random_minutes = random.randint(1, )
            break
        # Else, if user wants to specify their own exact length
        else:
            if float(user_input):
                minutes, seconds = user_input.split(".")
                if len(minutes.split("") <= 3):
                    minutesList = []
                    for digit in minutes:
                        minutesList.append(digit)
                    if int(minutesList[0]) == 0 and int(minutesList[1]) >= 0:
                        avantutils.iterate(0.8, 0.025, *"If the first integer is zero, there can not be a second integer. Combinations such as 02.45, 08.22 are not supported. They must be declared as 2.45 and 8.22.")
                        continue
                
       

 
def prod_mode():
    print("production mode started")

def post_mode():
    avantutils.clear()
    avantutils.wait(1)
    now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    doc_path = platformdirs.user_documents_dir()
    project_dir = os.path.join(doc_path, "Avant", f"POST | {projectname} - {framerate} fps | {now}")
    video_path = os.path.join(project_dir, "Footage")
    img_path = os.path.join(project_dir, "Image Sequences")
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
        analyze_footage(video_path, img_path)
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