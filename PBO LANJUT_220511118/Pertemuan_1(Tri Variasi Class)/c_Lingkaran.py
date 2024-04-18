class Lingkaran:
    def __init__(self):
        self._jari_jari = None

    @property
    def jari_jari(self):
        return self._jari_jari

    @jari_jari.setter
    def jari_jari(self, value):
        self._jari_jari = value

    def luas(self):
        return 3.14 * self._jari_jari ** 2

L = Lingkaran()
J = input("Masukkan nilai jari-jari lingkaran: ")

L.jari_jari = float(J)

luas = L.luas()

print("Jari-jari:", J)
print("Luas lingkaran:", luas)
