import tkinter as tk
import math

def hitung_luas():
    try:
        alas = float(alas_entry.get())
        tinggi = float(tinggi_entry.get())
        luas = 0.5 * alas * tinggi
        luas_label.config(text=f'Luas: {luas}')
    except ValueError:
        luas_label.config(text='Masukkan angka valid')

def hitung_keliling():
    try:
        sisi1 = float(sisi1_entry.get())
        sisi2 = float(sisi2_entry.get())
        sisi3 = float(sisi3_entry.get())
        keliling = sisi1 + sisi2 + sisi3
        keliling_label.config(text=f'Keliling: {keliling}')
    except ValueError:
        keliling_label.config(text='Masukkan angka valid')

# Membuat window
window = tk.Tk()
window.title('Kalkulator Segitiga')

# Membuat label dan entry untuk menginputkan alas dan tinggi
alas_label = tk.Label(window, text='Alas:')
alas_label.pack()
alas_entry = tk.Entry(window)
alas_entry.pack()

tinggi_label = tk.Label(window, text='Tinggi:')
tinggi_label.pack()
tinggi_entry = tk.Entry(window)
tinggi_entry.pack()

hitung_luas_button = tk.Button(window, text='Hitung Luas', command=hitung_luas)
hitung_luas_button.configure(bg='blue')
hitung_luas_button.pack()

luas_label = tk.Label(window, text='')
luas_label.pack()

# Membuat label dan entry untuk menginputkan sisi-sisi segitiga
sisi1_label = tk.Label(window, text='Sisi 1:')
sisi1_label.pack()
sisi1_entry = tk.Entry(window)
sisi1_entry.pack()

sisi2_label = tk.Label(window, text='Sisi 2:')
sisi2_label.pack()
sisi2_entry = tk.Entry(window)
sisi2_entry.pack()

sisi3_label = tk.Label(window, text='Sisi 3:')
sisi3_label.pack()
sisi3_entry = tk.Entry(window)
sisi3_entry.pack()

hitung_keliling_button = tk.Button(window, text='Hitung Keliling', command=hitung_keliling)
hitung_keliling_button.configure(bg='yellow')
hitung_keliling_button.pack()

keliling_label = tk.Label(window, text='')
keliling_label.pack()

window.mainloop()
