import tkinter as tk
from tkinter import messagebox
import math

# Fungsi untuk menghitung luas permukaan dan volume kerucut
def hitung_kerucut():
    try:
        radius = float(entry_radius.get())
        height = float(entry_height.get())
        
        # Hitung luas permukaan kerucut
        surface_area = math.pi * radius * (radius + math.sqrt(radius**2 + height**2))
        
        # Hitung volume kerucut
        volume = (1/3) * math.pi * radius**2 * height
        
        # Tampilkan hasil
        result_text = f"Luas Permukaan: {surface_area:.2f}\nVolume: {volume:.2f}"
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Kesalahan", "Masukkan angka yang valid untuk radius dan tinggi.")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Kerucut")

# Windows
frame = tk.Frame(root)
frame.pack(padx=30, pady=30)

# Label Nama
nama_label = tk.Label(frame, text="Muhammad Hafid Aridwan | 220511118")
nama_label.grid(row=0, column=0, columnspan=2, sticky="W", padx=5, pady=1)

# Membuat label untuk radius
label_radius = tk.Label(root, text="Radius:")
label_radius.pack()

# Membuat input untuk radius
entry_radius = tk.Entry(root)
entry_radius.pack()

# Membuat label untuk tinggi
label_height = tk.Label(root, text="Tinggi:")
label_height.pack()

# Membuat input untuk tinggi
entry_height = tk.Entry(root)
entry_height.pack()

# Tombol untuk menghitung
calculate_button = tk.Button(root, text="Hitung", command=hitung_kerucut)
calculate_button.pack()

# Label untuk menampilkan hasil
result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack()

# Menjalankan aplikasi
root.mainloop()
