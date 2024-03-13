import tkinter as tk

# Fungsi untuk menghitung luas jajar genjang
def hitung_luas():
    a = float(panjang_entry.get())
    t = float(tinggi_entry.get())
    luas = a * t
    luas_label.config(text=f'Luas: {luas}')

# Fungsi untuk menghitung keliling jajar genjang
def hitung_keliling():
    a = float(panjang_entry.get())
    b = float(lebar_entry.get())
    keliling = 2 * (a + b)
    keliling_label.config(text=f'Keliling: {keliling}')

# Membuat jendela
window = tk.Tk()
window.title("Kalkulator Jajar Genjang")

# Label dan entry untuk panjang dan tinggi
panjang_label = tk.Label(window, text="Panjang:")
panjang_label.pack()
panjang_entry = tk.Entry(window)
panjang_entry.pack()

tinggi_label = tk.Label(window, text="Tinggi:")
tinggi_label.pack()
tinggi_entry = tk.Entry(window)
tinggi_entry.pack()

# Tombol untuk menghitung luas
luas_button = tk.Button(window, text="Hitung Luas", command=hitung_luas)
luas_button.configure(bg='yellow')
luas_button.pack()

# Label untuk hasil luas
luas_label = tk.Label(window, text="")
luas_label.pack()

# Label dan entry untuk lebar
lebar_label = tk.Label(window, text="Lebar:")
lebar_label.pack()
lebar_entry = tk.Entry(window)
lebar_entry.pack()

# Tombol untuk menghitung keliling
keliling_button = tk.Button(window, text="Hitung Keliling", command=hitung_keliling)
keliling_button.configure(bg='yellow')
keliling_button.pack()

# Label untuk hasil keliling
keliling_label = tk.Label(window, text="")
keliling_label.pack()

# Menjalankan aplikasi
window.mainloop()
