import tkinter as tk
from tkinter import ttk

def cm_to_inch():
    cm = float(entry.get())
    inch = cm / 2.54
    output.config(text=f'{cm} cm is {inch:.2f} inches')

# Create the main window
window = tk.Tk()
window.title('Hello World')
window.geometry('400x200')

# title
title = ttk.Label(window, text='Enter centimeters', font = ('Arial', 24))
title.pack()

#input
input = ttk.Frame(window)
entry = ttk.Entry(input)
button = ttk.Button(input, text='Submit', command = cm_to_inch)
entry.pack(side='left', padx = 10)
button.pack(side='left')
input.pack(pady = 10)

#output
output = ttk.Label(window, text='Inches', font = ('Arial', 24))
output.pack()


window.mainloop()
