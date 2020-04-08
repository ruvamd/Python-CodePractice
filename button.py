from tkinter import *
from tkinter import ttk 
root=Tk()

button=ttk.Button(root,text='click me')
button.pack()

def callback():
    print('clicked!')

button.config(command=callback)
button.invoke()
button.state(['disabled'])
button.instate(['disabled'])
button.state(['!disabled'])
('disabled',)

logo=PhotoImage(file='/Users/vadim/Pictures/usa-map.gif')

button.config(image=logo,compound=LEFT)

smallLogo=logo.subsample(5,5)
button.config(image=smallLogo)