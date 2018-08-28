from tkinter import Tk
from tkinter import *
from tkinter import ttk, Label, Entry, Button, E, W, messagebox

def quit_app():
    root.quit()

def show_about(event=None):
    messagebox.showwarning(
        "About"
        "This awesome program was made in 2018"
    )

root = Tk()

# Creating a dropdown menu
the_menu = Menu(root)

file_menu = Menu(the_menu, tearoff=0)

# adding items to my menu
file_menu.add_command(label="Open")

file_menu.add_command(label="Save")

file_menu.add_separator()

file_menu.add_command(label="Quit", command=quit_app)

the_menu.add_cascade(label="File", menu=file_menu)




root.config(menu=the_menu)

# Keep the window open unitl the user hits the 'close' button
root.mainloop()
