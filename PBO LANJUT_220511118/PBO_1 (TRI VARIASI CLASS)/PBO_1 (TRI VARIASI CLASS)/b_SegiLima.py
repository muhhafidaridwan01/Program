class SegiLima:
    def __init__(self):
        self.panjang_sisi_alas = None
        self.tinggi = None
        self.panjang_sisi_tegak = None
        self.volume = None

    def hitung_volume(self, panjang_sisi_alas, tinggi, panjang_sisi_tegak):
        self.panjang_sisi_alas = panjang_sisi_alas
        self.tinggi = tinggi
        self.panjang_sisi_tegak = panjang_sisi_tegak
        self.volume = (1/3) * self.panjang_sisi_alas ** 2 * self.tinggi
        return self.volume

S = SegiLima()
panjang_sisi_alas = float(input("Masukkan Panjang Sisi Alas: "))
tinggi = float(input("Masukkan Tinggi: "))
panjang_sisi_tegak = float(input("Masukkan Panjang Sisi Tegak: "))
volume = S.hitung_volume(panjang_sisi_alas, tinggi, panjang_sisi_tegak)

print("Panjang Sisi Alas:", panjang_sisi_alas)
print("Tinggi:", tinggi)
print("Panjang Sisi Tegak:", panjang_sisi_tegak)
print("Volume:", volume)
