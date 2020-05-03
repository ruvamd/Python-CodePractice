from tkinter import *
window=Tk()

button=Button(window,text='click')
button.grid()

entry=Entry(window)
entry.grid(row=0,column=1)

text=Text(window,height=1,width=20)
text.grid(row=0,column=2)

window.mainloop()
