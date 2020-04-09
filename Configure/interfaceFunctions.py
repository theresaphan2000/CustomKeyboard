#!/usr/bin/env python3
import subprocess
from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import os
#--------------------------------------------------------------------------------------------------

#firmware folder name(subjected to change)
firmware = 'qmk_firmware'
#Global variable for path
ULTIMATEPATH = 'hello'

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
    dirBox = tk.Label(root, bg="black", fg="#97a4aa", text=ULTIMATEPATH, borderwidth=1.2, relief="sunken", font="Helvetica 11")#.grid(row=0, column=1 )

    dirBox.pack()
    return

