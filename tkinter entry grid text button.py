from tkinter import*
window=Tk()

def kmToMi():
    print(entryValue.get())
    miles=float(entryValue.get())*1.6
    text.insert(END,miles)

button=Button(window,text='click',command=kmToMi)
button.grid()

entryValue=StringVar()
entry=Entry(window,textvariable=entryValue)
entry.grid(row=0,column=1)

text=Text(window,height=1,width=20)
text.grid(row=0,column=2)

window.mainloop()
