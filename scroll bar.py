from tkinter import *
from tkinter import ttk 
root=Tk()
text=Text(root,width=40,height=10,wrap='word')
text.grid(row=0,column=0)
scrollbar=ttk.Scrollbar(root,orient=VERTICAL,command=text.yview)
text.config(yscrollcommand=scrollbar.set)