from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    strin = strftime("%H:%M:%S %p")
    label.config(text= strin)
    label.after(2000, time)

label = Label(  root, font="ds-digital,80", background= 'black', foreground= "red")
label.pack(anchor= "center")
time()

mainloop()