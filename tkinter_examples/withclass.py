from tkinter import *


class MyButton:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=RIGHT)

    def printMessage(self):
        print("Print Message")

root = Tk()
b = MyButton(root)
root.mainloop()