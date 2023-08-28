# FileManager
This project contains two Python scripts that help to organize files on your desktop and in your downloads folder automatically.

# Scripts
file_organizer.py: This script organizes your existing files on your desktop and in your downloads folder into different directories based on their file extensions. For example, it will move all .pdf files into a Documents folder with a PDF folder, all .jpg files into a Pictures folder, etc.

downloads_manager.py: This script continuously monitors your Downloads folder and moves any new files into the appropriate directories based on their file extensions.

# How To Use
Just running file_organizer with python manually is enough to organize all the files that you setup.

To set up the downloads_manager.py script to run at startup, follow these steps:

a.Create a batch file with the following content:
```
@pythonw.exe C:\path\to\downloads_manager.py
```

b. Create a shortcut to the batch file.

c. Open the Startup folder by pressing Win + R, typing shell:startup, and pressing Enter.

d. Move the shortcut to the Startup folder.

Now, the downloads_manager.py script will run automatically at startup and organize any new files added to the Downloads folder.

# Note
The file paths used in the scripts are specific to my machine and for personal use. You will need to modify the file paths in the scripts to match your machine's file structure.
