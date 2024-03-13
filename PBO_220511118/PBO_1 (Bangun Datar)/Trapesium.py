import tkinter as tk

def hitung_luas_trapesium():
    try:
        atas = float(entry_atas.get())
        bawah = float(entry_bawah.get())
        tinggi = float(entry_tinggi.get())
        
        luas = 0.5 * (atas + bawah) * tinggi
        label_hasil.config(text=f'Luas Trapesium: {luas}')
    except ValueError:
        label_hasil.config(text='Masukkan bilangan valid')

# Membuat jendela utama
root = tk.Tk()
root.title('Hitung Luas Trapesium')

# Membuat label dan input fields
label_atas = tk.Label(root, text='Panjang Atas:')
label_atas.grid(row=0, column=0)
entry_atas = tk.Entry(root)
entry_atas.grid(row=0, column=1)

label_bawah = tk.Label(root, text='Panjang Bawah:')
label_bawah.grid(row=1, column=0)
entry_bawah = tk.Entry(root)
entry_bawah.grid(row=1, column=1)

label_tinggi = tk.Label(root, text='Tinggi:')
label_tinggi.grid(row=2, column=0)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=2, column=1)

# Tombol untuk menghitung luas
button_hitung = tk.Button(root, text='Hitung Luas', command=hitung_luas_trapesium)
button_hitung .configure(bg='yellow')
button_hitung.grid(row=3, column=0, columnspan=2)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text='')
label_hasil.grid(row=4, column=0, columnspan=2)

# Memulai loop Tkinter
root.mainloop()
