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

calc_keys = [
    {
        'text': '7',
        'command': lambda: print('7'),
    },
    {
        'text': '8',
        'command': lambda: print('8'),
    },
    {
        'text': '9',
        'command': lambda: print('9'),
    },
    {
        'text': '+',
        'command': lambda: print('+'),
    },
    {
        'text': '4',
        'command': lambda: print('4'),
    },
    {
        'text': '5',
        'command': lambda: print('5'),
    },
    {
        'text': '6',
        'command': lambda: print('6'),
    },
    {
        'text': '-',
        'command': lambda: print('-'),
    },
    {
        'text': '1',
        'command': lambda: print('1'),
    },
    {
        'text': '2',
        'command': lambda: print('2'),
    },
    {
        'text': '3',
        'command': lambda: print('3'),
    },
    {
        'text': '*',
        'command': lambda: print('*'),
    },
    {
        'text': '.',
        'command': lambda: print('.'),
    },
    {
        'text': '0',
        'command': lambda: print('0'),
    },
    {
        'text': 'C',
        'command': lambda: print('C'),
    },
    {
        'text': '=',
        'command': lambda: print('='),
    },
]


calc_keys_objs = []

for calc_key_data in calc_keys: 
    btn = tk.Button(
        master=window,
        text=calc_key_data['text'],
        command=calc_key_data['command'],
        height=3,
    )
    calc_keys_objs.append(btn)

# 0,1,2,3 --> //4 = 0
# 4,5,6,7 --> //4 = 1
# 8,9,10,11 --> //4 = 2
# 12,13,14,15 --> //4 = 3
for i, calc_key_obj in enumerate(calc_keys_objs):
    calc_key_obj.grid(row=(i//4)+1, column=i%4, sticky='nsew')



# btn_7 = tk.Button(
#     master=window,
#     text='7',
#     command=lambda: print('7'),
#     height=3,
# )
# btn_7.grid(row=1, column=0, sticky='nsew')

# btn_8 = tk.Button(
#     master=window,
#     text='8',
#     command=lambda: print('8'),
#     height=3,
# )
# btn_8.grid(row=1, column=1, sticky='nsew')

# btn_9 = tk.Button(
#     master=window,
#     text='9',
#     command=lambda: print('9'),
#     height=3,
# )
# btn_9.grid(row=1, column=2, sticky='nsew')

# btn_plus = tk.Button(
#     master=window,
#     text='+',
#     command=lambda: print('+'),
#     height=3,
# )
# btn_plus.grid(row=1, column=3, sticky='nsew')

window.mainloop()

