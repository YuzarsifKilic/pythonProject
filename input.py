import tkinter as tk
from tkinter import ttk
import os
from videoprops import get_video_properties
import glob
import subprocess
from tkinter import *
from tkinter import ttk
win=Tk()

win.geometry("750x250")

entry = tk.Entry(win)

def a():
   print(entry.get())

entry.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 20, command= a).pack(pady=20)

win.mainloop()