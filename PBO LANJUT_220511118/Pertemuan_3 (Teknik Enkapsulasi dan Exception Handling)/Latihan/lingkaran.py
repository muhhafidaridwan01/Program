import math

class Lingkaran:
    def __init__(self, jari_jari):
        self._jari_jari = 0  # private variable
        self.__setJariJari(jari_jari)

    def getJariJari(self):  # Public Method
        return self._jari_jari

    def __setJariJari(self, nilai):  # Private Method
        if nilai <= 0:
            nilai = 1
        self._jari_jari = nilai

    def Luas(self):
        L = math.pi * self._jari_jari ** 2
        return L

    def Keliling(self):
        K = 2 * math.pi * self._jari_jari
        return K

while True:
    try:
        print("=====soal 1=====")
        jari_jari = float(input("Masukkan nilai jari-jari: "))
        C = Lingkaran(jari_jari)
        break  # Keluar dari loop jika input valid
    except ValueError:
        print("Masukkan Hanya Angka Saja. Silakan coba lagi.")

L = C.Luas()
K = C.Keliling()
print("Jari-Jari:", C.getJariJari())
print("Luas Lingkaran:", L)
print("Keliling Lingkaran:", K)
