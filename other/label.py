from tkinter import *
from tkinter import ttk
root=Tk()

label=ttk.Label(root,text='hello,tkinter!')
label.pack()

label.config(text='howdy.tkinter')
label.config(text='howdy,tkinter!dlkfndsklfsdkl')
label.config(wraplength=150)
label.config(justify=CENTER)
label.config(foreground='blue',background='red')
label.config(font=('courier',18,'bold'))

PhotoImage(file='/Users/vadim/Pictures/usa-map.gif')
usamap=PhotoImage(file='/Users/vadim/Pictures/usa-map.gif')
label.config(image=usamap)
