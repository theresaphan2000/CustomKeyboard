#!/usr/bin/env python3
from interfaceFunctions import *
#
class buttonAttributes(tk.Button):
    def __init__(self,  frameRef,rx ,ry ,**kwargs):

        tk.Button.__init__(self, master=frameRef, **kwargs)

        self.config(padx=1, relief="solid", pady=1, fg="#97a4aa", bd=0, highlightthickness=0)
        self.place(relwidth=.2, relheight=.2, relx=rx, rely=ry)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['bg']= "black"

    def on_leave(self,e):
        self['bg'] = "#293439"




def main():
    root.title("hello")
    root.geometry("500x200")
    root.configure(background='#21292d')
# # CANVAS
#     canvas = tk.Canvas(root, height=200, width=500, bg="pink")
#     canvas.grid(row=0, column=1)  # needed fill, exapnd, a geometry manager
#     canvas.update()

#FRAME
    frame = tk.Frame(root, bg="#293439")
    frame.config(relief="solid", highlightthickness=1,highlightbackground="#97a4aa" )
    frame.place(relwidth=.8, relheight=.7, relx=.1, rely=.1)
    # Border Label window

    openDir = buttonAttributes(frame, .05, .2,  text="Show Folder", command=getDirectory)
    newDir = buttonAttributes( frame, .5, .5, text="Show Folder", command=getDirectory)

    root.mainloop()


main()
