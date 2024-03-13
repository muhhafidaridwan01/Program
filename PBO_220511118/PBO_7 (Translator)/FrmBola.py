import tkinter as tk
from tkinter import Label, Entry, Button, END, W

class Bola:
    def __init__(self, master, title):
        self.master = master
        self.master.title(title)

        # Windows
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)

        # Label Nama
        self.nama_label = Label(self.frame, text="Muhammad Hafid Aridwan | 220511118")
        self.nama_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5)

        # Label Radius
        self.radius_label = Label(self.frame, text="Radius :")
        self.radius_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        # Textbox Radius
        self.txtradius = Entry(self.frame)
        self.txtradius.grid(row=1, column=1)

        # Button
        self.hitung_button = Button(self.frame, text="Hitung", command=self.hitung_volume_dan_luas_permukaan)
        self.hitung_button.grid(row=2, column=1, columnspan=2, pady=2)

        # Output Label Volume
        self.volume_label = Label(self.frame, text="Volume : ")
        self.volume_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        # Output Textbox Volume
        self.txtVolume = Entry(self.frame)
        self.txtVolume.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        # Output Label Luas Permukaan
        self.luas_permukaan_label = Label(self.frame, text="Luas Permukaan : ")
        self.luas_permukaan_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        # Output Textbox Luas Permukaan
        self.txtLuasPermukaan = Entry(self.frame)
        self.txtLuasPermukaan.grid(row=4, column=1, sticky=W, padx=5, pady=5)

    def hitung_volume_dan_luas_permukaan(self):
        r = float(self.txtradius.get())
        volume = round((4/3) * 3.14159 * r**3, 2)
        luas_permukaan = round(4 * 3.14159 * r**2, 2)

        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, volume)

        self.txtLuasPermukaan.delete(0, END)
        self.txtLuasPermukaan.insert(END, luas_permukaan)

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()  
    aplikasi = Bola(root, "Program Luas Lingkaran")
    root.mainloop()
