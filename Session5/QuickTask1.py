from tkinter import *

m = Tk()

m.title("Quick Task1")
#m.geometry('500x500+100+100')

# Buttons

bt1 = Button(text="Button 1")
bt2 = Button(text="Button 2")
bt3 = Button(text="Button 3")
bt4 = Button(text="Button 4")

# Placing
bt1.grid(row=0, column = 1)
bt2.grid(row=1, column = 0)
bt3.grid(row=1, column = 2)
bt4.grid(row=2, column = 1)

m.mainloop()
