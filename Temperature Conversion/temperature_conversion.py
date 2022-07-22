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

window.mainloop()
