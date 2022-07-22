# Code by @AmirMotefaker

# GUI - Temperature Conversion - (Fahrenheit to Celsius)

import tkinter as tk

window = tk.Tk()

fahrenheit_val = tk.StringVar()

lbl_result = tk.Label(
    master=window,
    text='Enter your number...'
)


def convert_fahrenheit_to_celsius():
    # user input value
    fahrenheit_input = fahrenheit_val.get()
    try:
        fahrenheit_value = float(fahrenheit_input)
        # Convert to Celsius
        lbl_result['text'] = (fahrenheit_value-32)*5/9
    except ValueError:
        if fahrenheit_input != '':
            # if user input is not valid
            lbl_result['text'] = 'You should enter a number'
        else:
            # if user input is empty
            lbl_result['text'] = 'Your input is empty.'

        

lbl_fahrenheit = tk.Label(
    master=window,
    text='Fahrenheit: ',
)
ent_fahrenheit = tk.Entry(
    master=window,
    width=50,
    textvariable=fahrenheit_val,
)
btn_calc = tk.Button(
    master=window,
    text='Calc',
    command=convert_fahrenheit_to_celsius,
)

lbl_fahrenheit.grid(row=0, column=0, padx=10, pady=10)
ent_fahrenheit.grid(row=0, column=1)
btn_calc.grid(row=0, column=2, padx=10, pady=10)

lbl_celsius = tk.Label(
    master=window,
    text='Celsius:',
)


lbl_celsius.grid(row=1, column=0, pady=(10, 20))
lbl_result.grid(row=1, column=1, pady=(10, 20))

window.title('Temperature Conversion by @AmirMotefaker')
window.mainloop()
