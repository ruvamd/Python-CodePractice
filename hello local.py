from tkinter import *
from tkinter import ttk
class HelloApp:
    def __init__(self,master):
        self.label=ttk.Label(master,text='hello,Tkinter!')
        self.label.grid(row=0,column=0,columnspan=2)
        ttk.Button(master,text='texas',
                   command=self.texasHello).grid(row=1,column=0)
        ttk.Button(master,text='hawaii',
                   command=self.hawaiiHello).grid(row=1,column=1)
        def texasHello(self):
            self.label.config(text='howdy,tkinter!')
        def hawaiiHello(self):
            self.label.config(text='Aloha,tkinter!')
def main():
    root = Tk()
    app=HelloApp(root)
    root.mainloop()
if __name__=='__main__':main()