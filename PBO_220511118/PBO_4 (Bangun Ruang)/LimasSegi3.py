import tkinter as tk
from tkinter import ttk

def hitung_luas():
    try:
        alas = float(alas_entry.get())
        tinggi = float(tinggi_entry.get())
        luas = 0.5 * alas * tinggi
        hasil_luas.set(f"Luas: {luas:.2f}")
    except ValueError:
        hasil_luas.set("Masukkan angka yang valid")

def hitung_volume():
    try:
        alas = float(alas_entry.get())
        tinggi = float(tinggi_entry.get())
        tinggi_limas = float(tinggi_limas_entry.get())
        volume = (1/3) * (alas * tinggi_limas)
        hasil_volume.set(f"Volume: {volume:.2f}")
    except ValueError:
        hasil_volume.set("Masukkan angka yang valid")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Limas Segitiga")

# Label Nama
nama_label = tk.Label(root, text="Muhammad Hafid Aridwan | 220511118")
nama_label.grid(row=10, column=5, columnspan=2, sticky="W", padx=10, pady=0)

# Membuat label dan entry widget untuk alas dan tinggi segitiga
alas_label = ttk.Label(root, text="Alas segitiga:")
alas_label.grid(row=0, column=0)
alas_entry = ttk.Entry(root)
alas_entry.grid(row=0, column=1)

tinggi_label = ttk.Label(root, text="Tinggi segitiga:")
tinggi_label.grid(row=1, column=0)
tinggi_entry = ttk.Entry(root)
tinggi_entry.grid(row=1, column=1)

# Membuat label dan entry widget untuk tinggi limas
tinggi_limas_label = ttk.Label(root, text="Tinggi limas:")
tinggi_limas_label.grid(row=3, column=0)
tinggi_limas_entry = ttk.Entry(root)
tinggi_limas_entry.grid(row=3, column=1)

# Tombol untuk menghitung luas dan volume
hitung_luas_button = ttk.Button(root, text="Hitung Luas", command=hitung_luas)
hitung_luas_button.grid(row=5, column=1)

hitung_volume_button = ttk.Button(root, text="Hitung Volume", command=hitung_volume)
hitung_volume_button.grid(row=6, column=1)

# Variabel untuk menampilkan hasil perhitungan
hasil_luas = tk.StringVar()
hasil_luas.set("Luas: ")
hasil_volume = tk.StringVar()
hasil_volume.set("Volume: ")

hasil_luas_label = ttk.Label(root, textvariable=hasil_luas)
hasil_luas_label.grid(row=0, column=3, columnspan=3)

hasil_volume_label = ttk.Label(root, textvariable=hasil_volume)
hasil_volume_label.grid(row=1, column=3, columnspan=3)

root.mainloop()
