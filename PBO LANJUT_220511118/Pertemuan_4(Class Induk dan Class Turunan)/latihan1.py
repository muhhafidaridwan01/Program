# Class Induk (Ibunya)
class Person:
    def __init__(self, nama, noktp, jk):
        self.nama = nama
        self.noktp = noktp
        self.jk = jk

# Class Turunan (Anak-anaknya)
class Dokter(Person):
    def __init__(self, nama, noktp, jk, spesialis, alamat, no_tlp):
        super().__init__(nama, noktp, jk)
        self.spesialis = spesialis
        self.alamat = alamat
        self.no_tlp = no_tlp

class Perawat(Person):
    def __init__(self, nama, noktp, jk, spesialis, alamat, no_tlp):
        super().__init__(nama, noktp, jk)
        self.spesialis = spesialis
        self.alamat = alamat
        self.no_tlp = no_tlp

class Karyawan(Person):
    def __init__(self, nama, nip, jk, jabatan, alamat, no_tlp):
        super().__init__(nama, nip, jk)
        self.jabatan = jabatan
        self.nip = nip
        self.alamat = alamat
        self.no_tlp = no_tlp

dokter1 = Dokter("Muhammad", "12345", "L", "Mata", "Jatiseeng", "081224455249")
print("=========== D O K T E R =========\n")

print("Nama:", dokter1.nama, "                  |")          
print("Spesialis:", dokter1.spesialis, "                 |")
print("Alamat:", dokter1.alamat, "               |")
print("Nomor Telepon:", dokter1.no_tlp, "     |")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")


perawat2 = Perawat("Hafid", "12345", "L", "Hati", "Jatiseeng Kidul", "08112678980")
print("========== P E R A W A T ========\n")

print("Nama:", perawat2.nama, "                     |")          
print("Jenis Kelamin:", perawat2.jk, "                |") 
print("Spesialis:", perawat2.spesialis, "                 |")
print("Alamat:", perawat2.alamat, "         |")
print("Nomor Telepon:", perawat2.no_tlp, "      |")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")  


karyawan3 = Karyawan("Syafira", "12345", "P", "Admin", "Jatiseeng Lor", "08112678980")
print("========= K A R Y A W A N =======\n")

print("Nama:", karyawan3.nama, "                   |")          
print("Nip:", karyawan3.nip,"                      |")
print("Jenis Kelamin:", karyawan3.jk, "                |") 
print("Jabatan:", karyawan3.jabatan, "                  |")
print("Alamat:", karyawan3.alamat, "           |")
print("Nomor Telepon:", karyawan3.no_tlp, "      |")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
