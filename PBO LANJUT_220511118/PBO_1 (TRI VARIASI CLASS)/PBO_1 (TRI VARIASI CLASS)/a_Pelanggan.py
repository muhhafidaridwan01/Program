class Pelanggan:
    def __init__(self, nama, usia, alamat):
        self.nama = nama
        self.usia = usia
        self.alamat= alamat

    def info(self):
        print(f"Nama : {self.nama}\nUsia : {self.usia}\nAlamat : {self.alamat}")

plg = Pelanggan("Hafid", "19", "Ds. Jatiseeng")
plg.info()