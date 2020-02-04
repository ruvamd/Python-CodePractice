from tkinter import *
from tkinter import ttk 
root=Tk()
label1=ttk.Label(root,text='label 1')
label2=ttk.Label(root,text='label 2')
label1.pack()
label2.pack()
label1.bind('<ButtonPress>',lambda e:print('<buttonPress>label'))
label1.bind('<1>',lambda e:print('<1> label'))
root.bind('<1>',lambda e:print('<1>root'))
label1.unbind('<1>')
label1.unbind('<ButtonPress>')
root.bind_all('<Escape>',lambda e:print('escape!'))
root.mainloop()
