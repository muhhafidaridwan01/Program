# Class Induk (Ibunya)
class Person:
    def __init__(self, nama, noktp, jk):
        self.nama = nama
        self.noktp = noktp
        self.jk = jk

# Class Turunan (Anak-anaknya)
class Manager(Person):
    def __init__(self, nama, noktp, jk):
        super().__init__(nama, noktp, jk)

class Programmer(Person):
    def __init__(self, nama, usia, noktp, jk):
        super().__init__(nama, noktp, jk)
        self.usia = usia

class Teknisi(Person):
    def __init__(self, nama, noktp, jk):
        super().__init__(nama, noktp, jk)

class Staff(Person):
    def __init__(self, nama, noktp, jk, jabatan, alamat, no_tlp):
        super().__init__(nama, noktp, jk)
        self.jabatan = jabatan
        self.alamat = alamat
        self.no_tlp = no_tlp

# Programmer
print("==== P R O G R A M M E R ===\n")
programmer1 = Programmer("HafidMer", "20", "987654321", "L")
print("Nama:", programmer1.nama, "            |")
print("Usia:", programmer1.usia, "                  |")
print("Jenis Kelamin:", programmer1.jk, "          |")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
