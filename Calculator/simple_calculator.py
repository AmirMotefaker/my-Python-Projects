# Code by @AmirMotefaker

# Simple Calculator

# Install Tkinter: pip install tk
from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator by AmirMotefaker")
        self.root.geometry("400x450+400+100")
        self.root.maxsize(400, 450)
        self.root.config(bg="white")

        self.old_value = False

        self.Entry_Value = StringVar()
        self.Entry_Value.set("")

        self.Entry_Field = Entry(self.root, textvariable = self.Entry_Value, justify ='right', font=("Calibri",18))
        self.Entry_Field.grid(columnspan= 4, ipadx= 46, ipady= 40)

        Button_blank = Button(self.root, text= '  ', height= 3, width = 7, fg = 'white', bg = 'gray35')
        Button_blank.grid(row= 1, columnspan= 3, ipadx= 100, ipady= 0)

        # Clear Button
        Button_clear = Button(self.root, text= ' CLR ', command = lambda: self.on_press("CLR"), height= 3, width = 7, fg = 'white', bg = 'gray35')
        # Grid Row 1 and Column 3
        Button_clear.grid(row= 1, column= 3)

        Button_7 = Button(self.root, text= ' 7 ', command = lambda: self.on_press(7), height= 3, width = 7, fg = 'white', bg = 'gray50')
        # Row 2 and Column 0
        Button_7.grid(row= 2, column= 0)

        Button_8 = Button(self.root, text= ' 8 ', command = lambda: self.on_press(8), height= 3, width = 7, fg = 'white', bg = 'gray50')
        Button_8.grid(row= 2, column= 1)

        Button_9 = Button(self.root, text= ' 9️ ', command = lambda: self.on_press(9), height= 3, width = 7, fg = 'white', bg = 'gray50')
        Button_9.grid(row= 2, column= 2)

        # Divide Button
        Button_div = Button(self.root, text= ' ➗ ', command = lambda: self.on_press("/"), height= 3, width = 7, fg = 'white', bg = 'gray35')
        Button_div.grid(row= 2, column= 3)

        Button_4 = Button(self.root, text= ' 4 ', command = lambda: self.on_press(4), height= 3, width = 7, fg = 'white', bg = 'gray50')
        Button_4.grid(row= 3, column= 0)

        Button_5 = Button(self.root, text= ' 5 ', command = lambda: self.on_press(5), height= 3, width = 7, fg = 'white', bg = 'gray50')
        Button_5.grid(row= 3, column= 1)

        Button_6 = Button(self.root, text= ' 6 ', command = lambda: self.on_press(6), height= 3, width = 7, fg = 'white', bg = 'gray50')
        Button_6.grid(row= 3, column= 2)

        # Multiply Button
        Button_mul = Button(self.root, text= ' ✖️ ', command = lambda: self.on_press("*"), height= 3, width = 7, fg = 'white', bg = 'gray35')
        Button_mul.grid(row= 3, column= 3)

        Button_1 = Button(self.root, text= ' 1 ', command = lambda: self.on_press(1), height= 3, width = 7, fg = 'white', bg = 'gray50')
        Button_1.grid(row= 4, column= 0)

        Button_2 = Button(self.root, text= ' 2 ', command = lambda: self.on_press(2), height= 3, width = 7, fg = 'white', bg = 'gray50')
        Button_2.grid(row= 4, column= 1)

        Button_3 = Button(self.root, text= ' 3 ', command = lambda: self.on_press(3), height= 3, width = 7, fg = 'white', bg = 'gray50')
        Button_3.grid(row= 4, column= 2)

        Button_min = Button(self.root, text= ' ➖ ', command = lambda: self.on_press("-"), height= 3, width = 7, fg = 'white', bg = 'gray35')
        Button_min.grid(row= 4, column= 3)

        # Point Button
        Button_point = Button(self.root, text= ' . ', command = lambda: self.on_press("."), height= 3, width = 7, fg = 'white', bg = 'gray50')
        Button_point.grid(row= 5, column= 0)

        Button_zero = Button(self.root, text= ' 0 ', command = lambda: self.on_press(0), height= 3, width = 7, fg = 'white', bg = 'gray50')
        Button_zero.grid(row= 5, column= 1)

        # Equals Button
        Button_equal = Button(self.root, text= ' = ', command = 
            lambda: self.on_press("="), height= 3, width = 7, fg = 'white', bg = 'orange')
        Button_equal.grid(row= 5, column= 2)

        # Plus Button
        Button_plus = Button(self.root, text= ' ➕ ', command = lambda: self.on_press("+"), height= 3, width = 7, fg = 'white', bg = 'gray35')
        Button_plus.grid(row= 5, column= 3)

    def on_press(self, txt):
        if txt == "=":
            if self.Entry_Value.get().isdigit():
                result = int(self.Entry_Value.get())
            else:
                try:
                    # eval function is used for evaluate expressions in Python
                    # This is the main part of this program. 
                    # This is used for the calculation.
                    result = eval(self.Entry_Field.get())
                except:
                    result = "Error"

            self.Entry_Value.set(result)
            self.Entry_Field.update()
            self.old_value = True
        elif txt == "CLR":
            self.Entry_Value.set("")
            self.Entry_Field.update()
        else:
            if self.old_value is False:
                self.Entry_Value.set(self.Entry_Field.get() + str(txt))
                self.Entry_Field.update()
            else:
                self.Entry_Value.set("")
                self.Entry_Field.update()
                self.Entry_Value.set(self.Entry_Field.get() + str(txt))
                self.Entry_Field.update()
                self.old_value = False

if __name__ == "__main__":
    root = Tk()
    obj = Calculator(root)
    root.mainloop()
