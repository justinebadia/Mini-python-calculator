from _ast import Lambda
from tkinter import *

root = Tk()
root.title("My Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=5, pady=10)

#
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

# calculation functions
def button_add():
    a = e.get()
    global g_a
    global g_type
    g_type = "addition"
    g_a = int(a)
    e.delete(0, END)

def button_equal():
    b = e.get()
    e.delete(0, END)
    if g_type == "addition":
        e.insert(0, g_a + int(b))
    if g_type == "substraction":
        e.insert(0, g_a - int(b))
    if g_type == "multiplication":
        e.insert(0, g_a * int(b))
    if g_type == "division":
        e.insert(0, g_a / int(b))

def button_sub():
    a = e.get()
    global g_a
    global g_type
    g_type = "substraction"
    g_a = int(a)
    e.delete(0, END)


def button_mul():
    a = e.get()
    global g_a
    global g_type
    g_type = "multiplication"
    g_a = int(a)
    e.delete(0, END)


def button_div():
    a = e.get()
    global g_a
    global g_type
    g_type = "division"
    g_a = int(a)
    e.delete(0, END)

# buttons variable initialization
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(text="+", padx=40, pady=20, command=button_add)
button_sub = Button(text="-", padx=40, pady=20, command=button_sub)
button_mul = Button(text="x", padx=40, pady=20, command=button_mul)
button_div = Button(text="/", padx=40, pady=20, command=button_div)

button_equal = Button(text="=", padx=40, pady=20, command=button_equal)
button_clear = Button(text="C", padx=40, pady=20, command=button_clear)

# buttons position in the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)
button_add.grid(row=1, column=4)
button_sub.grid(row=2, column=4)
button_mul.grid(row=3, column=4)
button_div.grid(row=4, column=4)

# event loop
root.mainloop()

