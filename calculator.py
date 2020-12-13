from tkinter import *

expression = "" 

# Function to update expressiom 
# in the text entry box 
def press(num): 
	global expression 
	expression = expression + str(num) 
	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	try: 

		global expression 

		# eval function evaluate the expression
		# i.e it will in this case recognize that
		# it's an arithmetic operation. So it will 
		# perform it and return the result 
		# and str function converts the result
		# into string 
		total = str(eval(expression)) 
		equation.set(total) 
		expression = "" 

	except: 

		equation.set(" error ") 
		expression = "" 


# Function to clear the contents 
# of text entry box 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


if __name__ == "__main__": 

	gui = Tk() 
	gui.configure(background="light green") 
	gui.title("Simple Calculator") 

	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar() 
	frame = Frame(gui)
	equation.set('enter your expression')
	expression_field = Entry(frame, textvariable=equation, bd=20, selectbackground="green" ) 
	expression_field.pack(fill=X)
	frame.pack(fill=X)

	frame_1 = Frame(gui)
	frame_2 = Frame(gui)
	frame_3 = Frame(gui)
	frame_4 = Frame(gui)

	

	button1 = Button(frame_1, text=' 1 ', fg='white', bg="blue", 
					command=lambda: press(1), height=5, width=10) 
	button1.pack(side=LEFT)

	button2 = Button(frame_1, text=' 2 ', fg='white', bg="blue", 
					command=lambda: press(2),  height=5, width=10) 
	button2.pack(side=LEFT)

	button3 = Button(frame_1, text=' 3 ', fg='white', bg="blue", 
					command=lambda: press(3),  height=5, width=10) 
	button3.pack(side=LEFT)

	button4 = Button(frame_1, text=' 4 ', fg='white', bg="blue", 
					command=lambda: press(4), height=5, width=10) 
	button4.pack(side=LEFT)
	frame_1.pack(fill=X) 

	button5 = Button(frame_2, text=' 5 ', fg='white', bg='red', 
					command=lambda: press(5), height=5, width=10) 
	button5.pack(side=LEFT) 

	button6 = Button(frame_2, text=' 6 ', fg='white', bg='red', 
					command=lambda: press(6), height=5, width=10) 
	button6.pack(side=LEFT) 

	button7 = Button(frame_2, text=' 7 ', fg='white', bg='red', 
					command=lambda: press(7), height=5, width=10) 
	button7.pack(side=LEFT)

	button8 = Button(frame_2, text=' 8 ', fg='white', bg='red', 
					command=lambda: press(8),  height=5, width=10) 
	button8.pack(side=LEFT)
	frame_2.pack(fill=X)
	
	button9 = Button(frame_3, text=' 9 ', fg='black', bg='yellow', 
					command=lambda: press(9), height=5, width=10) 
	button9.pack(side=LEFT) 

	button0 = Button(frame_3, text=' 0 ', fg='black', bg='yellow', 
					command=lambda: press(0),  height=5, width=10) 
	button0.pack(side=LEFT) 

	plus = Button(frame_3, text=' + ', fg='black', bg='yellow', 
				command=lambda: press("+"),  height=5, width=10) 
	plus.pack(side=LEFT) 

	minus = Button(frame_3, text=' - ', fg='black', bg='yellow', 
				command=lambda: press("-"),  height=5, width=10) 
	minus.pack(side=LEFT)
	frame_3.pack(fill=X)

	multiply = Button(frame_4, text=' * ', fg='white', bg='green', 
					command=lambda: press("*"),  height=5, width=10) 
	multiply.pack(side=LEFT) 

	divide = Button(frame_4, text=' / ', fg='white', bg='green', 
					command=lambda: press("/"), height=5, width=10) 
	divide.pack(side=LEFT)

	equal = Button(frame_4, text=' = ', fg='white', bg='green', 
				command=equalpress,  height=5, width=10) 
	equal.pack(side=LEFT) 

	clear = Button(frame_4, text='Clear', fg='white', bg='green', 
				command=clear,  height=5, width=10) 
	clear.pack(side=LEFT)
	"""
	Decimal= Button(frame_4, text='.', fg='black', bg='red', 
					command=lambda: press('.'),  height=5, width=10) 
	Decimal.pack(side=LEFT)
	"""
	frame_4.pack(fill=X)
	# start the GUI 
	gui.mainloop() 
