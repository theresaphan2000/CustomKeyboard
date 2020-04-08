#!/usr/bin/env python3
from interfaceFunctions import *

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()  # needed fill, exapnd, a geometry manager

frame = tk.Frame(root, bg="white")
frame.place(relwidth=.8, relheight=.7, relx=.1, rely=.1)



openDir = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42", command=getDirectory)
openDir.pack()  # packs openFile

# Border Label window
dirBox = tk.Label(root, text=ULTIMATEPATH, borderwidth=1, relief="solid", font="Helvetica 32")
dirBox.pack()

# Pull old contents of c file
runApps = tk.Button(root, text="Run App", padx=10,
                    pady=5, fg="white", bg="#263D42")
runApps.pack()  # packs openFile

root.mainloop()
