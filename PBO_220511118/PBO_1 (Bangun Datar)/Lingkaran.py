import tkinter as tk
import math

# Fungsi untuk menghitung luas dan keliling lingkaran
def hitung_lingkaran():
    try:
        jari_jari = float(entry_jari_jari.get())
        luas = math.pi * jari_jari**2
        keliling = 2 * math.pi * jari_jari
        label_hasil.config(text=f"Luas: {luas:.2f}\nKeliling: {keliling:.2f}")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid")

# Membuat jendela
root = tk.Tk()
root.title("Hitung Lingkaran")

# Label
label_jari_jari = tk.Label(root, text="Jari-jari lingkaran:")
label_jari_jari.pack()

# Masukan (Entry) untuk jari-jari
entry_jari_jari = tk.Entry(root)
entry_jari_jari.pack()

# Tombol hitung
hitung_button = tk.Button(root, text="Hitung", command=hitung_lingkaran)
hitung_button.configure(bg='yellow')
hitung_button.pack()

# Label hasil
label_hasil = tk.Label(root, text="")
label_hasil.pack()

# Memulai aplikasi
root.mainloop()
