from tkinter import *
win=Tk()

win.title('conv year sal to the hour range')

label=Label(win,text='Enter the year salary: ')
label.pack()

def closeWindow():
    exit()
button=Button(win,text='close window',command=closeWindow)
button.pack()

win.mainloop()

