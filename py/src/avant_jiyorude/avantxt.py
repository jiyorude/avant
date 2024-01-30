search_fail = "No results. Please try again."
exit = "Exiting....\n"
i1 = "\n\nAVANT\n"
i2 = "Random-data generating algorithm for experimental Quake III machinima (post-) production" 
i3 = "Created by Jordy Veenstra / A Pixelated Point of View"
i4 = "\nVersion 0.1.0\n"
sc = "Succesfully connected to avant database\n"
se = "Could not connect to avant database"
start_algorithm = "Start Algorithm"
help = "Help"
credits = "Credits"
exit = "Exit"
exit_two = "\n\nExiting....\n"
cred = "\nAVANT\nRandom-data generating algorithm for experimental Quake III machinima (post-) production\nCreated by Jordy Veenstra / A Pixelated Point of View\n"
cred_2 = "LINKS/REPOSITORIES:\nGitHub: https://github.com/jiyorude/avant\nIssues: https://github.com/jiyorude/avant/issues\nBitBucket: https://bitbucket.org/appov/avant/src/main/\nPyPi (Python Version): T.B.A\nNPM (JavaScript/Node Version): T.B.A\nFront-End: T.B.A."
cred_3 = "\nSOFTWARE/MODULES - PYTHON VERSION:\nPython 3.11 (Python Software Foundation)\nPyMongo (MongoDB Python Team)\nInquirer (Miguel Ángel García)\nMatplotlib (John D. Hunter, Michael Droettboom)\nReportlab (Andy Robinson, Robin Becker)\nASCII Art Generator (patorjk)\nAvantlib (Jordy Veenstra)"
cred_4 = "\nSOFTWARE/MODULES - JAVASCRIPT/NODE VERSION:\nNode 21.1.0 (OpenJS Foundation)\nMongoDB (MongoDB Node.js Team)\nASCII Art Generator (patorjk)\nAvantlib (Jordy Veenstra)\n\n"
any = "Press ENTER\RETURN to return to the main menu...\n"
any2 = "SCROLL to read. Press ENTER\RETURN to go back..."
h1 = "Background"
h2 = "Algorithm Modes"
h3 = "How to Use"
h4 = "Data Interpretation and Usage"
h5 = "Troubleshooting"
h6 = "Changelog"
h7 = "License"
h8 = "Return to main menu"
bg_t = "\n\nBACKGROUND\n\n"
bg = "Avant is a Python and JavaScript algorithm that outputs random-generated data for the purpose of experimental, depth-based and randomized Quake III Arena machinima production. The algorithm outputs a list of various elements that correspond to various machinima (post-)production processes and parameters found within Quake III movie-making mods. Both Quake III MovieMakers Edition and WolfcamQL are fully supported by avant and offer a native moviemaking experience.\n\nTechnically speaking, avant is able to generate endless variations of potential experimental Quake III machinima films."
bg_2 = "The algorithm was named after the highly popular art movement avant-garde, as it outputs raw, randomized and unchecked data made for experimental productions. It is not until the actual production or post-production process that the user is able to see how the actual data is 'visualized'. The focus lies on film design and graphical representation, not on contents or story; thus staying in true avant-garde fashion.\n\n\n"
bg_3 = "Avant serves as the successor to the now defunct DOMINION algorithm and offers a number of quality of life improvements, such as:\n\n"
bg_4 = "* Full integration of a custom `lvlworld` map database.\n\n"
bg_5 = "* Avant is able to generate data for only the production process of experimental Quake III machinima, post-production, or even both.\n\n"
bg_6 = "* The algorithm can generate keywords and potential theme mash-ups for the creation of custom maps.\n\n"
bg_7 = "* DepthMap generation can now be turned on or off during the initial wizard.\n\n"
bg_8 = "* Data will be automatically saved to a pre-stylized PDF instead of a notepad file.\n"
bg_9 = "* You can now define whether you want to save all generated data to a PDF, or only the necessary info required for production/post-production.\n\n"
bg_10 = "* Additional parameters for the project, such as name, framerate, game and intro/outro length can now be set freely.\n\n\n"
bg_11 = "In short, Avant generates and outputs data for a number of elements found inside your Quake III Machinima project, such as:\n\n* Runtime: The total length of your film seconds and frames per second\n\n"
bg_12 = "* Maps: A list of randomized lvlworld map ID's and corresponding map names\n\n"
bg_13 = "* Custom Map Keywords: (Optional) - Only if you turned on custom-mode. Generates randomized input for inspirational purposes if you are planning to create custom maps for your project.\n\n"
bg_14 = "* Post-Production Flow: Generates a full edit-list containing the required shots (in conjunction with depthmap profiles if depth-mode is turned on) and their runtime. The list contains an automatic function that deletes excess frames if the total output exceeds the runtime limit.\n\n"
bg_15 = "* Shot Information: Provides information regarding the length of each of the selected shots, various parameters such as camera position, roll, yaw and field of view. In tandem, the algorithm also decides whether the shot contains camera animations, and if so, what the animation parameters are. The shots contained in this list will be used.\n\n"
bg_16 = "* Depth Information: If depth-mode is turned on, each shot provided in the shotlist will contain parameters for depthfocus and depthrange as well.\n\n"

ascii = """
      __      __       _   _  _______ 
     /\\ \    / //\    | \ | ||__   __|
    /  \\ \  / //  \   |  \| |   | |   
   / /\ \\ \/ // /\ \  | . ` |   | |   
  / ____ \\  // ____ \ | |\  |   | |   
 /_/    \_\\//_/    \_\|_| \_|   |_|
 """

ascii_help = """
  _    _  ______  _       _____  
 | |  | ||  ____|| |     |  __ \ 
 | |__| || |__   | |     | |__) |
 |  __  ||  __|  | |     |  ___/ 
 | |  | || |____ | |____ | |     
 |_|  |_||______||______||_| 
"""

ascii_credits = """
   _____  _____   ______  _____  _____  _______  _____ 
  / ____||  __ \ |  ____||  __ \|_   _||__   __|/ ____|
 | |     | |__) || |__   | |  | | | |     | |  | (___  
 | |     |  _  / |  __|  | |  | | | |     | |   \___ \ 
 | |____ | | \ \ | |____ | |__| |_| |_    | |   ____) |
  \_____||_|  \_\|______||_____/|_____|   |_|  |_____/ 
"""

ascii_bye = """
   _____ __     __        _ 
  / ____|\ \   / / /\    | |
 | |      \ \_/ / /  \   | |
 | |       \   / / /\ \  | |
 | |____    | | / ____ \ |_|
  \_____|   |_|/_/    \_\(_)
"""

ascii_background = """
  ____            _____  _  __ _____  _____    ____   _    _  _   _  _____  
 |  _ \    /\    / ____|| |/ // ____||  __ \  / __ \ | |  | || \ | ||  __ \ 
 | |_) |  /  \  | |     | ' /| |  __ | |__) || |  | || |  | ||  \| || |  | |
 |  _ <  / /\ \ | |     |  < | | |_ ||  _  / | |  | || |  | || . ` || |  | |
 | |_) |/ ____ \| |____ | . \| |__| || | \ \ | |__| || |__| || |\  || |__| |
 |____//_/    \_\\_____||_|\_\\_____||_|  \_\ \____/  \____/ |_| \_||_____/ 
"""

ascii_algorithm_modes = """
            _       _____   ____   _____   _____  _______  _    _  __  __ 
     /\    | |     / ____| / __ \ |  __ \ |_   _||__   __|| |  | ||  \/  |
    /  \   | |    | |  __ | |  | || |__) |  | |     | |   | |__| || \  / |
   / /\ \  | |    | | |_ || |  | ||  _  /   | |     | |   |  __  || |\/| |
  / ____ \ | |____| |__| || |__| || | \ \  _| |_    | |   | |  | || |  | |
 /_/    \_\|______|\_____| \____/ |_|  \_\|_____|   |_|   |_|  |_||_|  |_|
  __  __   ____   _____   ______   _____                                  
 |  \/  | / __ \ |  __ \ |  ____| / ____|
 | \  / || |  | || |  | || |__   | (___  
 | |\/| || |  | || |  | ||  __|   \___ \ 
 | |  | || |__| || |__| || |____  ____) |
 |_|  |_| \____/ |_____/ |______||_____/ 
"""

ascii_howtouse = """
  _    _   ____ __          __  _______  ____    _    _   _____  ______ 
 | |  | | / __ \\ \        / / |__   __|/ __ \  | |  | | / ____||  ____|
 | |__| || |  | |\ \  /\  / /     | |  | |  | | | |  | || (___  | |__   
 |  __  || |  | | \ \/  \/ /      | |  | |  | | | |  | | \___ \ |  __|  
 | |  | || |__| |  \  /\  /       | |  | |__| | | |__| | ____) || |____ 
 |_|  |_| \____/    \/  \/        |_|   \____/   \____/ |_____/ |______|
"""

ascii_usage = """
  _____         _______          _    _   _____           _____  ______ 
 |  __ \    /\ |__   __| /\     | |  | | / ____|   /\    / ____||  ____|
 | |  | |  /  \   | |   /  \    | |  | || (___    /  \  | |  __ | |__   
 | |  | | / /\ \  | |  / /\ \   | |  | | \___ \  / /\ \ | | |_ ||  __|  
 | |__| |/ ____ \ | | / ____ \  | |__| | ____) |/ ____ \| |__| || |____ 
 |_____//_/    \_\|_|/_/    \_\  \____/ |_____//_/    \_\\_____||______|
"""

ascii_troubleshooting = """
  _______  _____    ____   _    _  ____   _       ______  
 |__   __||  __ \  / __ \ | |  | ||  _ \ | |     |  ____|
    | |   | |__) || |  | || |  | || |_) || |     | |__   
    | |   |  _  / | |  | || |  | ||  _ < | |     |  __|  
    | |   | | \ \ | |__| || |__| || |_) || |____ | |____
    |_|   |_|  \_\ \____/  \____/ |____/ |______||______|
   _____  _    _   ____    ____  _______  _____  _   _   _____ 
  / ____|| |  | | / __ \  / __ \|__   __||_   _|| \ | | / ____|
 | (___  | |__| || |  | || |  | |  | |     | |  |  \| || |  __ 
  \___ \ |  __  || |  | || |  | |  | |     | |  | . ` || | |_ |
  ____) || |  | || |__| || |__| |  | |    _| |_ | |\  || |__| |
 |_____/ |_|  |_| \____/  \____/   |_|   |_____||_| \_| \_____|
"""

ascii_changelog = """
   _____  _    _            _   _   _____  ______  _       ____    _____ 
  / ____|| |  | |    /\    | \ | | / ____||  ____|| |     / __ \  / ____|
 | |     | |__| |   /  \   |  \| || |  __ | |__   | |    | |  | || |  __ 
 | |     |  __  |  / /\ \  | . ` || | |_ ||  __|  | |    | |  | || | |_ |
 | |____ | |  | | / ____ \ | |\  || |__| || |____ | |____| |__| || |__| |
  \_____||_|  |_|/_/    \_\|_| \_| \_____||______||______|\____/  \_____|
"""

ascii_license = """
  _       _____  _____  ______  _   _   _____  ______ 
 | |     |_   _|/ ____||  ____|| \ | | / ____||  ____|
 | |       | | | |     | |__   |  \| || (___  | |__   
 | |       | | | |     |  __|  | . ` | \___ \ |  __|  
 | |____  _| |_| |____ | |____ | |\  | ____) || |____ 
 |______||_____|\_____||______||_| \_||_____/ |______|
"""