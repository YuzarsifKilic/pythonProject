import tkinter as tk
from tkinter import ttk
import os
from tkinter.ttk import Entry, Label, Button

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



for a in videoList:
    print(a)

root = tk.Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title("Radio Button Demo")

def open_select_video_window():
    new = tk.Toplevel(root)
    new.geometry("500x500")
    new.title("Select a video")
    var2 = tk.StringVar()
    var2.set(videoList)
    size = selected_size.get()
    def do_it():
        if size == "0":
            for item in lb.curselection():
                scale(item)
        elif size == "1":
            for item in lb.curselection():
                get_input = tk.Toplevel(new)
                get_input.geometry("300x300")
                width = tk.Label(get_input, text="width")
                width_input = tk.Entry(get_input)
                height = tk.Label(get_input, text="height")
                height_input = tk.Entry(get_input)
                def save():
                    compress(item, width_input.get(), height_input.get())
                height.pack()
                height_input.pack()
                width.pack()
                width_input.pack()
                submit = Button(get_input, text="Kaydet",command=save).place(x = 30, y = 100)
    lb = tk.Listbox(new, listvariable=var2, width=50)
    lb.pack()
    b1 = tk.Button(new, text='Seç', width=15, height=2, padx=10, pady=10, command=do_it)
    b1.pack()



def scale(item):
    subprocess.run("ffmpeg -i " + g[item] + " New" + g[item])

def compress(item, width, height):
    subprocess.run("ffmpeg -i " + g[item] +
                   " -vf scale=" + height +
                   ":" + width +
                   " " + width + "_" + height + g[item])
selected_size = tk.StringVar()
sizes = (("Scaling", 0),
         ("Compression", 1))


for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size)
    r.pack(fill="x", padx=5, pady=5)

button = ttk.Button(
    root,
    text="Get Selected Size",
    command=open_select_video_window
)

button.pack(fill="x", padx=5, pady=5)


root.mainloop()
