from tkinter import Frame, Label, Entry, Button, END, Tk, W, PhotoImage

class TemperatureConverter:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.setup_ui()

    def setup_ui(self):
        main_frame = Frame(self.parent, bd=10)
        main_frame.pack(fill="both", expand=True)

        Label(main_frame, text='Celsius:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text="Fahrenheit:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text="Reamur:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text="Kelvin :").grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txt_celsius = Entry(main_frame, width="23")
        self.txt_celsius.grid(row=0, column=1, padx=5, pady=5)

        self.txt_fahrenheit = Entry(main_frame, width="23")
        self.txt_fahrenheit.grid(row=2, column=1, padx=5, pady=5)

        self.txt_reamur = Entry(main_frame, width="23")
        self.txt_reamur.grid(row=3, column=1, padx=5, pady=5)

        self.txt_kelvin = Entry(main_frame, width="23")
        self.txt_kelvin.grid(row=4, column=1, padx=5, pady=5)

        self.btn_calculate = Button(main_frame, width="10", text='Calculate', command=self.on_calculate)
        self.btn_calculate.grid(row=1, column=1, padx=5, pady=5)

    def get_fahrenheit(self, celsius):
        return (9/5 * celsius) + 32

    def get_reamur(self, celsius):
        return 4/5 * celsius

    def get_kelvin(self, celsius):
        return celsius + 273

    def on_calculate(self):
        try:
            celsius = float(self.txt_celsius.get())
            fahrenheit = self.get_fahrenheit(celsius)
            reamur = self.get_reamur(celsius)
            kelvin = self.get_kelvin(celsius)

            self.txt_fahrenheit.delete(0, END)
            self.txt_fahrenheit.insert(END, str(fahrenheit))

            self.txt_reamur.delete(0, END)
            self.txt_reamur.insert(END, str(reamur))

            self.txt_kelvin.delete(0, END)
            self.txt_kelvin.insert(END, str(kelvin))
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a numeric value.")

    def on_exit(self):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()

    # ICON
    image_icon = PhotoImage(file="b_iconconvertsuhu.png")
    root.iconphoto(True, image_icon)

    aplikasi = TemperatureConverter(root, "Celsius-Qu")
    root.geometry("250x190")
    root.resizable(False, False)
    root.mainloop()
