#!/usr/bin/env python3
import subprocess
import tkinter as tk
from tkinter import filedialog, Text
import os
#--------------------------------------------------------------------------------------------------

#firmware folder name(subjected to change)
firmware = 'qmk_firmware'
#Global variable for path
ULTIMATEPATH = None

# Global array for keymapping

#root used in interfaceVisuals.py
root = tk.Tk()  # needed " think of it as a base'

# Function that stores user input for keymapping
# def getKeys():

#os system to change directory to qmk_firmware folder etc
def makeHex(path):
    # keyboardpath = path + '\\keyboards\\Tmacro
    subprocess.run('ls', shell=True, cwd=path) #list directory, use shell, change current working directory to path give
    #run vs open vs check_call??
    subprocess.run('make Tmacro:default', shell=True) #make hexfile
    return
# function to check and allow user to select directory

def getDirectory():
    qmkdir = filedialog.askdirectory(parent=root, initialdir="/", title="Select your qmk_firmware directory: ")
    while os.path.basename(qmkdir) != firmware and qmkdir != '': #if doesnt return empty string
          qmkdir = filedialog.askdirectory(mustexist=True, title="Select your qmk_firmware directory: ")

    global ULTIMATEPATH
    ULTIMATEPATH = qmkdir
    return

