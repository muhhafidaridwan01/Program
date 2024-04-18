import math

class Segitiga:
    def __init__(self, alas, tinggi):
        self._alas = 0
        self._tinggi = 0
        self.__setAlas(alas)
        self.__setTinggi(tinggi)

    def getAlas(self):  # Public Method
        return self._alas

    def getTinggi(self):  # Public Method
        return self._tinggi

    def getSisiMiring(self):
        C = round(math.sqrt((self._alas**2) + (self._tinggi**2)), 2)
        return C

    def __setAlas(self, nilai):  # Private Method
        if nilai <= 0:
            nilai = 1
        self._alas = nilai

    def __setTinggi(self, nilai):  # Private Method
        if nilai <= 0:
            nilai = 1
        self._tinggi = nilai

    def Luas(self):  # Public Method
        L = 0.5 * self._alas * self._tinggi  # Perbaikan dari koma ke titik
        return L

    def Keliling(self):
        K = round(self.getSisiMiring() + self._alas + self._tinggi, 2)
        return K

try:
    alas = int(input("Masukkan nilai alas: "))
    tinggi = int(input("Masukkan nilai tinggi: "))
except ValueError:
    print("Masukkan hanya angka saja")
else:
    P = Segitiga(alas,tinggi)
    L = P.Luas()
    K = P.Keliling()
print("Alas:",P.getAlas())
print("Tinggi",P.getTinggi())
print("Sisi Miring",P.getSisiMiring())
print("Luas Segitigas:",L)
print("Keliling Segitiga:",K)