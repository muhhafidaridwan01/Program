class Balok:
    def __init__(self):
        self.panjang = None
        self.lebar = None
        self.tinggi = None
        self.volume = None

    def hitung_volume(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.volume = self.panjang * self.lebar * self.tinggi
        return self.volume

B = Balok()
panjang = input("Masukkan Nilai Panjang:")
lebar = input("Masukkan Nilai Lebar:")
tinggi = input("Masukkan Nilai Tinggi:")
volume = B.hitung_volume(int(panjang), int(lebar), int(tinggi))

print("Panjang:", panjang)
print("Lebar:", lebar)
print("Tinggi:", tinggi)
print("Volume:", volume)
