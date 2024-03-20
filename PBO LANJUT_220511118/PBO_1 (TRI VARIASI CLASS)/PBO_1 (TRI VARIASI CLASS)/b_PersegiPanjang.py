class PersegiPanjang:
    def __init__(self):
        self.panjang = None
        self.lebar = None
        self.luas = None

    def hitung_luas(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        self.luas = self.panjang * self.lebar
        return self.luas

PP = PersegiPanjang()
panjang = input("Masukkan Nilai Panjang:")
lebar = input("Masukkan Nilai Lebar:")
luas = PP.hitung_luas(int(panjang), int(lebar))

print("Panjang:", panjang)
print("Lebar:", lebar)
print("Luas:", luas)
