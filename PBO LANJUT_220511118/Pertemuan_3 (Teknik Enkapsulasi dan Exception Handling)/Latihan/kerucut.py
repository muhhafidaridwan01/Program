import math

class Kerucut:
    def __init__(self, jari_jari, tinggi):
        self._jari_jari = 0  # private variable
        self._tinggi = 0  # private variable
        self.__setJariJari(jari_jari)
        self.__setTinggi(tinggi)

    def getJariJari(self):  # Public Method
        return self._jari_jari

    def getTinggi(self):  # Public Method
        return self._tinggi

    def __setJariJari(self, nilai):  # Private Method
        if nilai <= 0:
            nilai = 1
        self._jari_jari = nilai

    def __setTinggi(self, nilai):  # Private Method
        if nilai <= 0:
            nilai = 1
        self._tinggi = nilai

    def LuasPermukaan(self):
        # Luas Permukaan = πr(r + s) dimana s adalah panjang garis pelukis (sisi miring)
        s = math.sqrt(self._jari_jari**2 + self._tinggi**2)  # Panjang garis pelukis
        L = math.pi * self._jari_jari * (self._jari_jari + s)
        return L

    def Volume(self):
        # Volume = 1/3πr^2h
        V = (1/3) * math.pi * self._jari_jari**2 * self._tinggi
        return V

while True:
    try:
        print("=====soal 3=====")
        jari_jari = float(input("Masukkan nilai jari-jari: "))
        tinggi = float(input("Masukkan nilai tinggi: "))
        K = Kerucut(jari_jari, tinggi)
        break  # Keluar dari loop jika input valid
    except ValueError:
        print("Masukkan Hanya Angka Saja. Silakan coba lagi.")

LP = K.LuasPermukaan()
V = K.Volume()
print("Jari-Jari:", K.getJariJari())
print("Tinggi:", K.getTinggi())
print("Luas Permukaan Kerucut:", LP)
print("Volume Kerucut:", V)
