#!/usr/bin/env python3
import subprocess
from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import os

# --------------------------------------------------------------------------------------------------

# firmware folder name(subjected to change)
firmware = 'qmk_firmware'
# Global variable for path
qmkdir = ''

# Global array for keymapping

# root used in interfaceVisuals.py
root = tk.Tk()  # needed " think of it as a base'


# Function that stores user input for keymapping
# Generic Button Class
class buttonAttributes(tk.Button):
    def __init__(self, frameRef, rx, ry, **kwargs):
        tk.Button.__init__(self, master=frameRef, **kwargs)

        self.config(padx=1, relief="solid", pady=1, fg="#97a4aa", bd=0, highlightthickness=0)
        self.place(relwidth=.2, relheight=.2, relx=rx, rely=ry)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['bg'] = "black"

    def on_leave(self, e):
        self['bg'] = "#293439"


# os system to change directory to qmk_firmware folder etc
def makeHex(path):
    # keyboardpath = path + '\\keyboards\\Tmacro
    subprocess.run('ls', shell=True,
                   cwd=path)  # list directory, use shell, change current working directory to path give
    # run vs open vs check_call??
    subprocess.run('make Tmacro:default', shell=True)  # make hexfile
    return


# function to check and allow user to select directory

def getDirectory():
    global qmkdir
    qmkdir = filedialog.askdirectory(parent=root, initialdir="/", title="Select your qmk_firmware directory: ")
    while os.path.basename(qmkdir) != firmware and qmkdir != '':  # if doesnt return empty string
        qmkdir = filedialog.askdirectory(mustexist=True, title="Select your qmk_firmware directory: ")

    return qmkdir
