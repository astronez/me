import pyttsx3
from tkinter import *

window = Tk()
window.title("Anonymous")
window.geometry("500x100")

m = Label(window, text = "Choose voice that you like").grid(row = 0, column = 0, columnspan = 6)

def ongea(val,user):
    speak = pyttsx3.init()
    voices = speak.getProperty('voices')
    speak.setProperty('voice',voices[val].id)
    speak.setProperty('rate', 150)
    speak.say(user)
    speak.runAndWait()

def male():
    male = Tk()

    window.title("Male talking")
    window.geometry("500x250")
    user = Entry(male,width = 36)

    def a(user):
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice',voices[0].id)
        speak.say(user.get())
        speak.runAndWait()

    user.grid(row=0,column = 0)
    btn = Button(male, text = "Male Speak", command = lambda x= user : a(x)).grid(row = 1, column = 0)
    male.mainloop()

def female():
    female = Tk()

    window.title("Female talking")
    window.geometry("500x250")
    user = Entry(female,width = 36)

    def a(user):
        user = user.get()
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice',voices[1].id)
        speak.say(user)
        speak.runAndWait()

    user.grid(row=0,column = 0)
    btn = Button(female, text = "Female Speak", command = lambda x = user : a(x)).grid(row = 1, column = 0)
    female.mainloop()

femal = Button(window, text = "Female", width = 36, command = female).grid(row = 1, column = 3)
mal = Button(window, text = "Male", width = 36, command = male).grid(row = 1, column = 5)

window.mainloop()