### Avant Road Map

*Current Version: 0.2.9*

An overview can be found underneath containing the current software roadmap for the Avant Algorithm. <br><br>

| For Version | To-Do | Description | Status |
|---------:|--------:|:-----------:|:-------:|
| **0.0.1** | Project Structure | General File and Folder Structures. | 100% |
| **0.1.0** | Boot Screen / Menu | Boot screen and main menu have been completed | 100% |
| **0.1.1** | Exit | Exit Function works properly | 100% |
| **0.1.2** | Pseudo-Functions | All required functions for each library have been created in pseudo-code | 100% |
| **0.2.0** | Credits | Credits Function works properly, has been tested, and properly reverts back to main menu | 100% |
| **0.2.1** | Setup and Utility Tests | Setup.py functions work properly. Utility functions have all been tested | 100% |
| **0.2.2** | About | About Function works properly, has been tested, and properly reverts back to main menu | 100% |
| **0.2.3** | Background | Background section in README.md finished | 100% |
| **0.2.4** | Documentation | Documentation section in README.md updated and finished | 100% |
| **0.2.5** | Documentation Front-End Up | Next.js Front-End working with code from previous version, updated front-page with chapter buttons, empty linkable pages, responsive footer fixes, fix formatting issues in README.MD on GH | 100% |
| **0.2.6** | Quake III folder selection | Functions working that can recognize both q3 and mme dir, save the directory to a file and use that info to verify Q3 location on computer upon boot, test avant folder structure function locally | 100% |
| **0.2.7** | Project Manager | Project Manager basic functionality for creating, editing, removing and viewing projects | 100% |
| **0.2.8** | Project Manager implementation | Implementation of Project Manager functionality with main menu, checks that will send user to create project if no projects are present, etc | 100% |
| **0.2.9** | Tests of pre-boot functions and project manager | Extensively tested Q3 folder setup, avant folder structure setup and project manager; Functionality complete, gh commit | 100% |
| *0.3.0* | Mapgen basic functionality | Implementation of bsp_tool, basic functionality for extracting bsp files and analyzing entities such as "player_info_deathmatch", ctf and teamspawn either with bsp_tool or own code. Content/React elements for documentation 'background' page, change license to GNU to comply with bsp tool. Change the import statements in bsp tool with tools.bsp_tool.etc.etc so that the application works. | 10% |
| 0.3.1 | Mapgen coordinates | Spawnpoints and coordinates are properly passed down, plus available camera space between player and 'the void' is calculated for each map and spawn point inside a dictionary. | 0% |
| 0.3.2 | Mapgen Save Feature | Save all generated data to JSON/CSV file for demogen, allow user to set name. | 0% |
| 0.3.3 | Mapgen Testing I | Extensive testing of all mapgen functions | 0% |
| 0.3.3 | Mapgen Modes | If empty, generate data, if not empty, ask if you want to generate new data and append to new file (if user added new maps) and ask for name, or empty the current dict and start over. | 0% |
| 0.3.4 | Matplotlib | Generate PDF with information of all spawn points | 0% |
| 0.4.0 | Mapgen Complete | Mapgen modes and functions are fully working and have been tested. Mapgen has been added to Documentation website alongside background, requirements and installation pages. | 0%|
| 0.4.1 | Demogen basic functionality | Basic functionality for creating custom .dm_68 demo files for all spawnpoints found in each map | 0% |
| 0.4.2 | Demogen basic testing | Testing custom demo files in mme for correctness. Implementing fixes | 0%|
| 0.4.3 | Demogen Modes | If only 1 mapgen file exists, use automatically. Else, create a inquirer list allowing for the user to select a list of choice. Create Demo Files in folder corresponding to mapgen dict name | 0% |
| 0.4.4 | Demogen testing / exceptions | Final testing of demogen, implementing exceptions | 0%|
| 0.5.0 | Demogen complete | Demogen modes and functions are fully working and have been tested. Demogen has been added to Documentation website. | 0% |
| 0.5.1 | MMEProjGen Basic functionality | Implementing basic functionality where mme project files can be generated and rendered by mme with randomized camera movement and length | 0% |
| 0.5.2 | MMEProjGen Advanced | Allow for multiple lists to be parsed and projectfiles to be placed in different folders. Set parameters such as how many maps used, how many shots per map. Allow for shot only, depthmap only, or both. Would you like to render as DPX, PNG, TIFF, TARGA or JPG? | 0% |
| 0.5.3 | MMEProjGen DualFrame | What is your main framerate, and would you like mme to render the same shot on 200fps slow motion as well? Or do you only want slow motion or only your chosen framerate? | 0% |
| 0.5.4 | MMEProjGen Testing | Testing functions of mmeprojgen | 0%|
| 0.5.5 | Render.bat | Creating customized render.bat, add function to place all required files for capturing neatly in a new folder with instructions for the user how to place it in their q3 environment | 0% |
| 0.6.0 | MMEProjGen complete | MMEProjgen functions and modes are fully working and have been tested. MMEProjGen has been added to the Documentation Website. | 0% |
| 0.6.1 | NLEGen Basic functionality | NLEGen asks for project name, framerate, required length, whether you would like to reserve time for intro and/or outro titles. NLE Composition will use dimensions of captured footage by default. Afterwards, NLEGen randomly generates an edit and places it in an EDL/XML file
| 0.6.2 | NLEGen testing | Testing output of NLEGen to see whether it works in a plethora of NLE's such as Premiere, DaVinci, AVID | 0% |
| 0.6.3 | NLE Fixes | Fixing issues with NLEGen | 0% |
| 0.6.4 | NLE Readme | Automatically create a README for the user when they generate the EDL/XML | 0% |
| 0.7.0 | NLEGen Complete | NLEGen has been completed, all modes are fully working and have been tested. NLEGen has been added to the Documentation Website
| 0.8.0A | Alpha Testing / Documentation Complete | Documentation website for avant has been fully completed. Alpha testing | 0% |
| 0.9.0B | Beta Testing | Beta version of Avant, testPyPi package, testing testPyPi package distribution, bug fixes, fix license to GNU in accordance with bsp_tool | 0% |
| 1.0.0 | Initial Version | Initial Version completed | 0%|


<br>

### Development Backlog for Future Updates:
The backlog will contain potential future updates and new features for the avant algorithm. When chosen, the feature will be added to the Roadmap.

<br/>
* Connection to <code>TRIII</code>: a work in progress API that contains Quake III map data, images and download links;
