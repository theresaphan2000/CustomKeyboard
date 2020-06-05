#!/usr/bin/env python3
import subprocess
from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import os
from miscDef import *

# --------------------------------------------------------------------------------------------------


# root used in interfaceVisuals.py
root = tk.Tk()  # needed " think of it as a base'
root.title("hello")
root.geometry("500x200")
root.configure(background=color["root"])


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
    dirLabel = tk.Label(dirFrame, pady=.1, text=qmkdir, bg=color["hl"], fg="#97a4aa", font="Helvetica 10").place(
        relx=.05,
        rely=.02)
    return qmkdir





# function that calls next frame
# def nextFrame():


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

    def addImage(self, r, c, photo,num):

        self.configure(fg="white", activeforeground="white", image=photo, border=0, compound="center", bg="#595959", activebackground="#595959")
        #self.grid(row=r, column=c)
        self.image = photo
        self.place(width=60, height=60, relx=r, rely=c)
        self.bind(self.OnButtonClick)

    def OnButtonClick(self, button_id):
        print("Hello")
        # global key
        # key[button_id] = input()
        # self.config(text = key[button_id])



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

        openDir = buttonAttributes(self, text="Select Folder:", bg=color["fBg"], command=lambda: getDirectory(dirFrame)).baseButtons(.35, .2)
        next = buttonAttributes(self, text="Next", bg=color["fBg"]).baseButtons(.55, .7,)


########################Page Classes 2 #####################################
class pageTwo(tk.Frame):
    def __init__(self, frameRoot, **kwargs):
        root.geometry("600x450")
        root.resizable(False,False)
        tk.Frame.__init__(self, frameRoot, **kwargs)
        self.config(bg=color["fBg"], relief="solid", highlightthickness=1, highlightbackground=color["hl"])
        self.place(relwidth=3, relheight=.9, relx=-1, rely=.05)

        img = PhotoImage(file="buttonPic.png")
        x = .365
        y = .1
        #b1 = buttonAttributes(self, command = lambda: b1.OnButtonClick(1)).addImage(x, y,img,0)
        b1 = buttonAttributes(self, command = lambda: b1.OnButtonClick(1)).addImage(x, y, img, 0)
        b2 = buttonAttributes(self, command = lambda: b2.OnButtonClick(2)).addImage(x+.043, y,img,1)
        b3 = buttonAttributes(self, command = lambda: b3.OnButtonClick(3)).addImage(x+.086, y,img,2)
        b4 = buttonAttributes(self, command = lambda: b4.OnButtonClick(4)).addImage(x, y+.15,img,3)
        b5 = buttonAttributes(self, command = lambda: b5.OnButtonClick(5)).addImage(x+.043,y+.15,img,4)
        b6 = buttonAttributes(self, command = lambda: b6.OnButtonClick(6)).addImage(x+.086,y+.15,img,5)
        b7 = buttonAttributes(self, command = lambda: b7.OnButtonClick(7)).addImage(x, y + .3, img,6)
        b8 = buttonAttributes(self, command = lambda: b8.OnButtonClick(8)).addImage(x + .043, y + .3, img,7)
        b9 = buttonAttributes(self, command = lambda: b9.OnButtonClick(9)).addImage(x + .086, y + .3, img,8)
