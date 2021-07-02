from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Hello World!").pack()


mybutton = Button(root, text="Click me!", command=myClick)
mybutton.pack()

root.mainloop()
