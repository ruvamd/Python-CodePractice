from tkinter import*
from tkinter import ttk 
root=Tk()

root.bind('<a>',lambda e:print('a'))
root.bind('<e>',lambda e:print('e'))
root.mainloop()
