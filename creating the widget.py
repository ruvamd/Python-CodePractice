from tkinter import *
from tkinter import ttk
class Feedback:
    def __init__(self,master):
        self.frame_header=ttk.Frame(master)
        
        self.logo=PhotoImage(file='/Users/vadim/Pictures/ca.png')
        ttk.Label(self.frame_header,image=self.logo)
        ttk.Label(self.frame_header,text='thx for exploring')
        ttk.Label(self.frame_header,text=('blablabla')

        self.frame_content=ttk.Frame(master)

        ttk.Label(self.frame_content,text='name:')
        ttk.Label(self.frame_content,text='email:')
        ttk.Label(self.frame_content,text='comments:')

        self.entry_name=ttk.Entry(self.frame_content,width=24)
        self.entry_email=ttk.Entry(self.frame_content,width=24)

        self.text_comments=Text(self.frame_content,width=50,height=10)
        
        ttk.Button(self.frame_content,text='submit')
        ttk.buton(self.frame_content,text='clear')