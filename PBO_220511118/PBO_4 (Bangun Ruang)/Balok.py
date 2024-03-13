import tkinter as tk

def hitung_luas():
    panjang = float(panjang_entry.get())
    lebar = float(lebar_entry.get())
    tinggi = float(tinggi_entry.get())
    luas = panjang * lebar
    hasil_luas_label.config(text=f'Luas: {luas}')

def hitung_volume():
    panjang = float(panjang_entry.get())
    lebar = float(lebar_entry.get())
    tinggi = float(tinggi_entry.get())
    volume = panjang * lebar * tinggi
    hasil_volume_label.config(text=f'Volume: {volume}')

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Balok")

# Windows
frame = tk.Frame(root)
frame.pack(padx=30, pady=10)

# Label Nama
nama_label = tk.Label(frame, text="Muhammad Hafid Aridwan | 220511118")
nama_label.grid(row=0, column=0, columnspan=2, sticky="W", padx=5, pady=5)

# Membuat label dan entry widget untuk panjang
panjang_label = tk.Label(root, text="Panjang:")
panjang_label.pack()
panjang_entry = tk.Entry(root)
panjang_entry.pack()

# Membuat label dan entry widget untuk lebar
lebar_label = tk.Label(root, text="Lebar:")
lebar_label.pack()
lebar_entry = tk.Entry(root)
lebar_entry.pack()

# Membuat label dan entry widget untuk tinggi
tinggi_label = tk.Label(root, text="Tinggi:")
tinggi_label.pack()
tinggi_entry = tk.Entry(root)
tinggi_entry.pack()

# Membuat tombol untuk menghitung luas
hitung_luas_button = tk.Button(root, text="Hitung Luas", command=hitung_luas)
hitung_luas_button.pack()
hasil_luas_label = tk.Label(root, text="")
hasil_luas_label.pack()

# Membuat tombol untuk menghitung volume
hitung_volume_button = tk.Button(root, text="Hitung Volume", command=hitung_volume)
hitung_volume_button.pack()
hasil_volume_label = tk.Label(root, text="")
hasil_volume_label.pack()

# Menjalankan aplikasi
root.mainloop()
