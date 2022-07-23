# Code by @AmirMotefaker

# GUI - Calculator

import tkinter as tk

window = tk.Tk()

lbl_calc_result = tk.Label(
    master=window,
    text='0',
    width=30,
    height=3,
)
lbl_calc_result.grid(row=0, column=0, columnspan=4)

btn_7 = tk.Button(
    master=window,
    text='7',
    command=lambda: print('7'),
)
btn_7.grid(row=1, column=0)

btn_8 = tk.Button(
    master=window,
    text='8',
    command=lambda: print('8'),
)
btn_8.grid(row=1, column=1)

btn_9 = tk.Button(
    master=window,
    text='9',
    command=lambda: print('9'),
)
btn_9.grid(row=1, column=2)

btn_plus = tk.Button(
    master=window,
    text='+',
    command=lambda: print('+'),
)
btn_plus.grid(row=1, column=3)

window.mainloop()

