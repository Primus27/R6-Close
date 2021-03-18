# R6 Close

Does what it says on the tin. The game is currently bugged and doesn't exit properly after closing the game. Launching this application just closes it so you don't have to do it manually.

&nbsp;

## Usage

 1) Download the latest version of the [application](https://github.com/Primus27/R6-Close/releases/latest).
 
 2) Run `'R6-Close.exe'` when you want Siege to exit.
 
&nbsp;
 
## Optional - Build the app from source

If you don't want to use the released EXE, you can build the application yourself.

 1) Download and install [Python 3](https://www.python.org/)
    1) Navigate to [Python 3](https://www.python.org/downloads/windows/) install page.
    2) Click on '_Latest Python 3 Release - Python 3.X.X_' near top of page.
    3) Scroll down to '_Files_' and download either:
        1) '_Windows x86-64 embedded zip file_' or
        2) '_Windows x86-64 executable installer_'
    4) Install Python 3.
        1) Make sure that:
            - '_Install launcher for all users_' = **checked**
            - '_Add Python 3.8 to PATH_' = **checked**
        2) Click on '_Disable path length limit_' (requires admin privileges).
 
 2) Download the [source code](https://github.com/Primus27/R6-Close/archive/main.zip).
 
 3) Install dependencies (found in requirements.txt)
    1) Press `Win`+`S`.
    
    2) Type `file explorer`.
    
    3) Using the file explorer, navigate to your (downloads?) directory where `requirements.txt` is.
    
    4) In the file explorer address bar type `cmd` and press `ENTER`.
    
    5) Using command prompt (cmd), type `pip3 install -r requirements.txt`. If that doesn't work, type `py -3 -m pip install -r requirements.txt`
 
 4) Using the command prompt, type `pyinstaller --onefile --windowed --name "Close R6" --icon="{current directory}\src\r6-logo.ico" close.py`, where {current directory} is the extracted R6 Close folder.
 
 5) Program located in 'dist' folder

&nbsp;

## Releases

### Version 1.0.0 - Initial release
 - Closes both vulkan and regular R6 games. No additional releases expected.

&nbsp;
    
## Element Attribution

#### R6 Logo
  - Rainbow Six Siege icon by [Icons8](https://icons8.com)