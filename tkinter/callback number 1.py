from tkinter import *
from tkinter import ttk 
root=Tk()

def callback(number):
    print(number)

ttk.Button(root,text='1',command=lambda:callback(1)).pack()
ttk.Button(root,text='2',command=lambda:callback(2)).pack()
ttk.Button(root,text='3',command=lambda:callback(3)).pack()

root.mainloop()
