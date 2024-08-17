import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    

#Declaration of Geometry of Calculator
root = tk.Tk()
root.title("Calculator")
root.geometry("240x300")
root.resizable(0,0)
# root.config(background="black")

text_result = tk.Text(root, height = 2, width = 16, font = ("Roman", 24))
text_result.grid(columnspan=5)

#Declaration of digit buttons
button_1 = tk.Button(root, text = "1", command = lambda:add_to_calculation(1), width = 5, font = ("Roman", 16))
button_1.grid(row = 2, column = 1)
button_2 = tk.Button(root, text = "2", command = lambda:add_to_calculation(2), width = 5, font = ("Roman", 16))
button_2.grid(row = 2, column = 2)
button_3 = tk.Button(root, text = "3", command = lambda:add_to_calculation(3), width = 5, font = ("Roman", 16))
button_3.grid(row = 2, column = 3)
button_4 = tk.Button(root, text = "4", command = lambda:add_to_calculation(4), width = 5, font = ("Roman", 16))
button_4.grid(row = 3, column = 1)
button_5 = tk.Button(root, text = "5", command = lambda:add_to_calculation(5), width = 5, font = ("Roman", 16))
button_5.grid(row = 3, column = 2)
button_6 = tk.Button(root, text = "6", command = lambda:add_to_calculation(6), width = 5, font = ("Roman", 16))
button_6.grid(row = 3, column = 3)
button_7 = tk.Button(root, text = "7", command = lambda:add_to_calculation(7), width = 5, font = ("Roman", 16))
button_7.grid(row = 4, column = 1)
button_8 = tk.Button(root, text = "8", command = lambda:add_to_calculation(8), width = 5, font = ("Roman", 16))
button_8.grid(row = 4, column = 2)
button_9 = tk.Button(root, text = "9", command = lambda:add_to_calculation(9), width = 5, font = ("Roman", 16))
button_9.grid(row = 4, column = 3)
button_0 = tk.Button(root, text = "0", command = lambda:add_to_calculation(0), width = 5, font = ("Roman", 16))
button_0.grid(row = 5, column = 2)

#Declaration of operations
button_add = tk.Button(root, text = "+", command = lambda:add_to_calculation("+"), width = 5, font = ("Roman", 16))
button_add.grid(row = 3, column = 4)
button_sub = tk.Button(root, text = "-", command = lambda:add_to_calculation("-"), width = 5, font = ("Roman", 16))
button_sub.grid(row = 4, column = 4)
button_prod = tk.Button(root, text = "*", command = lambda:add_to_calculation("*"), width = 5, font = ("Roman", 16))
button_prod.grid(row = 5, column = 4)
button_div = tk.Button(root, text = "/", command = lambda:add_to_calculation("/"), width = 5, font = ("Roman", 16))
button_div.grid(row = 6, column = 4)
button_mod = tk.Button(root, text = "%", command = lambda:add_to_calculation("%"), width = 5, font = ("Roman", 16))
button_mod.grid(row = 6, column = 3)

button_open = tk.Button(root, text = "(", command = lambda:add_to_calculation("("), width = 5, font = ("Roman", 16))
button_open.grid(row = 5, column = 1)
button_close = tk.Button(root, text = ")", command = lambda:add_to_calculation(")"), width = 5, font = ("Roman", 16))
button_close.grid(row = 5, column = 3)


# Declaration of Clear and Close buttons
button_equal = tk.Button(root, text = "=", command = evaluate, width = 5, font = ("Roman", 16))
button_equal.grid(row = 2, column = 4)
button_clear = tk.Button(root, text = "CLR", command = clear_field, width = 11, font = ("Roman", 16))
button_clear.grid(row = 6, column = 1, columnspan=2)

root.mainloop()