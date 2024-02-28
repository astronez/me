from tkinter import *
from tkinter import messagebox

start = Tk()
start.geometry("220x60")
start.title("Quiz Intro")
start.resizable(False, False)

def quiz():
    start.destroy()
    quiz = Tk()
    quiz.title("Quiz App")
    quiz.geometry("300x300")

    def check():
        val = int(an1.get())
        if val == (5*6):
            messagebox.showinfo("Answer","Correct")
            quiz.destroy()
        else:
            messagebox.showerror("Answer","Wrong")


    qn1 = Label(quiz, text = "Qn.1 What is 5 x 6 ?").grid(row=0,column=0,columnspan=5)
    # a = Button(quiz, text = "45", bg = "red", command = lambda : messagebox.showerror("Answer", "Wrong")).grid(row=1,column=1)
    # a = Button(quiz, text = "25", bg = "red", command = lambda : messagebox.showerror("Answer", "Wrong")).grid(row=1,column=2)
    # a = Button(quiz, text = "30", bg = "red", command = lambda : messagebox.showinfo("Answer", "Correct")).grid(row=1,column=3)
    # a = Button(quiz, text = "12", bg = "red", command = lambda : messagebox.showwarning("Answer", "Wrong")).grid(row=1,column=4)

    an1 = Entry(quiz)
    an1.grid(row=1,column=2)
    btn1 = Button(quiz, bg = "purple", text = "Submit", command = lambda : check()).grid(row=1,column=3)

    quiz.mainloop()

lb = Label(start, text = "Would you like to try the Quiz Game").grid(row=1,column=1,columnspan=12)
btn1 = Button(start, text = "Yes", command = quiz).grid(row=4,column=4)
btn2 = Button(start, text = "No", command = start.destroy).grid(row=4,column=6)

start.mainloop()