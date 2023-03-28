# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:12:08 2023

@author: mvojt
"""
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import pylab as pl


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)


def close_window():
    window.destroy()

def choose_file():
    filename = filedialog.askopenfilename()
    if filename:
        chosen_file_label.config(text=filename)
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
            x = []
            y = []
            while True:
                line = file.readline()
                if line =='':
                    break
                if ';' not in line:
                    continue
                x1,y1 = line.split(';')
                x.append(float(x1.replace(',','.')))
                y.append(float(y1.replace(',','.')))
    print(x)
    plt.plot(x,y, linestyle = lineVar.get(), marker = marker.get(), markerfacecolor = markbarva.get(), markeredgecolor = markbarva.get(), color = barva.get())
    plt.title(titleEntry.value)
    plt.xlabel(xlabelEntry.value)
    plt.ylabel(ylabelEntry.value)
    plt.show()



window = tk.Tk()
window.geometry("570x320")

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
sloup_frame.pack(anchor='e')

data_dir = tk.StringVar()
button_rad = tk.Radiobutton(sloup_frame, text = 'Data jsou v řádních',variable=data_dir,value='RAD')
button_rad.pack(anchor='w')
button_sloup = tk.Radiobutton(sloup_frame, text = 'Data jsou ve sloupcích',variable=data_dir,value='SLOUP')
button_sloup.pack(anchor='w')

graf_frame = tk.LabelFrame(sloup_frame, text='GRAF')
graf_frame.pack(padx = 5,pady = 5, fill = 'x', anchor='s')

tk.Label(graf_frame, text='Titulek').grid(row=0,column=0)
titleEntry = MyEntry(graf_frame)
titleEntry.grid(row=0,column=1)

tk.Label(graf_frame,text='osa X').grid(row = 1, column = 0)
xlabelEntry = MyEntry(graf_frame)
xlabelEntry.grid(row = 1, column = 1)

tk.Label(graf_frame,text='osa Y').grid(row = 2, column = 0)
ylabelEntry = MyEntry(graf_frame)
ylabelEntry.grid(row = 2, column = 1)

tk.Label(graf_frame,text='STYL ČÁRY').grid(row = 3, column = 0)
lineVar = tk.StringVar(value='none')
tk.OptionMenu(graf_frame,lineVar,'none','-','-.','--',':').grid(row=3,column=2, sticky='w')

tk.Label(graf_frame,text='Marker').grid(row = 4, column = 0)
marker = tk.StringVar(value='none')
tk.OptionMenu(graf_frame,marker,*tuple('.,o+PxX*1234<>v')).grid(row=4,column=2, sticky='w')

tk.Label(graf_frame,text='ČÁRA').grid(row = 5, column = 0)
barva = tk.StringVar(value='black')
tk.OptionMenu(graf_frame,barva,'green','blue','red','orange','black').grid(row=5,column=2, sticky='w')

tk.Label(graf_frame,text='MARKER').grid(row = 6, column = 0)
markbarva = tk.StringVar(value='black')
tk.OptionMenu(graf_frame,markbarva,'green','blue','red','orange','black').grid(row=6,column=2, sticky='w')



chosen_file_label = tk.Label(window, text="")
chosen_file_label.pack()

window.mainloop()