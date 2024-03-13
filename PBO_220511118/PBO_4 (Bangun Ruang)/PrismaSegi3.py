import tkinter as tk
from tkinter import messagebox
import math

# Fungsi untuk menghitung luas prisma segitiga
def hitung_luas():
    try:
        alas = float(entry_alas.get())
        tinggi_alas = float(entry_tinggi_alas.get())
        tinggi_prisma = float(entry_tinggi_prisma.get())
        luas = (alas * tinggi_alas) + (3 * (alas * tinggi_prisma))
        hasil_luas.config(text=f'Luas Prisma Segitiga: {luas:.2f} satuan persegi')
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid")

# Fungsi untuk menghitung volume prisma segitiga
def hitung_volume():
    try:
        alas = float(entry_alas.get())
        tinggi_alas = float(entry_tinggi_alas.get())
        tinggi_prisma = float(entry_tinggi_prisma.get())
        volume = (alas * tinggi_alas * tinggi_prisma) / 2
        hasil_volume.config(text=f'Volume Prisma Segitiga: {volume:.2f} satuan kubik')
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid")

# Membuat window
window = tk.Tk()
window.title("Kalkulator Prisma Segitiga")

# Label Nama
nama_label = tk.Label(window, text ="Muhammad Hafid Aridwan | 220511118")
nama_label.pack()

# Membuat label dan entry untuk alas segitiga
label_alas = tk.Label(window, text="Alas Segitiga:")
label_alas.pack()
entry_alas = tk.Entry(window)
entry_alas.pack()

# Membuat label dan entry untuk tinggi alas segitiga
label_tinggi_alas = tk.Label(window, text="Tinggi Alas Segitiga:")
label_tinggi_alas.pack()
entry_tinggi_alas = tk.Entry(window)
entry_tinggi_alas.pack()

# Membuat label dan entry untuk tinggi prisma segitiga
label_tinggi_prisma = tk.Label(window, text="Tinggi Prisma Segitiga:")
label_tinggi_prisma.pack()
entry_tinggi_prisma = tk.Entry(window)
entry_tinggi_prisma.pack()

# Tombol untuk menghitung luas dan volume
hitung_luas_button = tk.Button(window, text="Hitung Luas", command=hitung_luas)
hitung_luas_button.pack()
hasil_luas = tk.Label(window, text="")
hasil_luas.pack()

hitung_volume_button = tk.Button(window, text="Hitung Volume", command=hitung_volume)
hitung_volume_button.pack()
hasil_volume = tk.Label(window, text="")
hasil_volume.pack()

window.mainloop()
