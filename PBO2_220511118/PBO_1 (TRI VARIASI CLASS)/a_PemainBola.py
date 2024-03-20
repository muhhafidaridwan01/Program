class PemainBola:
    def __init__(self, nama, tinggi_badan, posisi):
        self.nama = nama
        self.tinggi_badan = tinggi_badan
        self.posisi = posisi

    def info(self):
        print(f"Nama : {self.nama}\nTinggi Badan : {self.tinggi_badan}\nPosisi : {self.posisi}")

pb = PemainBola("Hafid", "175 cm", "Penyerang")
pb.info()