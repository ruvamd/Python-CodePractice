from tkinter import *
from tkinter import ttk 
root=Tk()
month=StringVar()
combobox=ttk.Combobox(root,textvariable=month)
combobox.pack()
combobox.config(values=('jan','feb','march','april','may',
                        'jul','aug','sep','oct','nov','dec'))
month.get()
'mar'
month.set('choose month')
month.get()
year=StringVar()
Spinbox(root,from_=2000,to=2019,textvariable=year).pack()