#!/usr/bin/env python3
import subprocess
from subprocess import *
import threading
import queue
from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import os
from miscDef import *
import re

# --------------------------------------------------------------------------------------------------


# root used in interfaceVisuals.py
root = tk.Tk()  # needed " think of it as a base'
root.title("beesKeys Macro Editor")
root.geometry("500x200")
root.configure(background=color["root"])


# Function that stores user input for keymapping
# os system to change directory to qmk_firmware folder etc

def makeHex(path):
    subprocess.run('make beesKeys:all', shell=False, cwd=path)  # making hex file


# function to check and allow user to select directory
def getDirectory(dirFrame):
    global qmkdir
    qmkdir = filedialog.askdirectory(parent=root, initialdir="/", title="Select your qmk_firmware directory: ")
    while os.path.basename(qmkdir) != firmware and qmkdir != '':  # if doesnt return empty string
        qmkdir = filedialog.askdirectory(mustexist=True, title="Select your qmk_firmware directory: ")
    dirLabel = tk.Label(dirFrame, pady=.1, text=qmkdir, bg=color["hl"], fg="#97a4aa", font="Helvetica 10").place(
        relx=.05,
        rely=.02)
    return qmkdir


def capFile(path):
    f1 = open(path + "/keyboards/beesKeys/keymaps/default/keymap.c", mode="r")
    f2 = open(path + "/keyboards/beesKeys/keymaps/default/keymap2.c", mode="w")
    for line in f1:
        for i in range(len(key)):
            if line.startswith("#define ") and remap[i] in line:
                line = "#define " + key[i] + "\n"
        f2.write(line)


def OnButtonClick(button_id):
    key[button_id] = temp[button_id].get();
    print(key[button_id])


# Generic Button Class
class buttonAttributes(tk.Button):
    def __init__(self, frameRef, **kwargs):
        tk.Button.__init__(self, master=frameRef, **kwargs)

    def baseButtons(self, rx, ry):
        self.config(padx=1, relief="solid", pady=1, fg="#97a4aa", bd=0, highlightthickness=0)
        self.place(width=90, height=28, relx=rx, rely=ry)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['bg'] = "#312320"

    def on_leave(self, e):
        self['bg'] = color["fBg"]

    def addImage(self, r, c, photo):
        self.configure(fg="white", activeforeground="white", image=photo, border=0, compound="center", bg="#595959",
                       activebackground="#595959")
        self.image = photo
        self.place(width=98, height=60, relx=r, rely=c)


#######################Key Button#########################################

#######################Page Base #########################################
class mainFrame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.grid(row=0, column=0, sticky="nsew")
        self.frames = {}
        frame = pageOne(container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(pageOne)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()


#######################Page Classes 1#####################################

class pageOne(tk.Frame):
    def __init__(self, root, **kwargs):
        tk.Frame.__init__(self, root, **kwargs)
        self.config(bg=color["fBg"], relief="solid", highlightthickness=1, highlightbackground=color["hl"])
        self.place(relwidth=3, relheight=.7, relx=-1, rely=.1)

        # frame holding directory path
        dirFrame = tk.LabelFrame(self, bg=color["hl"], relief="sunken", bd=1)
        dirFrame.place(relwidth=.25, height=28, relx=.4, rely=.2)

        openDir = buttonAttributes(self, text="Select Folder: ", bg=color["fBg"],
                                   command=lambda: getDirectory(dirFrame)).baseButtons(.35, .2)
        next = buttonAttributes(self, text="Next", bg=color["fBg"]).baseButtons(.55, .7, )


temp = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
        StringVar()]


########################Page Classes 2 #####################################
class pageTwo(tk.Frame):
    global key

    def __init__(self, frameRoot, **kwargs):
        root.geometry("800x650")
        root.resizable(False, False)
        tk.Frame.__init__(self, frameRoot, **kwargs)
        self.config(bg=color["fBg"], relief="solid", highlightthickness=1, highlightbackground=color["hl"])
        self.place(relwidth=3, relheight=.9, relx=-1, rely=.05)

        makeImg = PhotoImage(file="makeImg.png")
        img = PhotoImage(file="buttonPic.png")
        x = .365
        y = .1

        ent1 = tk.Entry(self, relief=FLAT, state=NORMAL, textvariable=temp[0]).place(relx=x + .04, rely=y + .03)
        ent2 = tk.Entry(self, relief=FLAT, state=NORMAL, textvariable=temp[1]).place(relx=x + .13, rely=y + .03)
        ent3 = tk.Entry(self, relief=FLAT, state=NORMAL, textvariable=temp[2]).place(relx=x + .22, rely=y + .03)
        ent4 = tk.Entry(self, relief=FLAT, state=NORMAL, textvariable=temp[3]).place(relx=x + .04, rely=y + .19)
        ent5 = tk.Entry(self, relief=FLAT, state=NORMAL, textvariable=temp[4]).place(relx=x + .13, rely=y + .19)
        ent6 = tk.Entry(self, relief=FLAT, state=NORMAL, textvariable=temp[5]).place(relx=x + .22, rely=y + .19)
        ent7 = tk.Entry(self, relief=FLAT, state=NORMAL, textvariable=temp[6]).place(relx=x + .04, rely=y + .34)
        ent8 = tk.Entry(self, relief=FLAT, state=NORMAL, textvariable=temp[7]).place(relx=x + .13, rely=y + .34)
        ent9 = tk.Entry(self, relief=FLAT, state=NORMAL, textvariable=temp[8]).place(relx=x + .22, rely=y + .34)

        b1 = buttonAttributes(self, text="1", command=lambda: OnButtonClick(0)).addImage(x, y, img)
        b2 = buttonAttributes(self, text="2", command=lambda: OnButtonClick(1)).addImage(x + .09, y, img)
        b3 = buttonAttributes(self, text="3", command=lambda: OnButtonClick(2)).addImage(x + .18, y, img)
        b4 = buttonAttributes(self, text="4", command=lambda: OnButtonClick(3)).addImage(x, y + .15, img)
        b5 = buttonAttributes(self, text="5", command=lambda: OnButtonClick(4)).addImage(x + .09, y + .15, img)
        b6 = buttonAttributes(self, text="6", command=lambda: OnButtonClick(5)).addImage(x + .18, y + .15, img)
        b7 = buttonAttributes(self, text="7", command=lambda: OnButtonClick(6)).addImage(x, y + .3, img)
        b8 = buttonAttributes(self, text="8", command=lambda: OnButtonClick(7)).addImage(x + .09, y + .3, img)
        b9 = buttonAttributes(self, text="9", command=lambda: OnButtonClick(8)).addImage(x + .18, y + .3, img)

        makeButton = buttonAttributes(self, text="MAKE", command=lambda: makeHex(qmkdir)).addImage(.4, .6, makeImg)
        remap = buttonAttributes(self, text="REMAP", command=capFile(qmkdir)).addImage(.55, .6, makeImg)
