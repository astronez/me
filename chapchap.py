from tkinter import *
def calc():

    window = Tk()

    def dele():
        inp.delete(0, END)

    def writ(number):
        saivi = inp.get()
        inp.delete(0, END)
        inp.insert(0, str(saivi) + str(number))

    def outp():
        output = eval(inp.get())
        inp.delete(0, END)
        inp.insert(0, str(output))

    a = "orange"
    b = "blue"
    buttons = [
        ('7',1,0,a), ('8', 1, 1,a), ('9', 1, 2,a), ('/', 1, 3,b),
        ('4',2,0,a), ('5', 2, 1,a), ('6', 2, 2,a), ('+', 2, 3,b),
        ('1',3,0,a), ('2', 3, 1,a), ('3', 3, 2,a), ('-', 3, 3,b),
        ('0',4,0,a), ('C', 4, 1,"yellow"), ('=', 4, 2,b), ('*', 4, 3,b),
    ]

    fr = Frame(window, width= 40, height= 23).grid(row=0,column=0,columnspan=4)
    inp = Entry(fr)
    inp.grid(row=0,column=0,columnspan=4)
    for text,row,col,color in buttons:
        if text == "C":
            Button(window, text = text, bg = color, command= dele).grid(row=row, column=col)
        elif text == "=":
            Button(window, text = text, bg = color,  command= outp).grid(row=row, column=col)
        else:
            Button(window, text = text, bg = color, command = lambda x = text : writ(x)).grid(row=row, column=col)
    window.mainloop()
calc()