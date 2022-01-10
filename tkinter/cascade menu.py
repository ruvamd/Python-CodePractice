from tkinter import *
root=Tk()

root.option_add('*tearOff',False)

menubar=Menu(root)
root.config(menu=menubar)

file=Menu(menubar)
edit=Menu(menubar)
help_=Menu(menubar)

menubar.add_cascade(menu=file,label='File')
menubar.add_cascade(menu=edit,label='Edit')
menubar.add_cascade(menu=help_,label='Help')

file.add_command(label='New',command=lambda:print('New File'))
file.add_separator()
file.add_command(label='open...',command=lambda:print('opening file...'))
file.add_command(label='save',command=lambda:print('save File'))
file.entryconfig('New',accelerator='Ctrl+N')
logo=PhotoImage(file='/Users/vadim/Pictures/usa-map.gif').subsample(5,5)
file.entryconfig('open...',image=logo,compound='left')

save=Menu(file)
file.add_cascade(menu=save,label='save')
save.add_command(label='save as',command=lambda:print('saving as...'))
save.add_command(label='save all',command=lambda:print('saving all...'))

choice=IntVar()
edit.add_radiobutton(label='one',variable=choice,value=1)
edit.add_radiobutton(label='two',variable=choice,value=2)
edit.add_radiobutton(label='three',variable=choice,value=3)
file.post(400,300)
