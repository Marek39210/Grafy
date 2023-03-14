# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:12:08 2023

@author: mvojt
"""
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import pylab as pl

def close_window():
    window.destroy()

def choose_file():
    filename = filedialog.askopenfilename()
    if filename:
        chosen_file_label.config(text="Vybraný soubor: " + filename)
        show_button.config(state="normal", command=lambda: show_values(filename))
    else:
        chosen_file_label.config(text="")
        show_button.config(state="disabled", command=None)
def show_values(filename):
    if not filename:
        messagebox.showerror("Error", "Nevybrán žádný soubor!")
        return
    x = []
    y = []

    if data_dir.get() == 'RAD':
        with open(filename, "r") as file:
            line = file.readline()
            x = line.split(';')
            line = file.readline()
            y = line.split(';')
            x = [float(i.replace(',','.')) for i in x]
            y = [float(q.replace(',','.')) for q in y]

    elif data_dir.get() == 'SLOUP':
        with open(filename, "r") as file:
            for line in file:
                x, y = line.split()
                x = x + (float(x))
                y = y + (float(y))
    print(x)
    plt.plot(x,y, 'b.-')
    plt.title("Graph")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.show()

window = tk.Tk()
window.geometry("450x100+100+50")

window.title("Grafy")

label = tk.Label(window, text="Zobrazte si svůj graf")
label.pack()

button_frame = tk.Frame(window)
button_frame.pack(padx=5, pady=5)

show_button = tk.Button(button_frame, text="Show", state="disabled")
show_button.pack(side="left")

choose_button = tk.Button(button_frame, text="Choose", command=choose_file)
choose_button.pack(side="left")

quit_button = tk.Button(button_frame, text="Quit", command=close_window)
quit_button.pack(side="left")

sloup_frame = tk.Frame(button_frame)
sloup_frame.pack(anchor='s')

data_dir = tk.StringVar()
button_rad = tk.Radiobutton(sloup_frame, text = 'Data jsou v řádních',variable=data_dir,value='RAD')
button_rad.pack(anchor='w')
button_sloup = tk.Radiobutton(sloup_frame, text = 'Data jsou ve sloupcích',variable=data_dir,value='SLOUP')
button_sloup.pack(anchor='e')

chosen_file_label = tk.Label(window, text="")
chosen_file_label.pack()

window.mainloop()