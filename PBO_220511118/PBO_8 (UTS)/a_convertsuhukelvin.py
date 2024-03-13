import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
                
        if from_unit == "Kelvin":
            if to_unit == "Celcius:":
                result = temperature - 273
            elif to_unit == "Fahrenheit":
                result = 9/5 * (temperature - 273) + 32
            elif to_unit == "Reamur":
                result = 4/5 * (temperature - 273)
            else:
                result = temperature

        entry_result_var.set(f"{result:.2f} {to_unit}")
    except ValueError:
        entry_result_var.set("Invalid input. Please enter a number.")

# Create main window
root = tk.Tk()
root.title("Temperature Convert-Qu")
root.geometry("305x200")
root.resizable(False,False)

# ICON
image_icon = tk.PhotoImage(file="b_iconconvertsuhu.png")
root.iconphoto(True, image_icon)

# Create widgets
label_temperature = ttk.Label(root, text="Enter Temperature :")
entry_temperature = ttk.Entry(root, width=27)
label_from = ttk.Label(root, text="From                        :")
combo_from = ttk.Combobox(root, width=24, values=["Celcius", "Fahrenheit", "Reamur", "Kelvin"])
label_to = ttk.Label(root, text="To                             :")
combo_to = ttk.Combobox(root, width=24, values=["Celcius", "Fahrenheit", "Reamur", "Kelvin"])
convert_button = ttk.Button(root, padding=2, text="Convert", command=convert_temperature)
result_label = ttk.Label(root, text="Result : ")
entry_result_var = tk.StringVar()
entry_result = ttk.Entry(root, textvariable=entry_result_var, width=20)

# Place widgets in the grid
label_temperature.grid(row=0, column=0, padx=5, pady=5)
entry_temperature.grid(row=0, column=1, padx=5, pady=5)
label_from.grid(row=1, column=0, padx=5, pady=5)
combo_from.grid(row=1, column=1, padx=5, pady=5)
label_to.grid(row=2, column=0, padx=5, pady=5)
combo_to.grid(row=2, column=1, padx=5, pady=5)
convert_button.place(x=120, y=100)
result_label.place(x=120, y=140)
entry_result.place(x=164, y=140)

# Start the Tkinter event loop
root.mainloop()
