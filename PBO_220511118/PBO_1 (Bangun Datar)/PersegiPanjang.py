import tkinter as tk

# Fungsi untuk menghitung luas dan keliling persegi
def hitung():
    sisi = float(entry_sisi.get())
    luas = sisi ** 2
    keliling = 4 * sisi
    hasil_luas.config(text=f"Luas: {luas}")
    hasil_keliling.config(text=f"Keliling: {keliling}")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Persegi")

# Membuat label dan entry untuk memasukkan panjang sisi
label_sisi = tk.Label(root, text="Panjang Sisi:")
label_sisi.pack()
entry_sisi = tk.Entry(root)
entry_sisi.pack()

# Membuat tombol "Hitung" untuk menghitung luas dan keliling
hitung_button = tk.Button(root, text="Hitung", command=hitung)
hitung_button.configure(bg='yellow')
hitung_button.pack()

# Menampilkan hasil perhitungan luas dan keliling
hasil_luas = tk.Label(root, text="")
hasil_luas.pack()
hasil_keliling = tk.Label(root, text="")
hasil_keliling.pack()

# Menjalankan aplikasi
root.mainloop()
