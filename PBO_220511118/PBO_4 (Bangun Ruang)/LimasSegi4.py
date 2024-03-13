import tkinter as tk
from tkinter import ttk
import math

# Fungsi untuk menghitung luas permukaan dan volume limas segi empat
def hitung_luas_volume():
    panjang = float(panjang_entry.get())
    lebar = float(lebar_entry.get())
    tinggi = float(tinggi_entry.get())
    
    # Hitung luas permukaan
    luas_permukaan = panjang * lebar + 2 * panjang * tinggi + 2 * lebar * tinggi
    luas_permukaan_label.config(text=f"Luas Permukaan: {luas_permukaan:.2f} satuan^2")

    # Hitung volume
    volume = (panjang * lebar * tinggi) / 3
    volume_label.config(text=f"Volume: {volume:.2f} satuan^3")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Limas Segi Empat")
root.geometry("300x200")

# Label Nama
nama_label = tk.Label(root, text="Muhammad Hafid Aridwan | 220511118")
nama_label.pack()

# Label dan Entry untuk panjang
panjang_label = ttk.Label(root, text="Panjang:")
panjang_label.pack()
panjang_entry = ttk.Entry(root)
panjang_entry.pack()

# Label dan Entry untuk lebar
lebar_label = ttk.Label(root, text="Lebar:")
lebar_label.pack()
lebar_entry = ttk.Entry(root)
lebar_entry.pack()

# Label dan Entry untuk tinggi
tinggi_label = ttk.Label(root, text="Tinggi:")
tinggi_label.pack()
tinggi_entry = ttk.Entry(root)
tinggi_entry.pack()

# Tombol untuk menghitung
hitung_button = ttk.Button(root, text="Hitung", command=hitung_luas_volume)
hitung_button.pack()

# Label untuk menampilkan hasil perhitungan
luas_permukaan_label = ttk.Label(root, text="")
luas_permukaan_label.pack()
volume_label = ttk.Label(root, text="")
volume_label.pack()

root.mainloop()
