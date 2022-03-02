from tkinter import *
import n
n.test()
window = Tk()
window.geometry("420x420")
window.title("My first GUI program")
label = Label(window,text="Hello World")
label.pack()


window.config(background="#000000")

window.mainloop()