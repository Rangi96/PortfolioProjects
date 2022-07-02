# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 20:57:34 2022

@author: jrangel
"""


import tkinter as tk
from tkinter import ttk
import tkcalendar as cale


def show_calendar():
    
        # Create a GUI window
    new_gui = tk.Tk()
    new_gui.title("codemy.com")
    new_gui.geometry('600x400')
    
    
    cal = cale.Calendar(new_gui, selectionmode = "day", year = 2020 , month = 5, day = 22)
    cal.pack(pady = 20, fill = "both", expand = True)
    
    def grab_date():
        my_label.config(text = "today :" + cal.get_date()) 
    
    my_button = tk.Button(new_gui, text = 'Get Date', command = grab_date)
    my_button.pack(pady=20)
     
    my_label = tk.Label(new_gui, text ="")
    my_label.pack(pady=20)
     
    new_gui.mainloop()

    

# root window
root = tk.Tk()
root.geometry("620x180")
root.title('Information Input')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# username
a_label = ttk.Label(root, text="Date:")
a_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

a_entry = ttk.Entry(root)
a_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

Show = ttk.Button(root, text = "Show Calendar", command = show_calendar)
Show.grid(row = 0, column = 2)

# password
c_label = ttk.Label(root, text="Description:")
c_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

c_entry = ttk.Entry(root)
c_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# username
e_label = ttk.Label(root, text="Category:")
e_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

e_entry = ttk.Entry(root)
e_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

# username
b_label = ttk.Label(root, text="Method:")
b_label.grid(column=4, row=0, sticky=tk.W, padx=5, pady=5)

b_entry = ttk.Entry(root)
b_entry.grid(column=5, row=0, sticky=tk.E, padx=5, pady=5)

# password
d_label = ttk.Label(root, text="Location:")
d_label.grid(column=4, row=1, sticky=tk.W, padx=5, pady=5)

d_entry = ttk.Entry(root)
d_entry.grid(column=5, row=1, sticky=tk.E, padx=5, pady=5)

# username
f_label = ttk.Label(root, text="Amount:")
f_label.grid(column=4, row=2, sticky=tk.W, padx=5, pady=5)

f_entry = ttk.Entry(root)
f_entry.grid(column=5, row=2, sticky=tk.E, padx=5, pady=5)

# login button
add_button = ttk.Button(root, text="Add")
add_button.grid(column=7, row=0, sticky=tk.E, padx=5, pady=5)

# login button
up_button = ttk.Button(root, text="Update")
up_button.grid(column=7, row=1, sticky=tk.E, padx=5, pady=5)

# login button
del_button = ttk.Button(root, text="Delete")
del_button.grid(column=7, row=2, sticky=tk.E, padx=5, pady=5)
root.mainloop()


