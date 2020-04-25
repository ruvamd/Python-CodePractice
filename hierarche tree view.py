from tkinter import *
from tkinter import ttk 
root=Tk()

treeview=ttk.Treeview(root)
treeview.pack()

treeview.insert('','0','item1',text='first item')
treeview.insert('','1','item2',text='second item')
treeview.insert('','end','item3',text='third item')

logo=PhotoImage(file='/Users/vadim/Pictures/usa-map.gif').subsample(10,10)

treeview.insert('item2','end','python',text='python',image=logo)
treeview.move('item2','item1','end')
treeview.column('version',width=50,anchor='center')
treeview.column('#0',width=150)
treeview.heading('version',text='version')
treeview.set('python','version','3.8.0')
treeview.item('python',tags=('software'))
treeview.tag_configure('software',background='yellow')

def callback(event):
    print(treeview.selection())
treeview.bind('<<TreeviewSelect>>',callback)