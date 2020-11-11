from tkinter import *
from tkinter import ttk
root=Tk()

Label(root,text='Executing Fibonacci').pack()

def callback1():
    a,b=0,1
    num=int(input('Enter number: '))
    while b<num:
        print(b,end=' ',flush=True)
        a,b=b,a+b
    print()

ttk.Button(root,text='Start',command=callback1).pack()
root.mainloop()