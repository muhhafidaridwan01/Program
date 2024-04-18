class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def info(self):
        print(f"Nama : {self.nama}\nNIM: {self.nim}")

mhs = Mahasiswa("Budi", "20034532")
mhs.info()