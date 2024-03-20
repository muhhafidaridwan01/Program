class Ustadz:
    def __init__(self, nama, usia, banyak_hafalan):
        self.nama = nama
        self.usia = usia
        self.banyak_hafalan= banyak_hafalan

    def info(self):
        print(f"Nama : {self.nama}\nUsia : {self.usia}\nBanyak Hafalan : {self.banyak_hafalan}")

ust = Ustadz("Hafid", "24", "30 Juz")
ust.info()