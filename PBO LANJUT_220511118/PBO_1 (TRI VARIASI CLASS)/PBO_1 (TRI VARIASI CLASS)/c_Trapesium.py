class Trapesium:
    def __init__(self):
        self._sisi_atas = None
        self._sisi_bawah = None
        self._tinggi = None

    @property
    def sisi_atas(self):
        return self._sisi_atas

    @sisi_atas.setter
    def sisi_atas(self, value):
        self._sisi_atas = value

    @property
    def sisi_bawah(self):
        return self._sisi_bawah

    @sisi_bawah.setter
    def sisi_bawah(self, value):
        self._sisi_bawah = value

    @property
    def tinggi(self):
        return self._tinggi

    @tinggi.setter
    def tinggi(self, value):
        self._tinggi = value

    def luas(self):
        return 0.5 * (self._sisi_atas + self._sisi_bawah) * self._tinggi

T = Trapesium()
A = input("Masukkan nilai sisi atas: ")
B = input("Masukkan nilai sisi bawah: ")
Tinggi = input("Masukkan nilai tinggi: ")

T.sisi_atas = float(A)
T.sisi_bawah = float(B)
T.tinggi = float(Tinggi)

luas = T.luas()

print("Sisi Atas:", A)
print("Sisi Bawah:", B)
print("Tinggi:", Tinggi)
print("Luas trapesium:", luas)
