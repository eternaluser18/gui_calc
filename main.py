import tkinter as tk
x = None
y = None
xi = None
yi = None
sign = None
ans = 0
def answer(x, y, sign):
    global ans
    if y is not None:
        ans = 1
        if sign == "+":
            answer_label.config(text = x + y)
        if sign == "-":
            answer_label.config(text = x - y)
        if sign == "*":
            answer_label.config(text = x * y)
        if sign == "/":
            answer_label.config(text = x / y)
    else:
        print("Y is not declared")
def choose_a_sign(s):
    if ans == 0:
        global sign
        global x
        if x is  not None:
            sign = s
            sign_label.config(text = sign)
        else:
            print("First number isn't declared")
def build_a_number(n):
    global x
    global y
    global xi
    global yi
    if sign is None:
        if x == None:
            x = n
            first_number_label.config(text = x)
        else:
            x *= 10
            x = x + n
            first_number_label.config(text=x)
    else:
        if ans == 0:
            if y == None:
                y = n
                second_number_label.config(text=y)
            else:
                y *= 10
                y = y + n
                second_number_label.config(text=y)

def clear():
    global x
    global y
    global xi
    global yi
    global sign
    global ans

    ans = 0
    x = None
    y = None
    sign = None
    first_number_label.config(text='')
    sign_label.config(text='')
    second_number_label.config(text='')
    answer_label.config(text='')

root = tk.Tk()

root.geometry("500x500")
root.title("My first GUI")

buttonframe0 = tk.Frame(root)
buttonframe0.columnconfigure(0, weight = 1)
buttonframe0.columnconfigure(1, weight = 1)

answer_button = tk.Button(buttonframe0, text = "Answer?",font = "Tahoma 14", command = lambda : answer(x, y, sign))
answer_button.grid(row = 0, column = 0, sticky = tk.W + tk.E)

clear_button = tk.Button(buttonframe0, text = "Clear?",font = "Tahoma 14", command = clear)
clear_button.grid(row = 0, column = 2, sticky = tk.W + tk.E)

buttonframe0.pack(fill='y')

##############################################################################################
# Pack with a numbers is bellow
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight = 1)
buttonframe.columnconfigure(1, weight = 1)
buttonframe.columnconfigure(2, weight = 1)



btn1 = tk.Button(buttonframe, text = '1', font = ('Comic Sans', 18), command = lambda : build_a_number(1))
btn1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

btn2 = tk.Button(buttonframe, text = '2', font = ('Comic Sans', 18), command = lambda : build_a_number(2))
btn2.grid(row = 0, column = 1, sticky = tk.W + tk.E)

btn3 = tk.Button(buttonframe, text = '3', font = ('Comic Sans', 18), command = lambda : build_a_number(3))
btn3.grid(row = 0, column = 2, sticky = tk.W + tk.E)

btn4 = tk.Button(buttonframe, text = '4', font = ('Comic Sans', 18), command = lambda : build_a_number(4))
btn4.grid(row = 1, column = 0, sticky = tk.W + tk.E)

btn5 = tk.Button(buttonframe, text = '5', font = ('Comic Sans', 18), command = lambda : build_a_number(5))
btn5.grid(row = 1, column = 1, sticky = tk.W + tk.E)

btn6 = tk.Button(buttonframe, text = '6', font = ('Comic Sans', 18), command = lambda : build_a_number(6))
btn6.grid(row = 1, column = 2, sticky = tk.W + tk.E)

btn7 = tk.Button(buttonframe, text = '7', font = ('Comic Sans', 18), command = lambda : build_a_number(7))
btn7.grid(row = 2, column = 0, sticky = tk.W + tk.E)

btn8 = tk.Button(buttonframe, text = '8', font = ('Comic Sans', 18), command = lambda : build_a_number(8))
btn8.grid(row = 2, column = 1, sticky = tk.W + tk.E)

btn8 = tk.Button(buttonframe, text = '9', font = ('Comic Sans', 18), command = lambda : build_a_number(9))
btn8.grid(row = 2, column = 2, sticky = tk.W + tk.E)

btn8 = tk.Button(buttonframe, text = '0', font = ('Comic Sans', 18), command = lambda : build_a_number(0))
btn8.grid(row = 3, column = 1, sticky = tk.W + tk.E)

buttonframe.pack(fill='x')

########################################################################################

buttonframe1 = tk.Frame(root)
buttonframe1.columnconfigure(0, weight = 1)
buttonframe1.columnconfigure(1, weight = 1)
buttonframe1.columnconfigure(2, weight = 1)
buttonframe1.columnconfigure(3, weight = 1)

btn01 = tk.Button(buttonframe1, text = '+', font = ('Comic Sans', 18), command = lambda : choose_a_sign("+"))
btn01.grid(row = 0, column = 0, sticky = tk.W + tk.E)

btn02 = tk.Button(buttonframe1, text = '-', font = ('Comic Sans', 18), command = lambda : choose_a_sign("-"))
btn02.grid(row = 0, column = 1, sticky = tk.W + tk.E)

btn03 = tk.Button(buttonframe1, text = '*', font = ('Comic Sans', 18), command = lambda : choose_a_sign("*"))
btn03.grid(row = 0, column = 2, sticky = tk.W + tk.E)

btn04 = tk.Button(buttonframe1, text = '/', font = ('Comic Sans', 18), command = lambda : choose_a_sign("/"))
btn04.grid(row = 0, column = 3, sticky = tk.W + tk.E)

buttonframe1.pack(fill='both')

first_number_label = tk.Label(root, font = "System 20")
first_number_label.pack()

sign_label = tk.Label(root, font = "System 20")
sign_label.pack()

second_number_label = tk.Label(root, font = "System 20")
second_number_label.pack()

answer_sign_label = tk.Label(root, font = "System 20", text = "=")
answer_sign_label.pack()

answer_label = tk.Label(root, font = "System 20")
answer_label.pack()

root.mainloop()
