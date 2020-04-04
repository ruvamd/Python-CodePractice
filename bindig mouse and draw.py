from tkinter import*
from tkinter import ttk 
root=Tk()

def mousePress(event):
    global prev
    prev=event
canvas=Canvas(root,width=640,height=480,background='white')
canvas.pack()
def draw(event):
    global prev
    canvas.create_line(prev.x,prev.y,event.x,event.y,width=5)
    prev=event
canvas.bind('<ButtonPress>',mousePress)
canvas.bind('<B1-Motion>',draw)
root.mainloop()
