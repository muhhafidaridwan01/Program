class SegiEmpat:
    def __init__(self):
        self._panjang = None 
        self._lebar = None

    @property
    def panjang(self):
        return self._panjang

    @panjang.setter
    def panjang(self, value):
        self._panjang = value

    @property
    def lebar(self):
        return self._lebar

    @lebar.setter
    def lebar(self, value):
        self._lebar = value

    def luas(self):
        return self._panjang * self._lebar

S = SegiEmpat()
P = input("Masukkan nilai panjang:")
L = input("Masukkan nilai lebar:")

S.panjang = int(P)
S.lebar = int(L)

luas = S.luas()

print("Panjang:", P)
print("Lebar:", L)
print("Luas:", luas)
