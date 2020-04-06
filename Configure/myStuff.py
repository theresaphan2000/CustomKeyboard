import subprocess
import os
import tkinter as tk
from tkinter import filedialog, Text

root = tk.Tk()

def getQMKDirect():
    path = input('Enter your full path the qmk_firmware directory: ')
    while os.path.isdir(path) == False or os.path.basename(path) != 'qmk_firmware':
        path = input('Path error. Enter your full path the qmk_firmware directory: ')


    p1 = subprocess.check_call('ls', shell=True, cwd=path) #list directory, use shell, change current working directory to path give
    return


