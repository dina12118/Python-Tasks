from tkinter import *
from math import factorial

m = Tk()

m.title("Factorial")

#Functions
def calculate():
    num = int(ent1.get())
    result = factorial(num)
    lbl_result.configure(text=f'The factorial of {num} is {num}! = {result}')

#Labels
lbl1 = Label(m,text='Enter the value of intrger N:')
lbl_result = Label(m)

#Entries
ent1 = Entry(m)

#Buttons
bt = Button(m, text='Validate', command=calculate)

#Placing
lbl1.grid(row=0,column=0)
lbl_result.grid(row=1,column=1)

ent1.grid(row=0,column=1)

bt.grid(row=2,column=1)

m.mainloop()