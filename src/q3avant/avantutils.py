import os
import time
import sys
from datetime import datetime
import avantxt

def print_ascii():
    for line in avantxt.ascii.splitlines():
        iterate(0.1, 0.010, *line)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(int: int):
    time.sleep(int)

def double_print():
    return print(), print()

def progress(int: int):
    print(f"{int}%", end='\r')

def terminate(int: int):
    print(f"Avant cannot connect to-/ or find any database. Terminating in {int} seconds", end='\r')

def iterate(bdel: int, tdel: float, *str: any):
    wait(bdel)
    for char in str:
        print(char, end='', flush=True)
        wait(tdel)
    print()

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

def exception(err: any, x: int):
    clear()
    print()
    iterate(0.4, 0.025, f"An error occurred: {err}.\n")
    for y in range(x, -1, -1):
        terminateAlt(y)
        wait(1)
    clear()
    sys.exit(0)

def ex():
    clear()
    wait(0.5)
    print()
    iterate(0.5, 0.025, *avantxt.exit_two)
    wait(1.5)
    clear()
    wait(0.5)
    sys.exit(0)

def wait_and_clear(x: int):
    wait(x)
    clear()