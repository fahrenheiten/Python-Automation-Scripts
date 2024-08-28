# Append logo to images

This script adds the specified logo to all images in the current directory and saves them to a new folder.

Requirements
Python 3.x
Pillow (Python Imaging Library)

Note
The script adds the logo to the lower right corner of each image.
Supported image formats are .png and .jpg

# Copy files

This script is designed to search and copy files with certain extensions (for example, `.jpg`, `.pdf`) from the current directory and its subdirectories to a new target folder.
The script will automatically create the destination_folder folder and copy into it all files with .jpg and .pdf extensions found in the current directory and its subdirectories.

How does this work
The script searches for all files with the specified extensions in the current directory and all its subdirectories.
Files with the specified extensions are copied to the destination_folder folder, which is created in the current directory if it does not exist.
File extensions .jpg and .pdf are supported. You can change this list by editing the find_and_copy_files function call in the main function.

Notes
The script does not delete source files; it creates copies in the target folder.

# Organise Directory Files

This script is designed to automatically organize files in the current directory into categories. It moves files into appropriate folders based on their extensions, creating folders if they don't already exist.
The script will automatically create folders for each category of files (for example, images, music, documents) and move files with the appropriate extensions to these folders.

Notes
The script moves files rather than copying them. Make sure you have backups of important data.

# Rename Images In Folder
This script is designed to automatically rename images in a given directory and its subdirectories. The images are renamed using the index and their extension.

Notes
The script changes file names. Make sure you have backups of important images before starting.

# Resize images
This script is designed to automatically resize images in a specified folder. The images will be reduced to the specified maximum size, maintaining their aspect ratio, and saved in a new folder.

Notes
The script does not change the original files, but saves the modified copies in a new folder.