import tkinter as tk

windows = tk.Tk()
windows.title('My Calculator')

lbl_calc_result = tk.Label(
    master=windows,
    text='0',
    width=30,
    height=3
)

lbl_calc_result.grid(row=0, column=0, columnspan=4)


def insert_number_in_calc_result(btn_text):
    current = lbl_calc_result['text']
    if current == '0':
        lbl_calc_result['text'] = btn_text
    elif btn_text == '=':
        lbl_calc_result['text'] = f"{eval(current)}"
    else:
        if btn_text == '+' or btn_text == '-' or btn_text == '*':
            if current[-1] == '+' or current[-1] == '-' or current[-1] == '*':
                lbl_calc_result['text'] = current[:-1] + btn_text
            else:
                lbl_calc_result['text'] += btn_text
        else:
            lbl_calc_result['text'] += btn_text


cals_keys = [
    {
        'text': '7',
        'command': lambda: insert_number_in_calc_result('7'),
    },
    {
        'text': '8',
        'command': lambda: insert_number_in_calc_result('8'),
    },
    {
        'text': '9',
        'command': lambda: insert_number_in_calc_result('9'),
    },
    {
        'text': '+',
        'command': lambda: insert_number_in_calc_result('+'),
    },
    {
        'text': '4',
        'command': lambda: insert_number_in_calc_result('4'),
    },
    {
        'text': '5',
        'command': lambda: insert_number_in_calc_result('5'),
    },
    {
        'text': '6',
        'command': lambda: insert_number_in_calc_result('6'),
    },
    {
        'text': '-',
        'command': lambda: insert_number_in_calc_result('-'),
    },
    {
        'text': '1',
        'command': lambda: insert_number_in_calc_result('1'),
    },
    {
        'text': '2',
        'command': lambda: insert_number_in_calc_result('2'),
    },
    {
        'text': '3',
        'command': lambda: insert_number_in_calc_result('3'),
    },
    {
        'text': '*',
        'command': lambda: insert_number_in_calc_result('*'),
    },
    {
        'text': '.',
        'command': lambda: insert_number_in_calc_result('.'),
    },
    {
        'text': '0',
        'command': lambda: insert_number_in_calc_result('0'),
    },
    {
        'text': 'C',
        'command': lambda: insert_number_in_calc_result('C'),
    },
    {
        'text': '=',
        'command': lambda: insert_number_in_calc_result('='),
    },
]

calc_keys_objs = []

for calc_key_data in cals_keys:
    btn = tk.Button(
        master=windows,
        text=calc_key_data['text'],
        command=calc_key_data['command'],
        height=3
    )
    calc_keys_objs.append(btn)

for i, calc_key_obj in enumerate(calc_keys_objs):
    calc_key_obj.grid(row=(i//4)+1, column=i % 4, sticky='nsew')


windows.mainloop()
