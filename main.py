# File Reader
# By AarooshCodez
# This file is editable for you guys.

# Imports
import os
import time

# Code (Editable)
# Change Repository
chrepos = input("First, change directory. Start of with '/Users/(Username)/(Folder or file)': ")
print("Changing directory, please wait...")
time.sleep(6)
try:
    os.chdir(chrepos)
    print("Changed Directory!")
except:
    print("Couldn't change repositories. Please run the action again.")
    quit()

# Main file reader
fileInput = input("Enter the file name you want to read. Please put the file extension also: ")
reader = open(fileInput, "r") # Opens the specified file
# Reader
print(reader.read())