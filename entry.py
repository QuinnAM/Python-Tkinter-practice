from tkinter import *

root = Tk()

e = Entry(root)
e.pack()

def my_click():
    hello = "hello there " + e.get()
    my_label = Label(root, text = hello)
    my_label.pack()


my_button = Button(root, text = "Enter your name:", command = my_click)
my_button.pack()

root.mainloop()






