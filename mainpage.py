from tkinter import *

def well():
    login.destroy()
    from chapchap import calc

login = Tk()

def check():
    user = usern.get()
    password = entry.get()
    if user == "col" and password == "123":
        well()
    else:
        Label(login,text="Wrong password").pack()

userLab = Label(login, text="Username").pack()
usern = Entry(login)
usern.pack()
pasLab = Label(login, text="Password").pack()
entry = Entry(login)
entry.pack()
btn = Button(login, text = "Submit", command = check).pack()
login.mainloop()