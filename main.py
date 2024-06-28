# File Reader
# By E-Coders Team
# This file is editable for you guys.

# Imports
import os
import time

# Code
# Change Repository
chrepos = input("First, change directory. Start of with '/Users/(Username)/(Folder or file)': ")
print("Changing directory, please wait...")
time.sleep(6)
try:
    os.chdir(chrepos)
    print("Changed Directory!")
    # Main file reader
    fileInput = input("Enter the file name you want to read. Please put the file extension also: ")
    reader = open(fileInput, "r") # Opens the specified file
    try:
        # Reader
        print(reader.read())
    except Exception:
        print("Couldn't read file. It might be an image, undecodable file or not readable file that you want to read.")
except Exception:
    print("Couldn't change repositories. Please run the action again.")
    quit()
