from tkinter import *
import subprocess as sb

def decu():
    inp = input_1.get()
    with open('www.txt', 'w') as weer:
        weer.write(inp)
    red()

def red():
    sb.call("nano www.txt",shell=True)

window = Tk()
window.title("Main Form for registration")
window.geometry("600x300")
# window.resizable(False,False)
background = Frame(window, bg="yellow", width=600, height=300).place(x=0, y=0)

heading = Label(window, text="REGISTRATION FORM IN GUI", font = ("impact", 15), bg="yellow",foreground="green").grid(row=0,column=0, columnspan=2)
div1 = Label(window, text="Enter Your First Name: ", bg="yellow").grid(row =1, column=0)
input_1 = Entry(window,width=30)
input_1.grid(row =1, column=1 )


div2 = Label(window, text="Enter Your second Name: ", bg="yellow").grid(row =4, column=0)
input_2 = Entry(window,width=30)
input_2.grid(row =4, column=1 )

div3 = Label(window, text="Enter Your Address: ", bg="yellow").grid(row =6, column=0)
input_3 = Entry(window,width=30)
input_3.grid(row =6, column=1 )

Submitbtn = Button(window, text="Submit", command= decu,).grid(row=10,column=1)


window.mainloop()