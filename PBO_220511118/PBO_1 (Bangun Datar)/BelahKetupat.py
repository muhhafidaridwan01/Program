import tkinter as tk

def hitung_luas_dan_keliling():
    sisi = float(entry_sisi.get())
    luas = sisi * sisi
    keliling = 4 * sisi
    hasil_label.config(text=f"Luas: {luas}\nKeliling: {keliling}")

# Membuat jendela utama
window = tk.Tk()
window.title("Kalkulator Belah Ketupat")

# Membuat label untuk sisi
sisi_label = tk.Label(window, text="Masukkan panjang sisi belah ketupat:")
sisi_label.pack()

# Membuat input untuk sisi
entry_sisi = tk.Entry(window)
entry_sisi.pack()

# Membuat tombol untuk menghitung
hitung_button = tk.Button(window, text="Hitung", command=hitung_luas_dan_keliling)
hitung_button.configure(bg='yellow')
hitung_button.pack()

# Membuat label untuk menampilkan hasil
hasil_label = tk.Label(window, text="")
hasil_label.pack()

# Menjalankan loop utama
window.mainloop()
