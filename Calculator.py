"""
By Nirajkumar Patel
Project: Simple calculator made from using python tkinter
Date: Aug, 23, 2019
"""
#importing tkinter libary
from tkinter import *

#fuction gets the pressed buttons values and displays it
def get_values(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

#fuction called when the clear button it pressed   
def clear():
    global operator
    operator=""
    text_input.set(operator)

#gets the final answer for the expression    
def equals():
    global operator
    number = str(eval(operator))
    text_input.set(number)
    operator=""
    

#main window
root = Tk()
root.title("Calculator")
root.config(bg="gray18")

#empty strings where numbers and expression will be stored
operator=""
text_input = StringVar()

#Output box and all button placement
display = Entry(root, font=("Times", 12), textvariable=text_input, bg="slate gray", fg="White", justify='right', bd="5")
display.grid(row=0, column=0, columnspan=4)

button7 = Button(root, text="7", bg="gray18", fg="white", activebackground="slate gray", height="3", width="5", command=lambda: get_values(7))
button7.grid(row=1, column=0)

button8 = Button(root, text="8", bg="gray18", fg="white", activebackground="slate gray", height="3", width="5", command=lambda: get_values(8))
button8.grid(row=1, column=1)

button9 = Button(root, text="9", bg="gray18", fg="white", activebackground="slate gray", height="3", width="5", command=lambda: get_values(9))
button9.grid(row=1, column=2)

addition = Button(root, text="+", bg="gray18", fg="deep sky blue", activebackground="slate gray", height="3", width="5", command=lambda: get_values("+"))
addition.grid(row=1, column=3)

#--------------------------------------------------------------------------------------------------------------------------

button4 = Button(root, text="4", bg="gray18", fg="white", activebackground="slate gray", height="3", width="5", command=lambda: get_values(4))
button4.grid(row=2, column=0)

button5 = Button(root, text="5", bg="gray18", fg="white", activebackground="slate gray", height="3", width="5", command=lambda: get_values(5))
button5.grid(row=2, column=1)

button6 = Button(root, text="6", bg="gray18", fg="white", activebackground="slate gray", height="3", width="5", command=lambda: get_values(6))
button6.grid(row=2, column=2)

subtraction = Button(root, text="-", bg="gray18", fg="deep sky blue", activebackground="slate gray", height="3", width="5", command=lambda: get_values("-"))
subtraction.grid(row=2, column=3)

#--------------------------------------------------------------------------------------------------------------------------

button1 = Button(root, text="1", bg="gray18", fg="white", activebackground="slate gray", height="3", width="5", command=lambda: get_values(1))
button1.grid(row=3, column=0)

button2 = Button(root, text="2", bg="gray18", fg="white", activebackground="slate gray", height="3", width="5", command=lambda: get_values(2))
button2.grid(row=3, column=1)

button3 = Button(root, text="3", bg="gray18", fg="white", activebackground="slate gray", height="3", width="5", command=lambda: get_values(3))
button3.grid(row=3, column=2)

division = Button(root, text="/", bg="gray18", fg="deep sky blue", activebackground="slate gray", height="3", width="5", command=lambda: get_values("/"))
division.grid(row=3, column=3)

#--------------------------------------------------------------------------------------------------------------------------

btnClear = Button(root, text="C", bg="gray18", fg="deep sky blue", activebackground="slate gray", height="3", width="5", command=lambda: clear())
btnClear.grid(row=4, column=0)

button0 = Button(root, text="0", bg="gray18", fg="white", activebackground="slate gray", height="3", width="5", command=lambda: get_values(0))
button0.grid(row=4, column=1)

btnEqual = Button(root, text="=", bg="gray18", fg="deep sky blue", activebackground="slate gray", height="3", width="5", command=lambda: equals())
btnEqual.grid(row=4, column=2)

multiplication = Button(root, text="x", bg="gray18", fg="deep sky blue", activebackground="slate gray", height="3", width="5", command=lambda: get_values("*"))
multiplication.grid(row=4, column=3)

root.mainloop()