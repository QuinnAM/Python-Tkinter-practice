from tkinter import *

root = Tk()

#Creating a label widget
my_label1 = Label(root, text = "Hello World!")
my_label2 = Label(root, text = "         ")
my_label3 = Label(root, text = "My name is Anna Quinn")

# Shoving it onto the screen
my_label1.grid(row = 0, column = 0 )
my_label2.grid(row = 1, column = 0)
my_label3.grid(row = 2, column = 0)

root.mainloop()






