from tkinter import *
win=Tk()
win.title('conv year sal to the hour range')

label=Label(win,text='Enter the year salary: ')
label.pack()

def close():
    exit()
button=Button(win,text='close',command=close)
button.pack()

# yearSal=int(input('Enter the year salary: '))
# def convYearToHourSal():
#     return round(yearSal/12/4/5/8,2)

# print(f'The annual ${yearSal} salary in the hour is: {convYearToHourSal()}')

win.mainloop()
