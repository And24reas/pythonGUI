from tkinter import *
import tkinter.messagebox

root= Tk()
string = 'Monkeys can live up to 300 years'
messagebox = tkinter.messagebox.showinfo('Window Title', string)

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces')

if answer == 'yes':
    string = "8===D - - - "
    print("8===D - - - ")
    tkinter.messagebox.showinfo('Window Title', string)

root.mainloop()