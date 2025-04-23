import zipfile
import os
import shutil
import sys
import os
import json
import inquirer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bsp_tool

class MapGen:
    # Assign output to new variable
    def select_project(self):
        folders = [f for f in os.listdir(os.path.join(os.path.expanduser("~"), "Documents", "Avant")) if os.path.isdir(os.path.join(os.path.expanduser("~"), "Documents", "Avant", f))]
        select_folder = [inquirer.List('folder', message="Select Project", choices=folders)]
        select_folder_choice = inquirer.prompt(select_folder)
        selected_folder = select_folder_choice['folder']
        return os.path.join(os.path.expanduser("~"), "Documents", "Avant", selected_folder)

    def extract_bsp(self, pk3_path: str, temp_dir="temp_maps"):
        pk3_name = os.path.basename(pk3_path)
        try:
            with zipfile.ZipFile(pk3_path, 'r') as zip_ref:
                bsp_files = [file for file in zip_ref.namelist() if file.lower().endswith(".bsp")]
                if not bsp_files:
                    print("..No BSP files found. Skipping...")
                    return False
                print(f"...Extracting {len(bsp_files)} BSP file(s) from PK3 archive.")
                os.makedirs(temp_dir, exist_ok=True)
                custom_output_dir = "BSP_FILES"
                os.makedirs(custom_output_dir, exist_ok=True)
                for bsp in bsp_files:
                    zip_ref.extract(bsp, temp_dir)
                    print(f"...{bsp} successfully extracted from PK3!")
                    bsp_path = os.path.join(temp_dir, bsp)
                    destination_path = os.path.join(custom_output_dir, os.path.basename(bsp))
                    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                    shutil.move(bsp_path, destination_path)
                return True
        except zipfile.BadZipFile as e:
            print(f"ERR012: Unable to extract {pk3_name}: {e}")
            return False
        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

    def load_bsp(self, bsp_path: str):
        return bsp_tool.load_bsp(bsp_path)

    # Check for additional entities with new maps from different gamemodes.
    def analyze_entities(self, bsp_var):
        origin = []
        angle = []
        for entity in bsp_var.ENTITIES:
            if entity.get('classname') == 'info_player_deathmatch':
                origin.append(entity['origin'])
                angle.append(entity['angle'])
        return origin, angle

    def get_world_size(self, bsp_var):
        world_model = bsp_var.models[0]
        min_x, min_y, min_z = world_model.min
        max_x, max_y, max_z = world_model.max
        world_data = [min_x, max_x, min_y, max_y, min_z, max_z]
        return world_data

    # Uses origin and angle lists and returns a spawnpoint for PDF and json data for demogen
    def get_spawnpoint_data(self, origin, angle, world_data):
        spawnpoint_data = [f"Map Dimensions - Min X: {world_data[0]}, Max X: {world_data[1]}, Min Y: {world_data[2]}, Max Y: {world_data[3]}, Min Z: {world_data[4]}, Max Z: {world_data[5]}"]
        json_data = list(world_data)
        for i, (origin_entry, angle_entry) in enumerate(zip(origin, angle)):
            x, y, z = origin_entry.split(" ")
            spawnpoint_data.append(f"Spawnpoint {i} - Position X: {x}, Position Y: {y}, Position Z: {z}, Angle: {angle_entry}")
            json_data.append(i, x, y, z, angle_entry)
        return spawnpoint_data, json_data

    # Calculates the total map space, and available movable space for each spawn point
    # Proceeds to add these to the spawnpoint and jsondata lists.
    # Finalizes by converting these to tuples for save_json func
    def calculate_camera_void_space(self, json_data):
        new_json_data = []
        world_data = self.world_data
        for x, data in enumerate(json_data):
            available_x = 0
            available_y = 0
            available_z = 0
            splitted = data.split(",")
            if len(splitted) == 6:
                width = float(splitted[1]) - float(splitted[0])
                height = float(splitted[3]) - float(splitted[2])
                depth = float(splitted[5]) - float(splitted[4])
                # X-Axis calculation
                if float(splitted[0]) <= world_data[0]:
                    available_x = min(width, world_data[1] - float(splitted[0]))
                elif float(splitted[1]) >= world_data[1]:
                    available_x = -min(width, float(splitted[1]) - world_data[0])
                else:
                    available_x = min(width, world_data[1] - float(splitted[0]), float(splitted[0]) - world_data[0])
                # Y-Axis calculation
                if float(splitted[2]) <= world_data[2]:
                    available_y = min(height, world_data[3] - float(splitted[2]))
                elif float(splitted[3]) >= world_data[3]:
                    available_y = -min(height, float(splitted[3]) - world_data[2])
                else:
                    available_y = min(height, world_data[3] - float(splitted[2]), float(splitted[2]) - world_data[2])
                # Z-Axis calculation
                if float(splitted[4]) <= world_data[4]:
                    available_z = min(depth, world_data[5] - float(splitted[4]))
                elif float(splitted[5]) >= world_data[5]:
                    available_z = -min(depth, float(splitted[5]) - world_data[4])
                else:
                    available_z = min(depth, world_data[5] - float(splitted[4]), float(splitted[4]) - world_data[4])
                new_json_data.append(x, available_x, available_y, available_z)
                return new_json_data
            else:
                return None

    def save_json(self, dataset, output):
        with open(output, 'a') as json_file:
            json.dump(list(map(tuple, dataset)), json_file, indent=4)

    def generate_data_pdf(self):
        # Use reportlab to create a PDF with the information, including a 3D Graph and place it in the folder.
        pass

# Test locally (not in codespace)
test = MapGen()
test.extract_bsp("ironwood.pk3")
bsp_path = os.path.join("BSP_FILES", "ironwood.bsp")
bsp_data = test.load_bsp(bsp_path)

