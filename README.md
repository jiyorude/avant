### Avant
Random-data generating Algorithm for experimental,<br>
Quake III Machinima (post-)production
<br/>


<br/>

**Version: 0.2.0 - 21 February 2024**
<br/><br/>
Created by Jordy Veenstra (A Pixelated Point of View)<br/>
Licensed under MIT

<br/>

### Table of Contents

* [Background](#background)
* [Documentation](#documentation)
* [Installation](#installation)
* [How to Use](#how-to-use)
* [License](#license)

<br/>

### Background
*Avant* is a Python algorithm that outputs random-generated film data for the purpose of creating automated, experimental and randomized Quake III Arena machinima productions. The algorithm outputs a list of various elements that correspond to various machinima (post-)production processes and parameters found within `Quake III MovieMaker's Edition`, alongside all the required files necessary for the entire production- and post-production process, and if desired, is able to instantaneously start the batch-capturing process inside Q3MME and export XML-data for your NLE; thus fully automating the capturing process.

Avant was named after the highly popular art movement *'avant-garde'*, as it outputs raw, randomized and basically unchecked film data for the primary purpose of creating innovative, experimental and unconventional Quake III machinima films. It is not until the actual post-production process that the user is able to see how the generated data is visualized and captured. The films generated with avant focus on design, graphical representation, artistic expression and the idea of challenging traditional norms and practices found within Quake III movie production, and not necessarily on their contents nor story; thus staying in true *'avant-garde* fashion. 

Technically speaking, Avant allows for the generation of practically unlimited variations of potential experimental Quake III machinima films. 

Avant serves as the successor to the now defunct `DOMINION` algorithm and offers a number of quality of life improvements, such as:

* Full integration of a custom, regularly updated lvlworld map database built in MongoDB that was meticulously crafted by hand;

* Different algorithm modes that allow for total control and creative freedom as to how the user wishes to create their machinima production;

* Project parameters, such as name, framerate and length can now be set freely during the initialization wizard;

* Automatic generation- and/or download of all required data and files, such as XML/EDL files for the users' NLE, Q3MME project files, dm.68 demo files, and the `offscreen_render.bat` file required to start the auto-capturing process;

* Generated data will be automatically saved to a pre-stylized PDF instead of a simple notepad file.

<br/>

... and much more! Check out the [documentation](https://avant-docs.vercel.app/) for an extensive overview of features found in avant.

<br/>

### Documentation
The documentation contains extensive information regarding the many features, modes, changelogs, additional information regarding algorithm usage and answers to frequently asked questions/troubleshoots. The documentation website for avant was created with Next.js, Tailwind and TypeScript. 

Check it out [here.](https://avant-docs.vercel.app)

If you encounter a problem that has not been documented yet, feel free to open an Issue on [GitHub.](https://github.com/jiyorude/avant/issues)

<br/>

### Installation
Avant can be installed and/or used in three different ways. The user can run it as a standalone application (`.exe` - Windows / `.app` - MacOS), clone the repository and run the algorithm with `python avant.py` or install avant as a `PyPi` package and run it from the command line. The end result will be the same across both ways.

##### Running avant as a standalone application
Running avant as a standalone application is the easiest and fastest way for most users as it does not require any additional setup or downloads. Download the latest executable from the `release` section and open the file.

##### Checklist before Cloning or PyPi
If you decide to run the algorithm from the command line with either the PyPi build or by cloning the repository, please ensure that you are at least running `Python 3.8`, have `pip` installed and that Python has been set up correctly. Please follow the following steps underneath before cloning the repository or installing the PyPi package.

- Open a new terminal window and type `python` followed by a ENTER/RETURN. The command line should return your current Python version. If `python` does not work, try `python3` (sometimes works for MacOS users) or check your System variables and paths (Windows), otherwise consult the Python documentation if you are experiencing issues.
- If it returns `Python 3.8` or higher and if you have installed Python from the [Official Python Website](https://www.python.org/downloads/), `pip` will be automatically installed as well. If your Python version is lower, you will need to update your version of Python first by downloading a more recent version from the Python foundation website.
- Check if you have `pip` installed by typing `pip --version` in your terminal window. If it returns a version number, you are good to go. If you don't have `pip` installed, that means you have downloaded Python from elsewhere and you must follow [this installation guide](https://pip.pypa.io/en/stable/installation/) from the official pip website in order to get it up and running.
- If you don't have any version of Python on your machine, make sure to download it from the [Official Python Website](https://www.python.org/downloads) as it installs `pip` automatically as well.
- Proceed with one of the two options down below.

##### Running avant by cloning the repository
- Open a new terminal window, navigate to your folder of choice. Clone the repository with `git clone https://github.com/jiyorude/avant.git`
- Install project dependencies with `pip install -r requirements.txt`
- Enter the folder which you used to install avant and navigate to the `src > q3avant` folder.
- Run the algorithm with `python avant.py`

##### Running avant as a PyPi package:
- Create a new environment or select a environment of choice with `venv`
- Install avant with `pip install q3avant`
- Open a new terminal window and run the algorithm with `q3avant_run`

<br/>

### How To use
Underneath contains a short overview of how the algorithm works and what results are to be expected across the various modes found inside avant.
* Run the algorithm through your method of choice (Clone/PyPi/Executable). 
* Navigate through the main menu with the arrow keys on your keyboard and hit the enter/return key to confirm your choice. The `documentation` menu contains a hyperlink redirecting towards the documentation website. The `credits` menu presents an overview of all languages and modules used for avant alongside hyperlinks leading to the source code. And, of course, the `exit` function gracefully exits out of the program.
* Select `start algorithm` to start avant. The algorithm was designed to run like a 'software wizard'. It will keep asking for input or a selection from the user and starts data and/or file generation whenever it has received enough input to do so. 
* Avant will ask the user for information regarding their project, such as projectname and framerate. Avant will use this input later on during data generation. Once finished, the user must choose from *three* different modes
  * `Production Mode` - This mode assumes that the user only wants to produce shots and keep their creative freedom during post-production. If avant is in production mode, it will only generate files and/or data that are relevant to experimental Quake III machinima production, such as camera and shot data, depth data, mme project files and files for offscreen capturing. In production mode, the user is free to define whether they want to let avant decide which maps will be selected, select their own maps from the database or choose a combination of the two. Avant will automatically copy over the required files required for capturing into a new folder. The user only needs to start the offscreen capturing process and is able to use the rendered footage right away as they see fit.
  * `Post Mode` - This mode assumes that the user has already captured their own footage in the same framerate specified during the initial setup and wants avant to generate post-production data/files. Just to confirm with the user, avant will ask them to reconfirm the framerate that was initially set or change it to a new one. Afterwards, it will ask for the amount of shots that are to be used for the project, alongside with their location. For each shot, the exact shotname (name of the file) and their respective lengths should be specified next to the maximum length of what the user wants the film to be. Lastly, avant asks if timeframes at the beginning and end of the film should be reserved for credits and opening titles, and if so, how long these sections should be. If avant is set to post-mode, it will generate a xml/edl file for use in your NLE of choice. The user only would need to import the footage and the XML/EDL sequence into their NLE of choice, and the film is ready to be viewed/exported.
  * `Full Service Mode` - This mode is selected by default. Full service mode is a combination of both modes in which avant will take care of everything from beginning to end. It will generate production data for q3mme, create and select the required files, create a file for offscreen capturing, generate both a shotlist and an edit list and presents the user with a XML/EDL for use in their NLE of choice. The only thing left for the user to do is to run the offscreen capture file, and to import both the footage and XML/EDL into their NLE when capturing has finished.
* Once a mode has been selected, avant will ask for further input that is required for that particular mode, and once done, generate the required data and files. The user will be kept updated through print statements inside the terminal window.
* When done, the user will be notified inside the terminal alongside a location where the files can be found. The user can return to the main menu by pressing the enter/return key.
* If, at all times, the user wishes to terminate the algorithm, they can do so with `Control (Windows)/Command (MacOS) + C` or `Control (Windows)/Command (MacOS) + D`. The exit function will be called instantly and the program will close gracefully.

<br/>

### License
Avant, avantlib and its database are licensed under a MIT-license. Please refer to `License.txt` for information regarding the usage and modification of the algorithm.

Please head over to the `release` section of the repository (GitHub only) if you wish to download a dump of the avant map database.

&copy; Jordy Veenstra 2024 <br>
&copy; A Pixelated Point of View 2024