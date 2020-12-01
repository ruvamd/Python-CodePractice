from tkinter import *
from tkinter import ttk 
root=Tk()
def keyPress(event):
    print(f'type:{event.type}')
    print(f'widget:{event.widget}')
    print(f'char:{event.char}')
    print(f'keysym:{event.keysym}')
    print(f'keycode:{event.keycode}')
def shortcut(action):
    print(action)
root.bind('<Command-c>',lambda e:shortcut('copy'))
root.bind('<Command-v>',lambda e:shortcut('paste'))
root.mainloop()