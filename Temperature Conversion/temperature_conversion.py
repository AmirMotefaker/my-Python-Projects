# Code by @AmirMotefaker

# Temperature Conversion

import tkinter as tk

window = tk.Tk()

lbl_fahrenheit = tk.Label(
    master=window,
    text='Fahrenheit: ',
)
ent_fahrenheit = tk.Entry(
    master=window,
)
btn_calc = tk.Button(
    master=window,
    text='Calc',
)

lbl_fahrenheit.grid(row=0, column=0)
ent_fahrenheit.grid(row=0, column=1)
btn_calc.grid(row=0, column=2)

lbl_celsius = tk.Label(
    master=window,
    text='Celsius:',
)
lbl_result = tk.Label(
    master=window,
    text='Enter your number...'
)

lbl_celsius.grid(row=1, column=0)
lbl_result.grid(row=1, column=1)

window.mainloop()
