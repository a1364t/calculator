import tkinter as tk

windows = tk.Tk()

lbl_calc_result = tk.Label(
    master=windows,
    text='0',
    width=30,
    height=3
)

lbl_calc_result.grid(row=0, column=0)

windows.mainloop()
