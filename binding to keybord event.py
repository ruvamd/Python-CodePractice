from tkinter import *
from tkinter import ttk 
root=Tk()
def keyPress(event):
    print('type:{}'.format(event.type))
    print('widget:{}'.format(event.widget))
    print('char:{}'.format(event.char))
    print('keysym:{}'.format(event.keysym))
    print('keycode:{}'.format(event.keycode))
#root.bind('<KeyPress>',keyPress)
def shortcut(action):
    print(action)
root.bind('<Command-c>',lambda e:shortcut('copy'))
root.bind('<Command-v>',lambda e:shortcut('paste'))
root.mainloop()
