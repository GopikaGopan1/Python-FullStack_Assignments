# ==================================================================================================
#  Tkinter Basic Window Example
# --------------------------------------------------------------------------------------------------
# This program demonstrates the creation of a basic Tkinter window
# with labels arranged using the grid layout manager.
# ==================================================================================================

from tkinter import *
window = Tk()
window.title('Desktop App')
window.geometry('400x400')
window.maxsize(800, 800)
window.minsize(200, 200)

l1 = Label(text='hello')
l1.grid(row=0, column=0)

l2 = Label(text='python')
l2.grid(row=2, column=1)

l3 = Label(text='tkinter')
l3.grid(row=3, column=0)

window.mainloop()


# ==================================================================================================
# Tkinter Simple Arithmetic Calculator
# --------------------------------------------------------------------------------------------------
# This program takes two numbers as input and performs addition,
# subtraction, multiplication, and division using buttons.
# It also includes clear and backspace functionalities.
# ==================================================================================================

from tkinter import *
window = Tk()
window.geometry('500x500')

l1 = Label(text='1st Number : ', fg='blue')
l1.grid(row=0, column=1)

l2 = Label(text='2nd Number : ', fg='blue')
l2.grid(row=1, column=1)

l3 = Label()
l3.grid(row=3, column=2)

t1 = Entry()
t1.grid(row=0, column=2)

t2 = Entry()
t2.grid(row=1, column=2)


def onClick1():
    s1 = t1.get()
    s2 = t2.get()
    l3.config(text=int(s1) + int(s2))


def onClick2():
    s1 = t1.get()
    s2 = t2.get()
    l3.config(text=int(s1) - int(s2))


def onClick3():
    s1 = t1.get()
    s2 = t2.get()
    l3.config(text=int(s1) * int(s2))


def onClick4():
    s1 = t1.get()
    s2 = t2.get()
    l3.config(text=int(s1) / int(s2))


def clear():
    t1.delete(0, END)
    t2.delete(0, END)


def backspace1():
    t1.delete(len(t1.get()) - 1, END)


def backspace2():
    t2.delete(len(t2.get()) - 1, END)


b1 = Button(text='Add', command=onClick1)
b1.grid(row=2, column=0)

b2 = Button(text='Sub', command=onClick2)
b2.grid(row=2, column=1)

b3 = Button(text='Mult', command=onClick3)
b3.grid(row=2, column=2)

b4 = Button(text='Div', command=onClick4)
b4.grid(row=2, column=3)

b5 = Button(text='CLEAR', command=clear)
b5.grid(row=2, column=4)

b6 = Button(text='Backspace', command=backspace1)
b6.grid(row=0, column=3)

b7 = Button(text='Backspace', command=backspace2)
b7.grid(row=1, column=3)

window.mainloop()


# ==================================================================================================
# Tkinter Full Functional Calculator
# --------------------------------------------------------------------------------------------------
# This program implements a fully working calculator using Tkinter.
# It supports:
#   - Numeric input
#   - Basic operations (+, -, *, /)
#   - Backspace, Clear, and Equals functions
#   - Proper input validation (avoids multiple operators)
# ==================================================================================================

from tkinter import *
window = Tk()
window.geometry('330x225')
window.minsize(320, 200)
window.maxsize(450, 450)

t1 = Entry(width=55)
t1.insert(0, '0')
t1.grid(row=0, column=0, columnspan=5)

op0 = ['+0', '-0', '/0', '*0']
op = ['-', '/', '*', '+']


# --- Numeric Button Functions ---
def Num0():
    c = 0
    b = t1.get()
    if b != '0' and b[-2:] not in op0:
        t1.insert(END, c)


def Num1():
    c = 1
    b = t1.get()
    if b == '0' or (b[-1] == '0' and b[-2] in op):
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


def Num2():
    c = 2
    b = t1.get()
    if b == '0' or (b[-1] == '0' and b[-2] in op):
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


def Num3():
    c = 3
    b = t1.get()
    if b == '0' or (b[-1] == '0' and b[-2] in op):
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


def Num4():
    c = 4
    b = t1.get()
    if b == '0' or (b[-1] == '0' and b[-2] in op):
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


def Num5():
    c = 5
    b = t1.get()
    if b == '0' or (b[-1] == '0' and b[-2] in op):
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


def Num6():
    c = 6
    b = t1.get()
    if b == '0' or (b[-1] == '0' and b[-2] in op):
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


def Num7():
    c = 7
    b = t1.get()
    if b == '0' or (b[-1] == '0' and b[-2] in op):
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


def Num8():
    c = 8
    b = t1.get()
    if b == '0' or (b[-1] == '0' and b[-2] in op):
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


def Num9():
    c = 9
    b = t1.get()
    if b == '0' or (b[-1] == '0' and b[-2] in op):
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


# --- Operation Button Functions ---
def onClick1():
    c = '+'
    b = t1.get()
    if b[-1] in op:
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


def onClick2():
    c = '-'
    b = t1.get()
    if b[-1] in op:
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


def onClick3():
    c = '*'
    b = t1.get()
    if b[-1] in op:
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


def onClick4():
    c = '/'
    b = t1.get()
    if b[-1] in op:
        t1.delete(len(b) - 1, END)
    t1.insert(END, c)


def onClickAns():
    b = t1.get()
    ans = eval(b)
    t1.delete(0, END)
    t1.insert(0, ans)


def clear():
    t1.delete(0, END)
    t1.insert(END, 0)


def backspace1():
    t1.delete(len(t1.get()) - 1, END)
    if len(t1.get()) == 0:
        t1.insert(END, 0)


# --- Button Layout ---
n0 = Button(text='0', command=Num0, width=10, height=2)
n0.grid(row=5, column=1)
n1 = Button(text='1', command=Num1, width=10, height=2)
n1.grid(row=4, column=0)
n2 = Button(text='2', command=Num2, width=10, height=2)
n2.grid(row=4, column=1)
n3 = Button(text='3', command=Num3, width=10, height=2)
n3.grid(row=4, column=2)
n4 = Button(text='4', command=Num4, width=10, height=2)
n4.grid(row=3, column=0)
n5 = Button(text='5', command=Num5, width=10, height=2)
n5.grid(row=3, column=1)
n6 = Button(text='6', command=Num6, width=10, height=2)
n6.grid(row=3, column=2)
n7 = Button(text='7', command=Num7, width=10, height=2)
n7.grid(row=2, column=0)
n8 = Button(text='8', command=Num8, width=10, height=2)
n8.grid(row=2, column=1)
n9 = Button(text='9', command=Num9, width=10, height=2)
n9.grid(row=2, column=2)

b1 = Button(text='+', command=onClick1, width=10, height=2)
b1.grid(row=4, column=3)
b2 = Button(text='-', command=onClick2, width=10, height=2)
b2.grid(row=3, column=3)
b3 = Button(text='*', command=onClick3, width=10, height=2)
b3.grid(row=2, column=3)
b4 = Button(text='/', command=onClick4, width=10, height=2)
b4.grid(row=1, column=3)
b41 = Button(text='=', width=10, height=2, command=onClickAns)
b41.grid(row=5, column=3)
b5 = Button(text='C', command=clear, width=10, height=2)
b5.grid(row=1, column=1)
b6 = Button(text='<X', command=backspace1, width=10, height=2)
b6.grid(row=1, column=2)
b7 = Button(text='CE', width=10, height=2)
b7.grid(row=1, column=0)
b8 = Button(text='+/-', width=10, height=2)
b8.grid(row=5, column=0)
b9 = Button(text='.', width=10, height=2)
b9.grid(row=5, column=2)

window.mainloop()


# ==================================================================================================
# Tkinter Scrolled Text Example
# --------------------------------------------------------------------------------------------------
# This program demonstrates how to use the `ScrolledText` widget
# to create a text area with automatic scrolling.
# ==================================================================================================

from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

window = Tk()
window.geometry('500x500')
window.title('Scrolled Text Example')

scroll_1 = scrolledtext.ScrolledText(width=50, height=15)
scroll_1.grid()


def clicked():
    scroll_1.insert(5.9, '**********')  # Inserts at line 5, index 9


bt1 = Button(text='Click', command=clicked)
bt1.grid()

window.mainloop()





















