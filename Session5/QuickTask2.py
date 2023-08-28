from tkinter import *

m = Tk()

m.title("Quick Task2")
#m.geometry('400x400')

#functions
def reverse():
    word = ent.get()
    lbl2.configure(text=word[::-1])


#Lables
lbl1 = Label(m, text="Enter a word:")
lbl2 = Label(m)

#Entry
ent = Entry(m)

#Buttons
bt = Button(m, text='Validate',command=reverse)

#placing

lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=1)
ent.grid(row=0,column=1)
bt.grid(row=2,column=1)


m.mainloop()