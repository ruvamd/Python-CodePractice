from tkinter import *
from tkinter import ttk 
root=Tk()

checkbutton=ttk.Checkbutton(root,text='spam?')
checkbutton.pack()
spam=StringVar()
spam.set('SPAM!')
checkbutton.config(variable=spam,onvalue='SPAM Please!',offvalue='Boo SPAM')
breakfast=StringVar()

ttk.Radiobutton(root,text='SPAM',variable=breakfast,value='SPAM').pack()
ttk.Radiobutton(root,text='Eggs',variable=breakfast,value='Eggs').pack()
ttk.Radiobutton(root,text='Sausage',variable=breakfast,value='Sausage').pack()
ttk.Radiobutton(root,text='SPAM',variable=breakfast,value='SPAM').pack()
checkbutton.config(textvariable=breakfast)