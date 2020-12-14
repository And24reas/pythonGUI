from tkinter import *

def doNothing():
    print("ok ok i wont")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

#######################################################
#                      Toolbar                        #
#######################################################
toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="Insert Image", command=doNothing)
printButt = Button(toolbar, text="Print", command=doNothing)
fb = PhotoImage(file="facebook.png")
labelfb = Label(printButt, image=fb)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=Y)

#######################################################
#                     Statusbar                       #
#######################################################

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
root.mainloop()