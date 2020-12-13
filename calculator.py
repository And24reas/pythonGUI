from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=5)

#e.insert(0,"0")


def createGui():
    myButton0 = Button(root, text="0",padx=40,pady=20, command=button_add).grid(row=5,column=0)
    myButton1 = Button(root, text="1",padx=40,pady=20, command=button_add).grid(row=4,column=1)
    myButton2 = Button(root, text="2",padx=40,pady=20, command=button_add).grid(row=4,column=0)
    myButton3 = Button(root, text="3",padx=40,pady=20, command=button_add).grid(row=4,column=2)
    myButton4 = Button(root, text="4",padx=40,pady=20, command=button_add).grid(row=3,column=0)
    myButton5 = Button(root, text="5",padx=40,pady=20, command=button_add).grid(row=3,column=1)
    myButton6 = Button(root, text="6",padx=40,pady=20, command=button_add).grid(row=3,column=2)
    myButton7 = Button(root, text="7",padx=40,pady=20, command=button_add).grid(row=2,column=0)
    myButton8 = Button(root, text="8",padx=40,pady=20, command=button_add).grid(row=2,column=1)
    myButton9 = Button(root, text="9",padx=40,pady=20, command=button_add).grid(row=2,column=2)
    myButtonPlus = Button(root, text="+",padx=40,pady=20, command=button_add).grid(row=6,column=0)
    myButtonMinus = Button(root, text="-",padx=40,pady=20, command=button_add).grid(row=5,column=2)
    myButtonEquals = Button(root, text="=",padx=40,pady=20, command=button_add).grid(row=5,column=1,columnspan = 2)
    myButtonClear = Button(root, text="C",padx=40,pady=20, command=button_add).grid(row=6,column=1,columnspan = 2)


def button_add():
    pass
createGui()
root.mainloop()
#