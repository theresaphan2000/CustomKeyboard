#!/usr/bin/env python
import tkinter
from tkinter import *
from tkinter import messagebox




def main():
    root = tkinter.Tk()
    root.geometry("800x800")

    photo = PhotoImage(file="buttonPic.png")

    btn = Button(root, text="hi", fg="white",activeforeground="white",image=photo, border=0, compound="center")
    btn.image = photo
    btn.pack()

    root.mainloop()


main()
