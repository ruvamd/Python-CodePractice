import tkinter
from tkinter import *
from tkinter import ttk 
root=Tk()

entry=ttk.Entry(root)
entry.pack()
entry.bind('<<copy>>',lambda e:print('copy'))
entry.bind('<<paste>>',lambda e:print('paste'))

entry.event_add('<<OddNumber>>','1','3','5','7','9')

entry.bind('<<OddNumber>>',lambda e: print('Odd Number!'))

print(entry.event_info('<<OddNumber>>'))

entry.event_generate('<<OddNumber>>')
entry.event_generate('<<paste>>')

root.mainloop()