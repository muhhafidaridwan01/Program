import tkinter as tk
from tkinter import *

from FrmPersegi import *
from FrmSegitiga import *
from FrmLingkaran import *
from FrmBola import *

# root window
root = tk.Tk()
root.title('Menu Demo')
root.geometry("400x400")


# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create menus
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add items to the File menu
file_menu.add_command(label='File Open', command=root.destroy)
file_menu.add_command(label='Exit', command=root.destroy)

# add items to the App menu
app_menu.add_command(label='App Persegi', command=lambda: new_window("Luas Persegi", FrmPersegi))
app_menu.add_command(label='App Segitiga', command=lambda: new_window("Luas Segitiga", FrmSegitiga))
app_menu.add_command(label='App Lingkaran', command=lambda: new_window("Luas Lingkaran", FrmLingkaran))
app_menu.add_command(label='App Bola', command=lambda: new_window("Luas Bola", Bola))

# add menus to the menubar
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="App", menu=app_menu)

# function to create a new window
def new_window(number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

root.mainloop()
