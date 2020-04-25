from tkinter import *
from tkinter import ttk 
root=Tk()

ttk.Label(root,text='hello,tkinter!',background='yellow').pack(fill=BOTH,expand=True)
ttk.Label(root,text='hello,tkinter!',background='blue').pack(fill=BOTH)
ttk.Label(root,text='hello,tkinter!',background='green').pack(fill=BOTH,expand=True)

root.mainloop()