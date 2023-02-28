# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:12:08 2023

@author: mvojt
"""
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt

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
    x_values = []
    y_values = []
    with open(filename, "r") as file:
        for line in file:
            x, y = line.split()
            x_values.append(float(x))
            y_values.append(float(y))
    plt.plot(x_values, y_values, 'b.-')
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
button_frame.pack()

show_button = tk.Button(button_frame, text="Show", state="disabled")
show_button.pack(side="left")

choose_button = tk.Button(button_frame, text="Choose", command=choose_file)
choose_button.pack(side="left")

quit_button = tk.Button(button_frame, text="Quit", command=close_window)
quit_button.pack(side="left")

chosen_file_label = tk.Label(window, text="")
chosen_file_label.pack()

window.mainloop()