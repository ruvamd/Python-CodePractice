from tkinter import *
root=Tk()
text=Text(root,width=200,height=100)
text.pack()
text.config(wrap='word')
text.insert('1.0+2 lines','inserted message')
text.insert('1.0+2 lines lineend','and\nmore and\nmore...')
text.tag_add('my_tag','1.0','1.0 wordend')
text.tag_configure('my_tag',background='yellow')
image=PhotoImage(file='/Users/vadim/Pictures/usa-map.gif')
text.image_create('insert',image=image)
button=Button(text,text='click me')
text.window_create('insert',window=button)

