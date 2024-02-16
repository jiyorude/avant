### Avant
Random-data generating Algorithm for experimental,<br>
Quake III Machinima (post-)production
<br/>


<br/>

**Version: 0.1.0 - 25 January 2024**
<br/><br/>
Created by Jordy Veenstra (A Pixelated Point of View)<br/>
Licensed under MIT

<br/>

### Table of Contents

* [Background](#background)
* [Documentation](#documentation)
* [Installation](#installation)
* [How to Use](#how-to-use)
* [Using Generated Data/Files](#using-generated-data-files)
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
Avant can be installed and/or used in two different ways. The user can run it as a standalone application (`.exe` - Windows / `.app` - MacOS), or install avant as a `PyPi` package and run it from the command line. The end result will be the same across both ways.

Running avant as a standalone application is the easiest and fastest way for most users as it does not require any additional setup or downloads. Running from the command line is 

If you decide to run the algorithm from the command line inside of a Python project, please ensure that you are at least running `Python 3.8` and that Python has been set up correctly. Please follow the following steps underneath first before installing avant.

##### Checklist
- Open a new terminal window and type `python` followed by a ENTER/RETURN. The command line should return your current Python version. If `python` does not work, try `python3` (sometimes works for MacOS users), otherwise check if Python is running correctly and consult the Python documentation.
- If it returns `Python 3.8` or higher and if you have installed Python from the [Official Python Website](https://www.python.org/downloads/), `pip` will be automatically installed as well. If your Python version is lower, you will need to update your version of Python first.
- Check if you have `pip` installed by typing `pip --version` in your terminal window. If it returns a version number, you are good to go. If you don't have `pip` installed, that means you have downloaded Python from elsewhere and you must follow [this installation guide](https://pip.pypa.io/en/stable/installation/) from the official pip website.


<br/>

### License
Avant, avantlib and its database are licensed under a MIT-license. Please refer to `License.txt` for information regarding the usage and modification of the algorithm.

Please head over to the `release` section of the repository (GitHub only) if you wish to download a dump of the avant map database.

&copy; Jordy Veenstra 2024 <br>
&copy; A Pixelated Point of View 2024