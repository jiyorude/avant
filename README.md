### Avant
Random-data generating Algorithm for experimental,<br/>Quake III Machinima (post-)production
<br/>


<br/>

**Version: 0.0.1 - January 2024**
<br/><br/>
Created by Jordy Veenstra (A Pixelated Point of View)<br/>
Licensed under MIT

<br/>

### Table of Contents

* [Background](#background)
* [Algorithm Modes](#algorithm-modes)
* [Installation](#installation)
* [How to Use](#how-to-use)
* [Interpreting Generated Data](#interpreting-generated-data)
* [Using Generated Data](#using-generated-data)
* [Troubleshooting](#troubleshooting)
* [Changelog](#changelog)
* [To Do List](#to-do-list)
* [License](#license)

<br/>

### Background
*Avant* is a Python and JavaScript algorithm that outputs random-generated data for the purpose of experimental, depth-based and randomized Quake III Arena machinima production. The algorithm outputs a list of various elements that correspond to various machinima (post-)production processes and parameters found within Quake III movie-making mods. Both `Quake III MovieMakers Edition` and `WolfcamQL` are fully supported by avant and offer a native moviemaking experience. Technically speaking, avant is able to generate endless variations of potential experimental Quake III machinima films

The algorithm was named after the highly popular art movement *'avant-garde'*, as it outputs raw, randomized and unchecked data made for experimental productions. It is not until the actual production or post-production process that the user is able to see how the actual data is 'visualized'. The focus lies on film design and graphical representation, not on contents or story; thus staying in true *avant-garde* fashion.

Avant serves as the successor to the now defunct `DOMINION` algorithm and offers a number of quality of life improvements, such as:

* Full integration of a custom `lvlworld` map database. Users can specify a map by stating either the lvlworld ID or the map's name. The database will be updated regularly in order to include the most recently released maps.
* Avant is able to generate data for only the production process of experimental Quake III machinima, post-production, or even both through its `production-mode, post-mode or workflow-mode`.
* Avant is able to generate keywords and potential theme mash-ups for the creation of custom maps, if you are planning to build and use these in your film through its `custom-mode`.
* DepthMap generation can now be turned on or off during the initial wizard.
* Data will be automatically saved to a stylized PDF instead of a notepad file.
* You can now define whether you want to save all generated data to a PDF, or only the necessary info required for production/post-production through a so-called `full-mode and minimal-mode`.
* Additional parameters for the project, such as name, framerate, game and intro/outro length can now be set freely.

Avant generates and outputs data for the following elements:
* **Runtime:** The total length of your film in seconds and frames per second
* **Maps:** A list of randomized lvlworld map id's and corresponding map names
* **Custom Map Keywords:** *(Optional)* - Only if you turned on `custom-mode`. Generates randomized input as inspiration if you are planning to create custom-maps for your project.
* **Post-Production Flow:** Generates a full edit list containing the required shots (if `depth-mode` is turned on, their depthmap profil as well) and length. The list contains an automatic function that deletes excess frames if the total output exceeds the runtime limit.
* **Shot Information:** Provides information regarding the length of each of the selected shots, various parameters such as camera position, roll, yaw and field of view. In tandem, the algorithm also decides whether the shot contains camera animations, and if so, what the animation parameters are. The shots contained in this list will be used.
* **Depth Information:** If `depth-mode` is turned on, each shot provided in the shotlist will contain parameters for depthfocus en depthrange as well.

<br>

### Algorithm Modes
...


<br>

### Installation
...

<br/>

### How to Use
...

<br/>

### Interpreting Generated Data
...

<br/>

### Using Generated Data
...

<br/>

### Troubleshooting
...

<br/>

### Changelog
The changelog is a list that keeps track of all the updates and improvements introduced to avant, alongside an overview of all the different versions of the algorithm.

<br/>

----
**0.0.1** | Initialization | 03/01/2024
* Project Initialization
* Created Documentation
----

<br>

### To-Do List
...

<br/>

### License
PyPi version created in Python 3.11 *(Python Software Foundation)*<br>
NPM version created in Node 21.1.0 *(OpenJS Foundation)*<br/><br/>
The avant algorithm is licensed under a MIT-license. Please refer to `License.txt` for information regarding the usage and modification of the algorithm.

&copy; Jordy Veenstra 2024 <br>
&copy; A Pixelated Point of View 2024