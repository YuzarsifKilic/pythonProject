import tkinter as tk
from tkinter import ttk
import os
from videoprops import get_video_properties
import glob
import subprocess

g = glob.glob("*.mp4")

videoList = []

for file in g:
    fileSize = len(str(round(os.path.getsize(file)/1024, 2)))
    word = len(str(file))
    initialSpace = str(file)
    props = get_video_properties(file)
    width = props["width"]
    height = props["height"]
    while word < 25:
        word = word + 1
        initialSpace = initialSpace + " "
    initialSpace = initialSpace + str(round(os.path.getsize(file)/1024, 2)) + " " + str(width) + " x " + str(height)
    videoList.append(initialSpace)

root = tk.Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title("Radio Button Demo")

selected_size = tk.StringVar()
sizes = (("Scaling", 0),
         ("Compression", 1))

var2 = tk.StringVar()
var2.set(videoList)


def select():
    print("asdfasdf")


for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size)
    r.pack(fill="x", padx=5, pady=5)


lb = tk.Listbox(root, listvariable=var2, width=50)

lb.pack()
button = ttk.Button(
    root,
    text="Get Selected Size",
    command=select
)

button.pack(fill="x", padx=5, pady=5)


root.mainloop()