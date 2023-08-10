from tkinter import *
root=Tk()

window=Toplevel(root)
window.title('new window')
window.lower()
window.lift(root)
window.state('zoomed')
