# Class Induk (Ibunya)
class Person:
    def __init__(self, nama, noktp, jk):
        self.nama = nama
        self.noktp = noktp
        self.jk = jk

# Class Turunan (Anak-anaknya)
class Dosen(Person):
    def __init__(self, nama, nidn, jk):
        super().__init__(nama, '', jk)  # NIDN tidak ada pada kelas induk
        self.nidn = nidn

class Mahasiswa(Person):
    def __init__(self, nama, noktp, jk, nim, fakultas, prodi, angkatan):
        super().__init__(nama, noktp, jk)
        self.nim = nim
        self.fakultas = fakultas
        self.prodi = prodi
        self.angkatan = angkatan

class Staff(Person):
    def __init__(self, nama, noktp, jk, jabatan, alamat, no_tlp):
        super().__init__(nama, noktp, jk)
        self.jabatan = jabatan
        self.alamat = alamat
        self.no_tlp = no_tlp

class Satpam(Person):
    def __init__(self, nama, noktp, jk, area_penjagaan):
        super().__init__(nama, noktp, jk)
        self.area_penjagaan = area_penjagaan

class OB(Person):
    def __init__(self, nama, noktp, jk, ruangan):
        super().__init__(nama, noktp, jk)
        self.ruangan = ruangan

# Satpam
print("========== S A T P A M =========\n")
satpam1 = Satpam("Babeh", "3209010120147", "L", "Kampus 3 UMC")
print("Nama:", satpam1.nama,"                   |")
print("Nomor KTP:", satpam1.noktp, "      |")
print("Jenis Kelamin:", satpam1.jk,"              |")
print("Area Penjagaan:", satpam1.area_penjagaan, "  |")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
