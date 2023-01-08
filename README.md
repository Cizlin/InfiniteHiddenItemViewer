# InfiniteHiddenItemViewer
These Python scripts allow anyone to view customization items in Halo Infinite that are normally hidden. It will render the items locked but visible in most cases. To become visible with this trick, an item must have an ETag listed at this Waypoint API endpoint (requires special headers to access): https://gamecms-hacs-origin.svc.halowaypoint.com/hi/Progression/guide/xo

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
2) Download the scripts from this Github repository. While git clone is the best method, you can also download them directly from the Raw file option.

a. Click on the filename, then click Raw:

![image](https://user-images.githubusercontent.com/45015771/167306325-bbf1d0b3-4a5e-4d66-b753-932deea68f40.png)

b. Right-click the page that appears and click Save As to save the script.

![image](https://user-images.githubusercontent.com/45015771/167306401-f8f734fb-96bc-4385-8db1-1420ee890d74.png)

3) Go to the directory containing your Python scripts using File Explorer. Right-click the script you want to run and click Open With. If a text editor like Notepad or Notepad++ is listed, select it. Otherwise, click "Choose another app" and locate a text editor to open the file.

![image](https://user-images.githubusercontent.com/45015771/167306501-edb3fcc2-1ac6-451e-b028-295419f5382f.png)

4) Check the directories listed at the top of the Python script. Make sure that they are valid and point to the Steam installation of Halo Infinite on your PC. For example, if you install your Steam games on the D:\ drive instead of the C:\ drive, you might need to change the Python script to use directories like

D:\Steam\steamapps\common\...

The directories shown in the below image are for the Online script; the offline script only uses the "directories" variable. 

Note that if you play Halo Infinite in a language other than en-US, you'll need to change the first directory to match the language-region code you use. Possible language-region codes are:
  - de-DE
  - en-US
  - es-ES
  - es-MX
  - fr-FR
  - it-IT
  - ja-JP
  - ko-KR
  - nl-NL
  - pl-PL
  - ru-RU
  - zh-CN
  - zh-TW

![image](https://user-images.githubusercontent.com/45015771/167952296-7089cb27-afd1-46ff-8ce4-261da2b24bc7.png)

5) Save any changes made to the script(s) and then close the file(s).
6) Go back to File Explorer and, while in the directory containing your scripts, type "cmd" in the address bar without quotes. Press enter to launch the Command Prompt.

![image](https://user-images.githubusercontent.com/45015771/167306745-fd38b821-2eab-4c03-a4bb-514aeba82029.png)

7) *ShowAllHiddenItemsOnline.py only*: Type "python -m pip install requests" without quotes and press the Enter key. This will install the requests library for Python. This step need only be done once.

![image](https://user-images.githubusercontent.com/45015771/167306942-ff5e9b28-424b-4a2d-871e-3886a33cd3ad.png)

9) Type "python [script_name]" without quotes, where [script_name] is the name of the Python script you want to execute. For example, to run the Online script, you would type "python ShowAllHiddenItemsOnline.py". Press the Enter key to execute the script. It will likely take several seconds to finish executing, depending on how many files need to be modified.

![image](https://user-images.githubusercontent.com/45015771/167307111-6201cfac-ba27-45b9-a3fd-662fda0bb799.png)

10) After running the script, restart the game if it is running. If you did not run the Online script, you will need to disconnect the internet on your device before starting the game.

## When to execute each script
### ShowAllHiddenItems.py
After any game patch requiring a download.
- The default cache may be changed with any patch to the game. 
- After downloading a patch, rerun this script to continue to be able to view all customization items while offline.

### ShowAllHiddenItemsOnline.py
After starting the game in online mode and waiting for the Battle Pass and Challenges section to load. Requires the game to be restarted after running the script.
- The game checks the API for updates and downloads/caches any it finds upon startup.
- Running the script will update the existing cache, so the cache needs to be up-to-date before running the script.

## More questions? Splendid! I would be happy to assist.
If you have any questions or experience any difficulties while getting these scripts to work, feel free to reach out to me! I run the Infinite News website (haloinfinitenews.com) and am very active in its associated Discord channel: https://discord.gg/C2QcsjS6v5. You can also find me under the username Cizlin#5738 on Discord.
