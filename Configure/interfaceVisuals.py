#!/usr/bin/env python3
from interfaceFunctions import *

##################################################GUI DISPLAY FRAMES ##############################################################################

# def dirScreen():
#     global root
#     # FRAME
#     frame = tk.Frame()
#     frame.config(relief="solid", highlightthickness=1, highlightbackground="#97a4aa")
#     frame.place(relwidth=.8, relheight=.7, relx=.1, rely=.1)
#     # Border Label window
#     dirFrame = tk.LabelFrame(root, bg="#52606D", relief="sunken", bd=1)
#     dirFrame.place(relwidth=.5, relheight=.1, relx=.3, rely=.26)
#
#     openDir = buttonAttributes(frame, .05, .2, text="Show Folder", bg="#293439", command=lambda: getDirectory(dirFrame))
#
#     # nextButton = buttonAttributes(frame, .65, .6, text="Next", bg="#293439", command=nextButtonFunction)
#     root.mainloop()


def main():
    global root
    dirScreen = pageOne(root, bg="#293439", relief="solid", highlightthickness=1,highlightbackground="#97a4aa")

    root.mainloop()

main()
