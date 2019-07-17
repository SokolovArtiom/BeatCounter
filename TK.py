from tkinter import *
from main import main

def start():
    p=message.get()
    out=main(p)
    edit2.insert(1.0, out)

def delete():
    edit2.delete(1.0, END)
    
def copy():
    cop=StringVar()
    cop=edit2.get(1.0, END)
    win.clipboard_append(cop)
    
win=Tk()
win.geometry('500x400')

t1 = Label(win, text='Enter file name', fg='black')
t1.config(font=('Veranda', 15))
t1.pack()

message=StringVar()
edit1 = Entry (win, textvariable=message, width = 25, bg='white').pack()

button1=Button(win, text='Start', width=15, height=2, font='Veranda 15', command=start)
button1.pack()

button2=Button(win, text='Clear', width=15, height=2, font='Veranda 15', command=delete)
button2.pack()

edit2 = Text (win, height=15, width=50, bg='white')
edit2.pack()

button3=Button(win, text='Copy', width=15, height=2, font='Veranda 15', command=copy)
button3.pack()

win.mainloop()