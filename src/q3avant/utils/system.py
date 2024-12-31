try:
    import inquirer, pyfiglet, sys, textwrap
    import utils.texts as avantxt
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
        # If folder structure does not exist, create it in Documents plus shortcut to docs.
        pass

    def check_q3_installation(self):
        # Only during first boot, verify q3 installation and create a hidden file.
        # During each boot, check if file is still there
        pass

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