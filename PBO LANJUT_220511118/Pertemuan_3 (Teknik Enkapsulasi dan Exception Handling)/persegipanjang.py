class Persegipanjang:
    def __init__(self, panjang, lebar):
        self._panjang = 0  # private variable
        self._lebar = 0    # private variable
        self.__setPanjang(panjang)
        self.__setLebar(lebar)

    def getPanjang(self):  # Public Method
        return self._panjang

    def getLebar(self):    # Public Method
        return self._lebar

    def __setPanjang(self, nilai):  # Private Method
        if nilai <= 0:
            nilai = 1
        self._panjang = nilai

    def __setLebar(self, nilai):  # Private Method
        if nilai <= 0:
            nilai = 1
        self._lebar = nilai

    def Luas(self):
        L = self._panjang * self._lebar
        return L

    def Keliling(self):
        K = (2 * self._panjang) + (2 * self._lebar)
        return K

try:
    panjang = int(input("Masukkan nilai panjang: "))
    lebar = int(input("Masukkan nilai lebar: "))
except ValueError:
    print("Masukkan Hanya Angka Saja")
else:
    P = Persegipanjang(panjang, lebar)
    L = P.Luas()
    K = P.Keliling()
    print("Panjang:", P.getPanjang())
    print("Lebar:", P.getLebar())
    print("Luas Persegipanjang:", L)
    print("Keliling Persegipanjang:", K)
