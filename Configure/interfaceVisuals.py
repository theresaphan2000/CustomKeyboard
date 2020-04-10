#!/usr/bin/env python3
from interfaceFunctions import *
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
    dirLabel = tk.Label(dirFrame, pady=.1, text=qmkdir, bg="#52606D", fg="white", font="Helvetica 8").place(relx=0, rely=0)  # FIX ISSUE

    return qmkdir
# def nextButtonFunction():

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

    openDir = buttonAttributes(frame, .05, .2, text="Show Folder", bg="#293439", command= lambda: getDirectory(dirFrame))



    #nextButton = buttonAttributes(frame, .65, .6, text="Next", bg="#293439", command=nextButtonFunction)
    root.update()

    root.mainloop()




def main():
    dirScreen()


main()