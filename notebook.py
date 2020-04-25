from tkinter import *
from tkinter import ttk 
root=Tk()

notebook=ttk.Notebook(root)
notebook.pack()

frame1=ttk.Frame(notebook)
frame2=ttk.Frame(notebook)

notebook.add(frame1,text='one')
notebook.add(frame2,text='two')
ttk.Button(frame1,text='click me').pack()

frame3=ttk.Frame(notebook)

notebook.insert(1,frame3,text='three')
notebook.forget(1)
notebook.add(frame3,text='three')

