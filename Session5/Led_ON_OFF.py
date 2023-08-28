from tkinter import *

m = Tk()
m.title("Led Task")
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200

#Functions
def Led_ON():
    lbl1.configure(text='Led is ON')
    canvas.itemconfigure(oval, fill='red')

def Led_OFF():
    lbl1.configure(text='Led is OFF')
    canvas.itemconfigure(oval, fill='white')

#Labels
lbl1 = Label(m)

#Buttons
bt1 = Button(m, text='Led ON',width=10, command=Led_ON)
bt2 = Button(m, text='Led OFF',width=10, command=Led_OFF)

#Canvas
canvas = Canvas(m, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
oval = canvas.create_oval((CANVAS_WIDTH/2)-30, (CANVAS_HEIGHT/2)-30, (CANVAS_WIDTH/2)+30,(CANVAS_HEIGHT/2)+30, fill='white', outline='black')

#Placing
canvas.grid(row=0, column=0)
lbl1.grid(row=1,column=0)
bt1.grid(row=2,column=0)
bt2.grid(row=3,column=0)

m.mainloop()