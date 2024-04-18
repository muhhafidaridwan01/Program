class Trapesium:
    def __init__(self, sisi_atas, sisi_bawah, tinggi, sisi_miring1, sisi_miring2):
        self._sisi_atas = 0  # private variable
        self._sisi_bawah = 0  # private variable
        self._tinggi = 0  # private variable
        self._sisi_miring1 = 0  # private variable
        self._sisi_miring2 = 0  # private variable
        self.__setSisiAtas(sisi_atas)
        self.__setSisiBawah(sisi_bawah)
        self.__setTinggi(tinggi)
        self.__setSisiMiring1(sisi_miring1)
        self.__setSisiMiring2(sisi_miring2)

    def getSisiAtas(self):
        return self._sisi_atas

    def getSisiBawah(self):
        return self._sisi_bawah

    def getTinggi(self):
        return self._tinggi

    def getSisiMiring1(self):
        return self._sisi_miring1

    def getSisiMiring2(self):
        return self._sisi_miring2

    def __setSisiAtas(self, nilai):
        if nilai <= 0:
            nilai = 1
        self._sisi_atas = nilai

    def __setSisiBawah(self, nilai):
        if nilai <= 0:
            nilai = 1
        self._sisi_bawah = nilai

    def __setTinggi(self, nilai):
        if nilai <= 0:
            nilai = 1
        self._tinggi = nilai

    def __setSisiMiring1(self, nilai):
        if nilai <= 0:
            nilai = 1
        self._sisi_miring1 = nilai

    def __setSisiMiring2(self, nilai):
        if nilai <= 0:
            nilai = 1
        self._sisi_miring2 = nilai

    def Luas(self):
        L = ((self._sisi_atas + self._sisi_bawah) * self._tinggi) / 2
        return L

    def Keliling(self):
        K = self._sisi_atas + self._sisi_bawah + self._sisi_miring1 + self._sisi_miring2
        return K

while True:
    try:
        print("=====soal 2=====")
        sisi_atas = float(input("Masukkan nilai sisi atas: "))
        sisi_bawah = float(input("Masukkan nilai sisi bawah: "))
        tinggi = float(input("Masukkan nilai tinggi: "))
        sisi_miring1 = float(input("Masukkan nilai sisi miring 1: "))
        sisi_miring2 = float(input("Masukkan nilai sisi miring 2: "))
        T = Trapesium(sisi_atas, sisi_bawah, tinggi, sisi_miring1, sisi_miring2)
        break
    except ValueError:
        print("Masukkan Hanya Angka Saja. Silakan coba lagi.")

L = T.Luas()
K = T.Keliling()
print("Sisi Atas:", T.getSisiAtas())
print("Sisi Bawah:", T.getSisiBawah())
print("Tinggi:", T.getTinggi())
print("Sisi Miring 1:", T.getSisiMiring1())
print("Sisi Miring 2:", T.getSisiMiring2())
print("Luas Trapesium:", L)
print("Keliling Trapesium:", K)
