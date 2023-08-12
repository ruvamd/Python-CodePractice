from tkinter import *
root=Tk()

canvas=Canvas(root)
canvas.pack()
canvas.config(width=640,height=480)

line=canvas.create_line(160,360,480,120,fill='blue',width=5)

canvas.itemconfigure(line,fill='green')
canvas.coords(line)
canvas.coords(line,0,0,320,240,640,0)
canvas.itemconfigure(line,smooth=True)
canvas.itemconfigure(line,splinesteps=5)
canvas.itemconfigure(line,splinesteps=100)
canvas.delete(line)

rect=canvas.create_rectangle(160,120,480,360)

canvas.itemconfigure(rect,fill='yellow')

oval=canvas.create_oval(160,120,480,360)
arc=canvas.create_arc(160,1,480,240)

canvas.itemconfigure(arc,start=0,extent=180,fill='green')

poly=canvas.create_polygon(160,360,320,480,480,360,fill='blue')
text=canvas.create_text(320,240,text='python',font=('courier',32,'bold'))
logo=PhotoImage(file='/Users/vadim/Pictures/hiragana.jpg')
image=canvas.create_image(320,240,image=logo)

canvas.lift(text)
canvas.lower(image)
canvas.lower(image,text)

button=Button(canvas,text='click me')

canvas.create_window(320,60,window=button)
canvas.itemconfigure(rect,tag=('shape'))
canvas.itemconfigure(oval,tag=('shape','round'))
canvas.itemconfigure('shape',fill='grey')
canvas.gettags(oval)



