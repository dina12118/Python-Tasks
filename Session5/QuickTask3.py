from tkinter import *
m = Tk()

m.title("Quick Task3")

#Functions
def calculate():
    global value
    v = value.get()
    M = int(ent1.get())
    N = int(ent2.get())
    
    if v == 1:
        lbl_result.configure(text='The sub is '+ str(M-N))
    elif v ==2:
        lbl_result.configure(text='The sum is '+ str(M+N))

#Labels
lbl1 = Label(m,text='Enter the value of M:')
lbl2 = Label(m,text='Enter the value of N:')
lbl_result = Label(m)

#Entries
ent1 = Entry(m)
ent2 = Entry(m)

#Buttons
bt = Button(m, text='Validate', command=calculate)

#Radio Buttons
value = IntVar()
rb1 = Radiobutton(m, text = 'sub', variable=value, value=1)
rb2 = Radiobutton(m, text = 'sum', variable=value, value=2)

#Placing
lbl1.grid(row=0,column=0)
lbl2.grid(row=1,column=0)
lbl_result.grid(row=2,column=1)

ent1.grid(row=0,column=1)
ent2.grid(row=1,column=1)

rb1.grid(row=2,column=0)
rb2.grid(row=3,column=0)

bt.grid(row=3,column=1)

m.mainloop()