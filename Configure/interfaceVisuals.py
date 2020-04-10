#!/usr/bin/env python3
from interfaceFunctions import *


def dirScreen():
    root.title("hello")
    root.geometry("500x200")
    root.configure(background='#21292d')

    # FRAME
    frame = tk.Frame(root, bg="#293439")
    frame.config(relief="solid", highlightthickness=1, highlightbackground="#97a4aa")
    frame.place(relwidth=.8, relheight=.7, relx=.1, rely=.1)
    # Border Label window
    dirFrame = tk.LabelFrame(root, bg="#52606D", relief="sunken", bd=1)
    dirFrame.place(relwidth=.5, relheight=.1, relx=.3, rely=.26)

    openDir = buttonAttributes(frame, .05, .2, text="Show Folder", bg="#293439", command=getDirectory)
    nextButton = buttonAttributes(frame, .05, .5, text="Next", bg="#293439", command=getDirectory)
    dirLabel = tk.Label(dirFrame, pady=.1, text=qmkdir, bg="#52606D", fg="white", font="Helvetica 8").place(relx=0,rely=0)
    print(qmkdir)
    root.update()

    root.mainloop()


dirScreen()
