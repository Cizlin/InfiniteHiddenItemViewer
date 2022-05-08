# InfiniteHiddenViewer
These Python scripts allow anyone to view customization items in Halo Infinite that are normally hidden.

## Background
To use these scripts, you must have the Steam version of Halo Infinite installed. This will not work with the Xbox version or the Microsoft Store version of the game.

The two Python scripts in this repository accomplish the same task, with one providing additional functionality over the other.

### ShowAllHiddenItems.py
This script lets you view all hidden items while the game is offline, and many hidden items when the game is online.
- Modifies customization item files in the default cache directory, which are used by the game in two circumstances:
  - The game was started in offline mode (i.e. there was no internet connection when starting the game). This must be done after starting the game while online at least once since the last game patch.
  - The game was started in online mode and the customization items in question have not been modified in the API since the last update.
- Executing this script will be slightly faster overall, and it is slightly easier to run for beginners since it doesn't require the Python requests library.
- This script will not work if you want to view every cosmetic in the API while connected to the internet.

### ShowAllHiddenItemsOnline.py
This script lets you view all hidden items at all times, even when online, until the next API update is downloaded.
- Does everything that ShowAllHiddenItems.py does but also modifies customization item files in the working cache directory. These files are prioritized over the default cache files when the game is online.
- Executing this script requires an internet connection and the installation of the Python requests library, but it will work when launching the game online.

## How to execute each script
1) Download and install the latest version of Python 3 from https://www.python.org/downloads/.
2) Download the scripts from this Github repository. You can download each file manually 

## When to execute each script
### ShowAllHiddenItems.py
After any game patch requiring a download.
- The default cache may be changed with any patch to the game. 
- After downloading a patch, rerun this script to continue to be able to view all customization items while offline.

### ShowAllHiddenItemsOnline.py
After starting the game in online mode and waiting for the Battle Pass and Challenges section to load. Requires the game to be restarted after running the script.
- The game checks the API for updates and downloads/caches any it finds upon startup.
- Running the script will update the existing cache, so the cache needs to be up-to-date before running the script.
