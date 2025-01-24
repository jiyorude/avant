try:
    import inquirer, pyfiglet, sys, textwrap, os, stat
    import utils.texts as avantxt
    import tkinter as tk
    from tkinter import filedialog
    from utils.utilities import Utilities
    from utils.mapgen import MapGen
    from utils.demogen import DemoGen
    from utils.mmeprojgen import MMEProjGen
    from utils.editorgen import NLEGen
except ImportError as err:
    sys.exit(f"ERR004: SYSTEM unable to reach critical libraries => => {err}")

class System:
    UTILITIES, MAPGEN, DEMOGEN, MMEPROJGEN, NLEGEN = Utilities(), MapGen(), DemoGen(), MMEProjGen(), NLEGen()

    def init(self):
        figlet_text = pyfiglet.figlet_format("AVANT", font="slant").split('\n')
        for line in figlet_text:
            self.UTILITIES.iterate(0.1, 0.015, *line)
        self.UTILITIES.iterate(0.8, 0.025, *avantxt.init_one)
        self.UTILITIES.iterate(0.8, 0.025, *avantxt.init_two)
        self.UTILITIES.print_whitespace()
        self.UTILITIES.iterate(0.8, 0.025, *avantxt.init_three)
        self.UTILITIES.wait_and_clear(2)

    def main_menu(self):
        self.UTILITIES.wait(1)
        print(pyfiglet.figlet_format("AVANT", font="slant"))
        main_menu = [inquirer.List('choice', message="Main Menu", choices=[
            avantxt.main_one,
            avantxt.main_two,
            avantxt.main_three,
            avantxt.main_four,
            avantxt.main_five,
            avantxt.main_six,
            avantxt.main_seven,
            avantxt.main_eight
        ])]
        show_main_menu = inquirer.prompt(main_menu)
        if show_main_menu is None:
            return 8
        selection = show_main_menu['choice']
        match (selection):
            case avantxt.main_one:
                return 1
            case avantxt.main_two:
                return 2
            case avantxt.main_three:
                return 3
            case avantxt.main_four:
                return 4
            case avantxt.main_five:
                return 5
            case avantxt.main_six:
                return 6
            case avantxt.main_seven:
                return 7
            case avantxt.main_eight:
                return 8

    def folder_structure_check(self):
        try:
            if not os.path.exists(os.path.join(os.path.expanduser('~/Documents'), 'Avant')):
                os.makedirs(os.path.join(os.path.expanduser('~/Documents'), 'Avant'))
                with open(os.path.join(os.path.expanduser('~/Documents/Avant'), '_Avant_Documentation.url'), 'w') as file:
                    file.write(f"[InternetShortcut]\nURL=https://avant-docs.vercel.app")
        except Exception as e:
            exit(1, f"ERR005: Exception arose while generating Avant folder structure: {e}")

    def check_q3_installation(self):
        if not os.path.isfile(os.path.join(os.path.expanduser("~/Documents/Avant"), "._avant_data")):
            self.UTILITIES.wait(1), print(pyfiglet.figlet_format("SETUP", font="slant"))
            self.UTILITIES.wait(1), self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_one), self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_two)
            self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_three), self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_four), self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_five)
            self.UTILITIES.wait(2), self.UTILITIES.clear()
            root = tk.Tk(), root.withdraw()
            folder_path = filedialog.askdirectory(initialdir="C:/Program Files")
            if folder_path is None:
                self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_six), self.UTILITIES.wait_and_clear(1)
                sys.exit(0)
            else:
                QUAKE_FOUND, PAKZERO_FOUND, MME_FOUND = False, False, False
                self.UTILITIES.iterate(0.8, 0.025, *f"Analyzing {folder_path}...")
                if os.path.isfile(os.path.join(folder_path, "quake3.exe")):
                    QUAKE_FOUND = True
                    self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_seven)
                    EXE_PATH = os.path.join(folder_path, "quake3.exe")
                if os.path.isdir(os.path.join(folder_path, "baseq3")):
                    if os.path.isfile(os.path.join(folder_path, "baseq3", "pak0.pk3")):
                        PAKZERO_FOUND = True
                        for x in range(0, 10):
                            if not os.path.isfile(os.path.join(folder_path, "baseq3", f"pak{x}.pk3")):
                                PAKZERO_FOUND = False
                                break
                    if PAKZERO_FOUND:
                        self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_eight)
                        PAKZERO_PATH = os.path.join(folder_path, "baseq3", "pak0.pk3")
                if os.path.isdir(os.path.join(folder_path, "mme")):
                    if os.path.isfile(os.path.join(folder_path, "quake3mme.exe")) and os.path.isfile(os.path.join(folder_path, "start q3mme.cmd")):
                        if all(os.path.isfile(os.path.join(folder_path, "mme", file)) for file in ["autoexec.cfg", "mmedemos.cfg", "uix86.dll", "qagamex86.dll", "cgamex86.dll"]):
                            if all(os.path.isfile(os.path.join(folder_path, "mme", "scripts", file)) for file in ["base_weapons.fx", "mme.shader", "base_player.fx", "base_extra.fx"]):
                                MME_FOUND = True
                                self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_nine)
                                MME_PATH = os.path.join(folder_path, "mme")
                if all([QUAKE_FOUND, PAKZERO_FOUND, MME_FOUND]):
                    with open(os.path.join(os.path.expanduser("~/Documents/Avant"), ".avant_data"), "w") as file:
                        file.write(EXE_PATH), file.write(PAKZERO_PATH), file.write(MME_PATH)
                        os.system(f'attrib +h"{os.path.join(os.path.expanduser("~/Documents/Avant"), ".avant_data")}"')
                        os.chmod(os.path.join(os.path.expanduser("~/Documents/Avant"), ".avant_data"), stat.S_IRUSR | stat.S_IWUSR)
                    self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_ten), self.utilities.wait_and_clear(2)
                else:
                    self.UTILITIES.clear()
                    if not QUAKE_FOUND:
                        self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_eleven)
                    if not PAKZERO_FOUND:
                        self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_twelve)
                    if not MME_FOUND:
                        self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_thirteen)
                    self.UTILITIES.wait(2), self.UTILITIES.print_whitespace(), self.UTILITIES.iterate(0.8, 0.025, *avantxt.setup_fourteen)
                    self.UTILITIES.wait(2), self.UTILITIES.clear(), sys.exit(1)
        else:
            # Keep checking at every boot if all files are still present.
            # Nothing wrong, boot as normal, if something's missing, iterate a new text welcome back, seems something has changed with ....

    def manage_avant_projects(self):
        self.UTILITIES.clear()
        print("MANAGE AVANT PROJECT...")
        self.UTILITIES.wait(2)
        self.UTILITIES.clear()
        return True

    def gen_map_data(self):
        self.UTILITIES.clear()
        print("GENERATE MAP DATA")
        self.UTILITIES.wait(2)
        self.UTILITIES.clear()
        return True

    def gen_demo_files(self):
        self.UTILITIES.clear()
        print("GENERATE DEMO DATA")
        self.UTILITIES.wait(2)
        self.UTILITIES.clear()
        return True

    def gen_mme_projs(self):
        self.UTILITIES.clear()
        print("GENERATE MME PROJECTS")
        self.UTILITIES.wait(2)
        self.UTILITIES.clear()
        return True

    def gen_nle_data(self):
        self.UTILITIES.clear()
        print("GENERATE NLE DATA")
        self.UTILITIES.wait(2)
        self.UTILITIES.clear()
        return True

    def show_credits(self):
        texts = [avantxt.credits_one, avantxt.credits_two, avantxt.credits_three, avantxt.credits_four, avantxt.credits_five, avantxt.credits_six, avantxt.credits_seven, avantxt.credits_eight, avantxt.credits_nine, avantxt.credits_ten, avantxt.credits_eleven, avantxt.credits_twelve, avantxt.credits_thirteen]
        wait_at = [3, 7, 10]
        self.UTILITIES.clear(), self.UTILITIES.wait(1)
        print(pyfiglet.figlet_format("CREDITS", font="slant")), self.UTILITIES.wait(1)
        for x, text in enumerate(texts, start=1):
            print(textwrap.fill(text, width=100))
            if x == 12:
                self.UTILITIES.print_whitespace()
            if x in wait_at:
                self.UTILITIES.wait(1), self.UTILITIES.print_whitespace()
        self.UTILITIES.wait(1), self.UTILITIES.print_whitespace()
        input(f"{avantxt.credits_fourteen}\n\n")
        self.UTILITIES.clear()
        return True

    def how_to_use(self):
        texts = [avantxt.htu_one, avantxt.htu_two, avantxt.htu_three, avantxt.htu_four, avantxt.htu_five, avantxt.htu_six, avantxt.htu_seven, avantxt.htu_eight, avantxt.htu_nine, avantxt.htu_ten, avantxt.htu_eleven, avantxt.htu_twelve, avantxt.htu_thirteen]
        wait_at = [3, 5, 7, 9, 11]
        self.UTILITIES.clear(), self.UTILITIES.wait(1)
        print(pyfiglet.figlet_format("ABOUT", font="slant")), self.UTILITIES.wait(1)
        for x, text in enumerate(texts, start=1):
            print(textwrap.fill(text, width=75))
            if x in [1, 2]:
                self.UTILITIES.print_whitespace()
            if x in wait_at:
                self.UTILITIES.wait(3), self.UTILITIES.print_whitespace(), self.UTILITIES.print_whitespace()
        self.UTILITIES.wait(3), self.UTILITIES.print_whitespace()
        input(f"{avantxt.htu_fourteen}\n\n")
        self.UTILITIES.clear()
        return True

    def exit_avant(self):
        self.UTILITIES.clear(), self.UTILITIES.wait(0.5)
        self.UTILITIES.iterate(0.4, 0.025, *"Exiting...")
        self.UTILITIES.wait(1.5), self.UTILITIES.clear(), self.UTILITIES.kill("", 0)
