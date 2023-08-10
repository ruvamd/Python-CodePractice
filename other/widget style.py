from tkinter import *
from tkinter import ttk 
root=Tk()

button1=ttk.Button(root,text='button 1')
button2=ttk.Button(root,text='button 2')
button1.pack()
button2.pack()

style=ttk.Style()
#style.theme_names()
style.theme_use('classic')
style.theme_use('alt')

button1.winfo_class()

style.configure('TButton',foreground='blue')
style.configure('Alarm.TButton',foreground='orange',font=('Arial',24,'bold'))

button2.config(style='Alarm.TButton')
style.map('Alarm.TButton',foreground=[('pressed','pink'),('disabled','grey')])
button2.state(['disabled']) 