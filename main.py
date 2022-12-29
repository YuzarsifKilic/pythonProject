import os
import glob
import tkinter as tk
import subprocess
from tkinter import messagebox
from tkinter import ttk
from videoprops import get_video_properties

g = glob.glob("*.mp4")

videoList = []

for file in g:
    fileSize = len(str(round(os.path.getsize(file)/1024, 2)))
    word = len(str(file))
    initialSpace = str(file)
    props = get_video_properties(file)
    width = props["width"]
    height = props["height"]
    print(width)
    while word < 25:
        word = word + 1
        initialSpace = initialSpace + " "
    initialSpace = initialSpace + str(round(os.path.getsize(file)/1024, 2)) + " " + str(width) + " x " + str(height)
    print(initialSpace)
    videoList.append(initialSpace)


window = tk.Tk()
window.title('Project')

window.geometry('500x300')


path = r"C:\sistemProgramlama"

var2 = tk.StringVar()
var2.set(videoList)


selected_size = tk.StringVar()

print(selected_size.get())

def select():
    for item in lb.curselection():
        ##subprocess.run("ffmpeg -i " + g[item] + " New" + g[item])
        subprocess.run("ffmpeg -i " + g[item] + " -vf scale=720:240 320_240" + g[item])


lb = tk.Listbox(window, listvariable=var2, width=50)

lb.pack()

b1 = tk.Button(window, text='Seç', width=15, height=2, padx= 10, pady=10, command=select)
b1.pack()

window.mainloop()


