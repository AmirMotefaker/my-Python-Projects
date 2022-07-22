# Code by @AmirMotefaker

# Temperature Conversion

import tkinter as tk

window = tk.Tk()

fahrenheit_name = tk.Label(
    master=window,
    text='Fahrenheit: ',
)
fahrenheit_entry = tk.Entry(
    master=window,
)
calc_button = tk.Button(
    master=window,
    text='Calc',
)

fahrenheit_name.grid(row=0, column=0)
fahrenheit_entry.grid(row=0, column=1)
calc_button.grid(row=0, column=2)

window.mainloop()
