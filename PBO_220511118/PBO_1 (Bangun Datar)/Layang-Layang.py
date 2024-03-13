import tkinter as tk
import math

def hitung_luas_keliling():
    d1 = float(entry_d1.get())
    d2 = float(entry_d2.get())
    sisi = float(entry_sisi.get())

    luas = 0.5 * d1 * d2
    keliling = 2 * sisi

    label_hasil.config(text=f"Luas: {luas:.2f} satuan\nKeliling: {keliling:.2f} satuan")

app = tk.Tk()
app.title("Kalkulator Layang-layang")

frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

label_d1 = tk.Label(frame, text="Diagonal 1:")
label_d1.grid(row=0, column=0)
entry_d1 = tk.Entry(frame)
entry_d1.grid(row=0, column=1)

label_d2 = tk.Label(frame, text="Diagonal 2:")
label_d2.grid(row=1, column=0)
entry_d2 = tk.Entry(frame)
entry_d2.grid(row=1, column=1)

label_sisi = tk.Label(frame, text="Panjang Sisi:")
label_sisi.grid(row=2, column=0)
entry_sisi = tk.Entry(frame)
entry_sisi.grid(row=2, column=1)

hitung_button = tk.Button(frame, text="Hitung", command=hitung_luas_keliling)
hitung_button.grid(row=3, column=0, columnspan=2)

label_hasil = tk.Label(frame, text="", font=("Helvetica", 14))
label_hasil.grid(row=4, column=0, columnspan=2)
app.mainloop()
