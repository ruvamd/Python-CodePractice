import tkinter
import time
def alarm():
    print('calling the pizza company')
def doorbell():
    print('ding dong')
    time.sleep(4)
    print('opening the door')
def phonecall():
    print('answering the phone')
root=tkinter.Tk()
tkinter.Button(root,text='ring doorbell',command=doorbell).pack()
tkinter.Button(root,text='call phone',command=phonecall).pack()

