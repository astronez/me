from tkinter import *

window = Tk()
window.geometry("500x500")

fram = Frame(window, width= 200, height= 40).pack(side=TOP)
ent = Entry(fram).pack()
btn = Button(window, image=PhotoImage(file="./a.png"),width=200).pack()

window.mainloop()
