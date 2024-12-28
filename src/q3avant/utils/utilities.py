# Reusable Utility Functions
import sys, time, os
from datetime import datetime

class Utilities():
    def clear(self):
        return os.system('cls' if os.name == 'nt' else 'clear')

    def kill(self, message: str = None, exit_code: int = 1):
        if exit_code not in [0, 1]:
            sys.exit("Termination of application only possible with exit code 0 or 1.")
        if message:
            print(message)
        sys.exit(exit_code)

    def wait(self, sec: float):
        if not float(sec) or sec < 0:
            sys.exit("Cannot leave wait function empty or execute negative function call.")
        return time.sleep(sec)

    def wait_and_clear(self, x: int):
        time.sleep(x)
        return os.system('cls' if os.name == 'nt' else 'clear')

    def iterate(self, init_del: float, type_del: float, *message: str):
        time.sleep(init_del)
        for char in message:
            print(char, end='', flush=True)
            time.sleep(type_del)
        print()

    def get_time(self):
        time_string = datetime.now().strftime("%A %d %B %Y %H %M %S")
        return time_string.split()
