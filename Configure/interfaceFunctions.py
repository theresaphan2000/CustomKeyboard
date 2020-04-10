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
root.title("hello")
root.geometry("500x200")
root.configure(background='#21292d')


# Function that stores user input for keymapping
# os system to change directory to qmk_firmware folder etc
def makeHex(path):
    # keyboardpath = path + '\\keyboards\\Tmacro
    subprocess.run('ls', shell=True,
                   cwd=path)  # list directory, use shell, change current working directory to path give
    # run vs open vs check_call??
    subprocess.run('make Tmacro:default', shell=True)  # make hexfile
    return


# function to check and allow user to select directory

def getDirectory(dirFrame):
    global qmkdir
    qmkdir = filedialog.askdirectory(parent=root, initialdir="/", title="Select your qmk_firmware directory: ")
    while os.path.basename(qmkdir) != firmware and qmkdir != '':  # if doesnt return empty string
        qmkdir = filedialog.askdirectory(mustexist=True, title="Select your qmk_firmware directory: ")
    dirLabel = tk.Label(dirFrame, pady=.1, text=qmkdir, bg="#52606D", fg="white", font="Helvetica 8").place(relx=0,
                                                                                                            rely=0)
    return qmkdir


# Generic Button Class
class buttonAttributes(tk.Button):
    def __init__(self, frameRef,  rx, ry,widgetFrame,  **kwargs):
        tk.Button.__init__(self, master=frameRef, **kwargs)

        self.config(padx=1, relief="solid", pady=1, fg="#97a4aa", bd=0, highlightthickness=0)
        self.place(relwidth=.2, relheight=.2, relx=rx, rely=ry)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['bg'] = "black"

    def on_leave(self, e):
        self['bg'] = "#293439"


#######################Page Classes#####################################
class pageOne(tk.Frame):
    def __init__(self, frameRoot, **kwargs):
        tk.Frame.__init__(self, root, **kwargs)
        self.place(relwidth=.8, relheight=.7, relx=.1, rely=.1)
        dirFrame = tk.LabelFrame(frameRoot, bg="#52606D", relief="sunken", bd=1)
        dirFrame.place(relwidth=.5, relheight=.1, relx=.3, rely=.26)

        openDir = buttonAttributes(self, .05, .2, dirFrame, text="Show Folder", bg="#293439", command=lambda: getDirectory(dirFrame))

class pageTow(tk.Frame):
    def __init__