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



'''
# import calendar module
import calendar
 
# Function for showing the calendar of the given year
def showCal() :
 
    # Create a GUI window
    new_gui = tk.Tk()
     
    # Set the background colour of GUI window
    new_gui.config(background = "white")
 
    # set the name of tkinter GUI window
    new_gui.title("CALENDAR")
 
    # Set the configuration of GUI window
    new_gui.geometry("550x600")
 
    # get method returns current text as string
    fetch_year = int(year_field.get())
 
    # calendar method of calendar module return
    # the calendar of the given year .
    cal_content = calendar.calendar(fetch_year)
 
    # Create a label for showing the content of the calendar
    cal_year = tk.Label(new_gui, text = cal_content, font = "Consolas 10 bold")
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal_year.grid(row = 5, column = 1, padx = 20)
     
    # start the GUI
    new_gui.mainloop()
 
     
# Driver Code
if __name__ == "__main__" :
 
    # Create a GUI window
    gui = tk.Tk()
     
    # Set the background colour of GUI window
    gui.config(background = "white")
 
    # set the name of tkinter GUI window
    gui.title("CALENDAR")
 
    # Set the configuration of GUI window
    gui.geometry("250x140")
 
    # Create a CALENDAR : label with specified font and size
    cal = tk.Label(gui, text = "CALENDAR", bg = "dark gray",
                            font = ("times", 28, 'bold'))
 
    # Create a Enter Year : label
    year = tk.Label(gui, text = "Enter Year", bg = "light green")
     
    # Create a text entry box for filling or typing the information. 
    year_field = tk.Entry(gui)
 
    # Create a Show Calendar Button and attached to showCal function
    Show = tk.Button(gui, text = "Show Calendar", fg = "Black",
                              bg = "Red", command = showCal)
 
    # Create a Exit Button and attached to exit function
    Exit = tk.Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)
     
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal.grid(row = 1, column = 1)
 
    year.grid(row = 2, column = 1)
 
    year_field.grid(row = 3, column = 1)
 
    Show.grid(row = 4, column = 1)
 
    Exit.grid(row = 6, column = 1)
     
    # start the GUI
    gui.mainloop()
'''