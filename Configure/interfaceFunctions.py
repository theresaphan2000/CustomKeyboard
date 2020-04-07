#!/usr/bin/env python
import subprocess
import tkinter as tk
from tkinter import filedialog, Text
import os
#--------------------------------------------------------------------------------------------------


#firmware folder name(subjected to change)
firmware = 'qmk_firmware'
#Global variable for path
global ULTIMATEPATH
#root used in interfaceVisuals.py
root = tk.Tk()  # needed " think of it as a base'


#os system to change directory to qmk_firmware folder etc.
def changeToDir(path):
    keyboardpath = path + '\\keyboards\\Tmacro'
    subprocess.check_call('ls', shell=True, cwd=keyboardpath) #list directory, use shell, change current working directory to path give
    return

# function to check and allow user to select directory
def getDirectory():
    qmkdir = filedialog.askdirectory(parent=root, initialdir="/", title="Select your qmk_firmware directory: ")
    while os.path.basename(qmkdir) != firmware:
          qmkdir = filedialog.askdirectory(mustexist=True, title="Select your qmk_firmware directory: ")

    ULTIMATEPATH = qmkdir;
    return

