from tkinter import *

win = Tk()
win.geometry("480x200")
win.title("My first GUI program")
label = Label(win,text="Hello World") 
label1 = Label(win,text="Howdy! What does a mere human have to do here?")

label.grid(row=1,column=0)
label1.grid(row=0,column=0)

win.config(background="#333333")

win.mainloop()