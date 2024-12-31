### Avant
Random-data generating Algorithm for experimental,<br>
Quake III Machinima (post-)production
<br/>


<br/>

**Version: 0.2.4**
<br/><br/>
Created by Jordy Veenstra (A Pixelated Point of View)<br/>

<br/>

****

### Table of Contents

* [Background](#background)
* [Documentation](#documentation)
* [Installation](#installation)
* [How to Use](#how-to-use)
* [License](#license)

<br/>

****

### Background
Avant is a <code>Python-based CLI tool</code> designed to simplify the creation of experimental Quake III Machinima films. Originally developed as a tool for my machinima label "A Pixelated Point of View," Avant’s main function is to generate random, experimental Quake III Arena compositions while automating much of the production process. Technically speaking, Avant allows for the generation of practically unlimited variations of potential experimental Quake III machinima films.

Avant was named after the highly popular art movement *'avant-garde'*, as it outputs raw, randomized and basically unchecked film data for the primary purpose of creating innovative, experimental and unconventional Quake III machinima films. It is not until the actual post-production process that the user is able to see how the generated data is visualized and captured. The films generated with avant focus on design, graphical representation, artistic expression and the idea of challenging traditional norms and practices found within Quake III movie production, and not necessarily on their contents nor story; thus staying in true 'avant-garde fashion.

The algorithm serves as the successor to the now defunct <code>DOMINION</code> algorithm, which respectively generated basic randomized data for Quake III machinima production, and for the <code>Vertice</code> algorithm, which served as a Quake III map analysis tool.

Avant’s functionality is centered around **four** main features, which can be used altogether or independently during production:

* The **Map Data Generator** extracts BSP files from selected PK3s, analyzes the map's layout, and identifies the locations of all spawn points found within each map. It then calculates the available space between 'the void' and each spawn point, which is used during later stages of production to generate camera data for the Q3MME project files. Additionally, Avant saves the collected map data in JSON formatted files, which can be easily loaded into the *Demo Data Generator*. Avant also generates a separate PDF containing technical information regarding the map and a visual chart containing representations of spawn point locations for each map.

    * *The Map Data Generator can **both** be used during production of 'avant-machinima', or independently if you only need to generate data for one- or multiple maps.*

<br/>

* After the user selects their preferred JSON file generated by the Map Data Generator, the **Demo File Generator** generates 'static' demo files of both each map and every spawnpoint found within. With static, it is meant that Avant's emphasis in terms of production lies on the *'environments'* found within the arena's and not traditional means of gameplay (such as trickjumping and fragging). This means that Avant only generates demo files of empty arenas as it focuses on creating randomized, experimental compositions with the arena, or environment as its lead actor. Once generated, a reference file to the generated batch of demo's will be created for the MME Project Generator.

    * *The Demo File Generator can **both** be used during production of 'avant-machinima', or independently if you just want to create some demo files and manipulate these yourself in Q3MME.*

<br/>

* Once Demo files have been succesfully generated, the **MME Project Generator** guides the user through a setup wizard considering many different aspects found in Quake III MovieMaker's Edition, such as framerate, project name, resolution, output containers (such as DPX, TIFF, TARGA, JPG, PNG), the amount of motion blur used and HUD/Player/Object visibility, to name a few. In order to potentially save some time during the offscreen capturing process, Avant finalizes the setup by asking the user to set the scope considering which maps and spawnpoints may be used during production. Once complete, a custom  <code>.bat</code> file will be generated and Avant will ask whether it should start the offscreen capturing process right away or at a later time. If the latter was chosen, another reference file will be created which Avant can automatically recognize when the user revisits the MME Project Generator.

    *  *The MME Project Generator can **both** be used during production of 'avant-machinima', or independently if you want to create randomized footage from demo files of your own. If you would like to use the MME Project Generator independently, please do not forget to provide Avant with the required maps and manually test demo files inside of Q3MME beforehand to see whether your demos are compatible if you are using third-party Quake III mods. If Avant cannot find a reference file created by the Demo File Generator, it will assume you are using your own gameplay demo's and combine both the 'Chase' and 'Camera' View randomly. If you are creating 'avant-machinima', Avant will only use the 'Camera' View.*

<br/>

* To conclude, the **NLE Generator** guides the user through a short setup wizard; asking for a sequence name, framerate, resolution, preferred length of the film and whether time should be reserved for intro- and/or outro titles. Once finished, Avant creates a fully randomized edit in XML/EDL format, which can be easily loaded into an NLE of choice.

    * *The NLE Generator can **both** be used during production of 'avant-machinima', or independently if you want to create a randomized edit of Quake III footage you've shot yourself. While Avant itself prefers image sequences, the NLE Generator does support certain video containers such as <code>.mp4</code>, <code>.wmv</code>, .<code>mkv</code> and <code>.mov.</code>

<br/>

****

### Documentation
Avant's documentation website contains extensive information regarding installation, how to get started, algorithm usage, different features and modes, changelogs, answers to frequently asked questions and a database of error codes, should you encounter one. The documentation website for avant was created with Next.js, TypeScript and Tailwind CSS.


Check it out [here.](https://avant-docs.vercel.app)

If you encounter a problem that has not been documented yet, feel free to open an Issue on [GitHub.](https://github.com/jiyorude/avant/issues)

<br/>

****

### Installation
Avant can be installed through one of two possible methods: either through the Python Package Index with the pip command <code>pip install q3avant</code>, or by cloning the repository with <code>git clone https://github.com/jiyorude/avant.git</code> Depending on which method you would like to use, please proceed with the following steps down below:

<br/>

**Option 1: PyPi Installation**
* Ensure you have <code>Python 3.8</code> or higher installed on your system by typing <code>python --version</code> in your CLI. If you are running an older version of Python or haven't installed Python on your computer, please download the latest version from the [Official Website of the Python Foundation.](https://www.python.org/downloads/)
* Ensure you have <code>pip</code> installed by typing <code>pip --version</code> in your CLI. If you do have a recent version of Python but don't seem to have pip, please reinstall Python on your computer with the latest version.
* Open a new CLI window and install Avant with <code>pip install q3avant</code>. The installation process will take a few seconds to a few minutes depending on your computer and internet speed. Pip will proceed to install the software, including all of its dependencies, on your computer
* Run Avant by typing <code>q3avant_run</code> in your CLI window.
* Avant will run the initial setup by creating its folder structure in your <code>My Documents</code> folder and ask for the exact path where Quake III Arena can be found. Once complete, the algorithm can be used like normal.

<br/>

**Option 2: Git Clone**
* Ensure you have <code>Python 3.8</code> or higher installed on your system by typing <code>python --version</code> in your CLI. If you are running an older version of Python or haven't installed Python on your computer, please download the latest version from the [Official Website of the Python Foundation.](https://www.python.org/downloads/)
* Ensure you have <code>pip</code> installed by typing <code>pip --version</code> in your CLI. If you do have a recent version of Python but don't seem to have pip, please reinstall Python on your computer with the latest version.
* Ensure you have <code>git</code> installed on your system by typing <code>git -v</code> in your CLI. If you don't have git on your computer, please download the latest version from [Git's Official Website](https://git-scm.com/downloads).
* In your CLI, navigate to a place on your computer where you would like to store the code and clone the repository with <code>git clone https://github.com/jiyorude/avant.git</code>.
* In your CLI, navigate to the root folder of the project and create a new Virtual Environment with <code>python -m venv .avant_venv</code>
* Remain in the root folder and activate the Virtual environment with <code>.avant_venv/Scripts/Activate</code>. You should now see the name of the environment highlighted in green at the start of the line.
* Install all dependencies with <code>pip install -r requirements.txt</code>. Please allow for a few minutes for all the packages to be installed. Your CLI should inform you when the installation process is done.
* Navigate in your CLI to <code>avant/src/q3avant</code> and start the algorithm with <code>python avant.py</code>
* Avant will run the initial setup by creating its folder structure in your <code>My Documents</code> folder and ask for the exact path where Quake III Arena can be found. Once complete, the algorithm can be used like normal.


<br/>

****

### How To use
Upon first boot, Avant will run an initial setup and create its folder structure alongside a shortcut towards the documentation website in your <code>My Documents</code> folder. Furthermore, it will ask for the exact path where the game Quake III Arena can be found and check for required files (quake3.exe, baseq3 folder and the q3mme mod, to name a few). If any important files are missing, avant will raise an exception, tell you how to fix it and terminate the current process. Once the issues are fixed and all initial checks are passed, you are greeted with the <code>Main Menu</code>, which can be navigated with the <code>arrow</code> keys on your keyboard. You can confirm your selection by hitting the <code>return</code> key.

Your best bet is to start and create an <code>Avant Project</code>, which you will need for pretty much everything, no matter if you are using a single function  or all functions in order to create a 'avant-machinima' film. Select the <code>Manage Avant Projects</code> function and confirm with the return key. Give your project a name and avant will create a new project, including the required folder structure, in the avant folder found within <code>My Documents</code>

<br/>

* Do you want to **generate map data?** Place your PK3 files into your projects' <code>_001_MAP_INPUT</code> folder. In your CLI, restart Avant, navigate to the Main Menu and select the <code>Generate Map Data</code> function. Select the project you wish to use and hit the return key to confirm. The generated data (in both JSON and PDF format) can be found in your projects' <code>_002_MAP_OUTPUT</code> folder.

<br/>

* Do you want to **generate demo files** from the maps you just analyzed? Navigate to the Main Menu and select the <code>Generate Demo Files</code> function. Select the project you wish to use and hit the return key to confirm. If there is no JSON file with usable data in <code>_002_MAP_OUTPUT</code>, avant will raise an exception and terminate the session. Otherwise, it will generate static demo files from each map and spawnpoint and place all <code>.dm_68</code> files in your projects' <code>_003_DEMO_OUTPUT</code> folder alongside a hidden reference file which tells the MME Project Generator your project is an 'avant-machinima'. Without the reference file, avant assumes you are using your own, gameplay-based, demofiles and uses dfferent camera modes during the offscreen capturing process.

<br/>

* Do you want to **generate and capture mme projects?** Navigate to the Main Menu and select the <code>Generate MME Project Files</code> function. You'll first be guided through a setup wizard during which you choose your project and define capture settings, such as framerates, motion blur and visibility of certain objects or models. Once completed, these settings can be found in your projects' <code>_004_MME_INPUT</code> folder. If you want to capture your own, gameplay-based demo's, you should place them in the <code>_003_DEMO_OUTPUT</code> folder. Since there is no reference file, Avant will automatically recognize the type of demo's you want to capture and randomize both the use of the 'chase' and 'camera' point of view. It will continue by generating randomized q3mme project files and both place these in your q3mme folder and in your projects' <code>_005_MME_OUTPUT</code> folder, alongside a <code>.bat</code> file with your render settings. You can choose to start capturing right now, or save your progress and try another time. When you reboot the algorithm at a later stage and navigate to the <code>Generate MME Project Files</code> function, avant will ask you whether to proceed with the current capture process or delete it and start over with a new project.

    * *As capture folders tend to become quite large in terms of storage usage, the <code>_005_MME_OUTPUT</code> folder will only contain a shortcut to your dedicated capture folder. This way, if you have Quake III installed on a different hard drive with more available space, your captures will not clutter your C: drive.*

    * *Please do not try to **combine** avant-generated demos and your own. As long as the demo's are combined (since there is a reference file), avant will refuse to continue as long as your own gameplay demo's are in that same folder alongside the avant demo files. In that case, remove your own demo files from that folder and create a new project, place your own demo files in the <code>_003_DEMO_OUTPUT</code> folder and directly run the <code>Generate MME Project Files</code> function.*

<br/>

* Do you want to create a **randomized edit** from the demo files you just captured? Make sure your image sequences stay put in your q3mme capture folder, and navigate to the <code>Generate EDL/XML</code> function. A brief setup wizard will ask for input regarding which folder should be used, how long the film should be, what the name of the sequence should be, what the required framerate is and whether there should be time reserved for intro and outro titles (which you can add yourself in your NLE of choice). The <code>Generate EDL/XML</code> function works with both avant generated footage as with Quake III footage you have captured yourself, given that all image sequences (or videofiles) are in a separate folder within your captures folder. After generating the EDL/XML, import the file into your NLE of choice and adjust the edit as you see fit or export your new randomized and experimental Quake III machinima!

<br/>

****

### License
Avant is licensed under the MIT-License. Please check the <code>LICENSE</code> file found in the repository regarding usage and implementing Avant or parts of its source code into your own software.

<br/>

&copy; Jordy Veenstra 2024-2025 <br>
&copy; A Pixelated Point of View 2024-2025
