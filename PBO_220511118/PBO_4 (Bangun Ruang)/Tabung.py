import tkinter as tk
from tkinter import messagebox
import math

# Fungsi untuk menghitung luas tabung
def hitung_luas():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())
        luas = 2 * math.pi * jari_jari * (jari_jari + tinggi)
        hasil_luas.config(text=f'Luas Tabung: {luas:.2f} satuan persegi')
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid")

# Fungsi untuk menghitung volume tabung
def hitung_volume():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())
        volume = math.pi * jari_jari**2 * tinggi
        hasil_volume.config(text=f'Volume Tabung: {volume:.2f} satuan kubik')
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid")

# Membuat window
window = tk.Tk()
window.title("Kalkulator Tabung")

# Windows
frame = tk.Frame(window)
frame.pack(padx=30, pady=10)

# Label Nama
nama_label = tk.Label(window, text="Muhammad Hafid Aridwan | 220511118")
nama_label.pack()

# Membuat label dan entry untuk jari-jari
label_jari_jari = tk.Label(window, text="Jari-Jari Tabung:")
label_jari_jari.pack()
entry_jari_jari = tk.Entry(window)
entry_jari_jari.pack()

# Membuat label dan entry untuk tinggi
label_tinggi = tk.Label(window, text="Tinggi Tabung:")
label_tinggi.pack()
entry_tinggi = tk.Entry(window)
entry_tinggi.pack()

# Tombol untuk menghitung luas dan volume
hitung_luas_button = tk.Button(window, text="Hitung Luas Tabung", command=hitung_luas)
hitung_luas_button.pack()
hasil_luas = tk.Label(window, text="")
hasil_luas.pack()

hitung_volume_button = tk.Button(window, text="Hitung Volume Tabung", command=hitung_volume)
hitung_volume_button.pack()
hasil_volume = tk.Label(window, text="")
hasil_volume.pack()

window.mainloop()
