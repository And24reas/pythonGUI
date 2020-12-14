from tkinter import *

root = Tk()

fb = PhotoImage(file="facebook.png")
labelfb = Label(root, image=fb)
labelfb.pack()
yt = PhotoImage(file="youtube.png")
labelyt = Label(root, image=yt)
labelyt.pack()
root.mainloop()