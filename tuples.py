import tkinter
def mouse_click(event):
    coords=root.winfo_pointerxy()
    print(f'coords: {coords}')
    print('X: {coords[0]}')
    print('Y: {coords[1]}')
root=tkinter.Tk()
root.bind('<Button>',mouse_click)
root.mainloop()
