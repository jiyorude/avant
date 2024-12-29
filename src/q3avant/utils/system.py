# Main System functions such as main menu etc.

try:
    import inquirer, pyfiglet, sys
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
        self.UTILITIES.iterate(0.8, 0.025, *"Random Data Generating Algorithm for Experimental Quake III Machinima Production.")
        self.UTILITIES.iterate(0.8, 0.025, *"Made by Jordy Veenstra (A Pixelated Point of View)")
        self.UTILITIES.iterate(0.8, 0.025, *"Version 0.0.0 - December 2024")
        self.UTILITIES.wait_and_clear(2)

    def main_menu(self):
        self.UTILITIES.wait(1)
        print(pyfiglet.figlet_format("AVANT", font="slant"))
        main_menu = [inquirer.List('choice', message="Main Menu", choices=[
            "Generate Map Data",
            "Generate Demo Files",
            "Generate MME Project Files",
            "Generate EDL/XML",
            "About Avant",
            "Credits",
            "Exit"
        ])]
        show_main_menu = inquirer.prompt(main_menu)
        if show_main_menu is None:
            return 7
        selection = show_main_menu['choice']
        match (selection):
            case "Generate Map Data":
                return 1
            case "Generate Demo Files":
                return 2
            case "Generate MME Project Files":
                return 3
            case "Generate EDL/XML":
                return 4
            case "About Avant":
                return 5
            case "Credits":
                return 6
            case "Exit":
                return 7

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
        self.UTILITIES.clear()
        print("SHOW CREDITS")
        self.UTILITIES.wait(2)
        self.UTILITIES.clear()
        return True

    def how_to_use(self):
        self.UTILITIES.clear()
        print("ABOUT/HTU")
        self.UTILITIES.wait(2)
        self.UTILITIES.clear()
        return True

    def exit_avant(self):
        self.UTILITIES.clear()
        self.UTILITIES.wait(0.5)
        self.UTILITIES.iterate(0.4, 0.025, *"Exiting...")
        self.UTILITIES.wait(1.5)
        self.UTILITIES.clear()
        self.UTILITIES.kill("", 0)

