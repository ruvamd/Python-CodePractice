from tkinter import *
from tkinter import ttk 
root=Tk()
def mousePress(event):
    global prev
    prev=event
    print(f'type:{event.type}')
    print(f'widget:{event.widget}')
    print(f'num:{event.num}')
    print(f'x:{event.x}')
    print(f'y:{event.y}')
    print(f'x_root:{event.x_root}')
    print(f'y_root:{event.y_root}')
canvas=Canvas(root,width=640,height=480,background='white')
canvas.pack()
def draw(event):
    global prev
    canvas.create_line(prev.x,prev.y,event.x,event.y,width=5)
    prev=event
canvas.bind('<ButtonPress>',mousePress)
canvas.bind('<B1-Motion>',draw)
root.mainloop()