# Code by @AmirMotefaker

# GUI - Calculator

import tkinter as tk

calc_keys = [
    {
        'text': '7',
        'command': lambda: insert_number_in_clac_result('7'),
    },
    {
        'text': '8',
        'command': lambda: insert_number_in_clac_result('8'),
    },
    {
        'text': '9',
        'command': lambda: insert_number_in_clac_result('9'),
    },
    {
        'text': '+',
        'command': lambda: insert_number_in_clac_result('+'),
    },
    {
        'text': '4',
        'command': lambda: insert_number_in_clac_result('4'),
    },
    {
        'text': '5',
        'command': lambda: insert_number_in_clac_result('5'),
    },
    {
        'text': '6',
        'command': lambda: insert_number_in_clac_result('6'),
    },
    {
        'text': '-',
        'command': lambda: insert_number_in_clac_result('-'),
    },
    {
        'text': '1',
        'command': lambda: insert_number_in_clac_result('1'),
    },
    {
        'text': '2',
        'command': lambda: insert_number_in_clac_result('2'),
    },
    {
        'text': '3',
        'command': lambda: insert_number_in_clac_result('3'),
    },
    {
        'text': '*',
        'command': lambda: insert_number_in_clac_result('*'),
    },
    {
        'text': '.',
        'command': lambda: insert_number_in_clac_result('.'),
    },
    {
        'text': '0',
        'command': lambda: insert_number_in_clac_result('0'),
    },
    {
        'text': 'C',
        'command': lambda: insert_number_in_clac_result('C'),
    },
    {
        'text': '=',
        'command': lambda: insert_number_in_clac_result('='),
    },
]

window = tk.Tk()

lbl_calc_result = tk.Label(
    master=window,
    text='0',
    width=30,
    height=3,
)
lbl_calc_result.grid(row=0, column=0, columnspan=4)

last_op_index = -1
last_dot_index = -1

def insert_number_in_clac_result(btn_text):
    current = lbl_calc_result['text']

    global last_op_index, last_dot_index
    if btn_text in ['+', '-', '*']:
        last_op_index = len(current)
    
    if btn_text == 'C':
        lbl_calc_result['text'] = '0'
        last_op_index, last_dot_index = 0, 0
    elif current == '0':
        lbl_calc_result['text'] = btn_text
    elif btn_text == '=':
        result = f"{eval(current)}"
        lbl_calc_result['text'] = result
        last_op_index, last_dot_index = 0, 0
        if '.' in result:
            last_dot_index = result.index('.')
    elif btn_text == '.' and not (last_dot_index > last_op_index or current[-1] == '.'):
        lbl_calc_result['text'] += btn_text
        last_dot_index = len(current)
    elif btn_text in ['+', '-', '*'] and current[-1] in ['+', '-', '*']:
        lbl_calc_result['text'] = current[:-1] + btn_text
    else:
        lbl_calc_result['text'] += btn_text
                
calc_keys_objs = []
for calc_key_data in calc_keys: 
    btn = tk.Button(
        master=window,
        text=calc_key_data['text'],
        command=calc_key_data['command'],
        height=3,
    )
    calc_keys_objs.append(btn)

for i, calc_key_obj in enumerate(calc_keys_objs):
    calc_key_obj.grid(row=(i//4)+1, column=i%4, sticky='nsew')

window.mainloop()
