from tkinter import messagebox

messagebox.showinfo(title='a friendly message',message='hello,tkinter!')
messagebox.askyesno(title='hungry?',message='do you want spam?')

from tkinter import filedialog

filename=filedialog.askopenfile()
filename.name('/Users/vadim/Pictures/usa-map.gif')

from tkinter import colorchooser
colorchooser.askcolor(initialcolor='#FFFFFF')