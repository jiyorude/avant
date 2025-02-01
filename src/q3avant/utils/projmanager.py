import os, pyfiglet, inquirer, shutil
from datetime import datetime
from utils.utilities import Utilities
import utils.texts as avantxt

class ProjectManager():
    def __init__(self):
        self.UTILITIES = Utilities()

    def show_projects(self):
        self.UTILITIES.wait_and_clear(1)
        print(pyfiglet.figlet_format("Overview", font="slant"))
        for folder in os.listdir(os.path.join(os.path.expanduser("~"), "Documents", "Avant")):
            if os.path.isdir(os.path.join(os.path.expanduser("~"), "Documents", "Avant", folder)):
                print(f"* {folder}")
        self.UTILITIES.wait(1), self.UTILITIES.print_whitespace()
        input(f"{avantxt.proj_seven}")
        self.UTILITIES.clear()
        return True

    def delete_project(self):
        while True:
            self.UTILITIES.wait_and_clear(1)
            print(pyfiglet.figlet_format("Delete", font="slant"))
            folders = [f for f in os.listdir(os.path.join(os.path.expanduser("~"), "Documents", "Avant")) if os.path.isdir(os.path.join(os.path.expanduser("~"), "Documents", "Avant", f))]
            folders.append("Return to Project Manager")
            deletion = [inquirer.List('folder', message="Select a project to delete...", choices=folders)]
            folder_delete_choice = inquirer.prompt(deletion)
            selected_folder = folder_delete_choice['folder']
            if selected_folder == "Return to Project Manager":
                break
            if selected_folder:
                self.UTILITIES.clear()
                print(pyfiglet.figlet_format("Confirm", font="slant"))
                self.UTILITIES.iterate(0.8, 0.025, *f"Are you sure you want to delete project {selected_folder}?")
                confirmation = [inquirer.List('confirmation', choices = ["Yes", "No"])]
                confirmation_choice = inquirer.prompt(confirmation)
                selected_confirmation_choice = confirmation_choice['confirmation']
                match (selected_confirmation_choice):
                    case "Yes":
                        shutil.rmtree(os.path.join(os.path.expanduser("~"), "Documents", "Avant", selected_folder))
                    case "No":
                        pass
        return True

    def modify_project(self):
        while True:
            try:
                self.UTILITIES.wait_and_clear(1)
                print(pyfiglet.figlet_format("Modify", font="slant"))
                folders = [f for f in os.listdir(os.path.join(os.path.expanduser("~"), "Documents", "Avant")) if os.path.isdir(os.path.join(os.path.expanduser("~"), "Documents", "Avant", f))]
                folders.append("Return to Project Manager")
                modification = [inquirer.List('folder', message="Select a project to modify...", choices=folders)]
                folder_modification_choice = inquirer.prompt(modification)
                selected_folder = folder_modification_choice['folder']
                if selected_folder == "Return to Project Manager":
                    break
                if selected_folder:
                    self.UTILITIES.clear()
                    print(pyfiglet.figlet_format("New Name", font="slant"))
                    folder_name = input("What is your new project name (max 50 chars): ").strip()
                    if len(folder_name) > 50:
                        raise Exception(*avantxt.proj_one)
                    elif not folder_name:
                        break
                    else:
                        project_name = folder_name
                        folder_name = folder_name.replace(" ", "_") + " " + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            except Exception as e:
                self.UTILITIES.iterate(0.8, 0.025, *str(e))
                pass
            else:
                os.rename(os.path.join(os.path.expanduser("~"), "Documents", "Avant", selected_folder), os.path.join(os.path.expanduser("~"), "Documents", "Avant", folder_name))
                self.UTILITIES.print_whitespace(), self.UTILITIES.iterate(0.8, 0.025, *f"Project succesfully renamed to {project_name}!")
                self.UTILITIES.wait_and_clear(2)
                break
        return True

    def create_project(self):
        while True:
            try:
                self.UTILITIES.wait_and_clear(1), print(pyfiglet.figlet_format("Create Project", font="slant"))
                folder_name = input("Please name your project (max 50 chars): ").strip()
                if len(folder_name) > 50:
                    raise Exception(*avantxt.proj_one)
                elif not folder_name:
                    break
                else:
                    project_name = folder_name
                    folder_name = folder_name.replace(" ", "_") + " " + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            except Exception as e:
                self.UTILITIES.iterate(0.8, 0.025, *str(e))
                pass
            else:
                if os.path.exists(os.path.join(os.path.expanduser("~"), "Documents", "Avant", f"{folder_name}")):
                    self.UTILITIES.print_whitespace(), self.UTILITIES.iterate(0.8, 0.025, *f"Project {project_name} already exists! Folder creation cancelled.")
                else:
                    os.makedirs(os.path.join(os.path.expanduser("~"), "Documents", "Avant", f"{folder_name}"))
                    for folder in ["_001_MAP_INPUT", "_002_MAP_OUTPUT", "_003_DEMO_OUTPUT", "_004_MME_INPUT", "_005_MME_OUTPUT", "_006_NLE_OUTPUT"]:
                        os.makedirs(os.path.join(os.path.expanduser("~"), "Documents", "Avant", f"{folder_name}", f"{folder}"))
                    self.UTILITIES.print_whitespace(), self.UTILITIES.iterate(0.8, 0.025, *f"Project {project_name} succesfully created!")
                    self.UTILITIES.wait_and_clear(2)
                    break
        return True
