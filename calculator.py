import subprocess as sb
from tkinter import *

def speak():
    sb.call("espeak",shell=True)

def read():
    text = ent.get()
    sb.call(f"espeak '{text.get}'", shell= True)

main = Tk()
main.title("Speak Operator")
main.geometry("500x400")

ent = Entry(main, width=36)
ent.grid(row=2,column=4,columnspan=10)
btn = Button(main, text = "Speak", command = speak).grid(row=5,column=6)
btn2 = Button(main, text = "Read", command= read).grid(row=5, column=8)

main.mainloop()
print(mainloop)