from tkinter import *
from tkinter import ttk 
root=Tk()
def callback():
    print('in the callback')
ttk.Button(root,text='click me!',command=callback).pack()
root.mainloop()
