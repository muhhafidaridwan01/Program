import tkinter as tk

def hitung_luas():
    sisi = float(entry_sisi.get())
    luas = sisi * sisi
    hasil_luas.set(f"Luas Persegi: {luas}")

def hitung_keliling():
    sisi = float(entry_sisi.get())
    keliling = 4 * sisi
    hasil_keliling.set(f"Keliling Persegi: {keliling}")

# Membuat jendela
window = tk.Tk()
window.title("Kalkulator Persegi")

# Label dan Entry untuk mengisi panjang sisi
label_sisi = tk.Label(window, text="Panjang Sisi:")
label_sisi.pack()
entry_sisi = tk.Entry(window)
entry_sisi.pack()

# Tombol untuk menghitung luas dan keliling
hitung_luas_button = tk.Button(window, text="Hitung Luas", command=hitung_luas)
hitung_luas_button.configure(bg='yellow')
hitung_luas_button.pack()
hitung_keliling_button = tk.Button(window, text="Hitung Keliling", command=hitung_keliling)
hitung_keliling_button.configure(bg='blue')
hitung_keliling_button.pack()

# Label untuk menampilkan hasil
hasil_luas = tk.StringVar()
hasil_keliling = tk.StringVar()
label_hasil_luas = tk.Label(window, textvariable=hasil_luas)
label_hasil_keliling = tk.Label(window, textvariable=hasil_keliling)
label_hasil_luas.pack()
label_hasil_keliling.pack()

# Menjalankan jendela
window.mainloop()
