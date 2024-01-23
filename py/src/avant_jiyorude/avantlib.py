import time

def iterate(bdel: int, *str: str):
    time.sleep(bdel)
    for char in str:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

def init():
    i1 = "AVANT"
    i2 = "Random-data generating algorithm for experimental, Quake III machinima (post-) production" 
    i3 = "Created by Jordy Veenstra / A Pixelated Point of View"
    i4 = "Version 0.0.1"
    iterate(0.4, *i1), iterate(0.4, *i2), iterate(0.4, *i3)

init()